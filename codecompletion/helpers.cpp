/*****************************************************************************
 * This file is part of KDevelop
 * Copyright (c) 2011-2012 Sven Brauch <svenbrauch@googlemail.com>           *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *           
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *   
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */

#include "helpers.h"

#include <language/duchain/abstractfunctiondeclaration.h>
#include <language/duchain/duchainutils.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/declaration.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/types/integraltype.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>

#include <QStringList>
#include <QTextFormat>

#include "parser/codehelpers.h"

using namespace KDevelop;

namespace Python {

ExpressionParser::ExpressionParser(QString code)
    : m_code(code.trimmed())
    , m_cursorPositionInString(m_code.length())
{
    
}

QString ExpressionParser::getRemainingCode()
{
    return m_code.mid(0, m_cursorPositionInString);
}

QString ExpressionParser::getScannedCode()
{
    return m_code.mid(m_cursorPositionInString, m_code.length() - m_cursorPositionInString);
}

int ExpressionParser::trailingWhitespace()
{
    int ws = 0;
    int index = m_cursorPositionInString - 1;
    while ( index >= 0 ) {
        if ( m_code.at(index).isSpace() ) {
            ws++;
            index --;
        }
        else {
            break;
        }
    }
    return ws;
}

void ExpressionParser::reset()
{
    m_cursorPositionInString = m_code.length();
}

QString ExpressionParser::skipUntilStatus(ExpressionParser::Status status, bool* ok, int* expressionsSkipped)
{
    if ( expressionsSkipped ) {
        *expressionsSkipped = 0;
    }
    QString lastExpression;
    Status currentStatus = InvalidStatus;
    while ( currentStatus != status ) {
        lastExpression = popExpression(&currentStatus);
        kDebug() << lastExpression << currentStatus;
        if ( currentStatus == NothingFound ) {
            *ok = false;
            return QString();
        }
        if ( expressionsSkipped && currentStatus == ExpressionFound ) {
            *expressionsSkipped += 1;
        }
    }
    *ok = true;
    return lastExpression;
}

QString ExpressionParser::popExpression(ExpressionParser::Status* status)
{
    QString operatingOn = getRemainingCode().trimmed();
    if ( operatingOn.isEmpty() ) {
        *status = NothingFound;
        return QString();
    }
    m_cursorPositionInString -= trailingWhitespace();
    if ( operatingOn.endsWith(',') ) {
        m_cursorPositionInString -= 1;
        *status = CommaFound;
        return QString();
    }
    if ( operatingOn.endsWith("import") ) {
        m_cursorPositionInString -= 6;
        *status = ImportFound;
        return QString();
    }
    if ( operatingOn.endsWith("from") ) {
        m_cursorPositionInString -= 4;
        *status = FromFound;
        return QString();
    }
    if ( operatingOn.endsWith("print") ) {
        m_cursorPositionInString -= 5;
        *status = PrintFound;
        return QString();
    }
    if ( operatingOn.endsWith('.') ) {
        m_cursorPositionInString -= 1;
        *status = MemberAccessFound;
        return QString();
    }
    if ( operatingOn.endsWith('(') ) {
        for ( int index = operatingOn.length() - 2; index >= 0; index-- ) {
            QChar c = operatingOn.at(index);
            if ( c.isSpace() ) continue;
            if ( c.isLetterOrNumber() || c == '_' ) {
                // call of a function referenced by name
                m_cursorPositionInString -= 1;
                *status = CallFound;
                return QString();
            }
            else {
                // not a call, or not one we can deal with
                break;
            }
        }
    }
    if ( operatingOn.endsWith('[') || operatingOn.endsWith('{') || operatingOn.endsWith('(') ) {
        m_cursorPositionInString -= 1;
        *status = InitializerFound;
        return QString();
    }
    // Otherwise, there's a real expression at the cursor, so scan it.
    QStringList lines = operatingOn.split('\n');
    Python::TrivialLazyLineFetcher f(lines);
    int lastLine = lines.length()-1;
    QString expr = CodeHelpers::expressionUnderCursor(f, KTextEditor::Cursor(lastLine, f.fetchLine(lastLine).length() - 1), true);
    if ( expr.isEmpty() ) {
        *status = NothingFound;
    }
    else {
        *status = ExpressionFound;
    }
    m_cursorPositionInString -= expr.length();
    return expr;
}


// This is stolen from PHP. For credits, see helpers.cpp in PHP.
void createArgumentList(Declaration* dec, QString& ret, QList<QVariant>* highlighting, int atArg)
{
    int textFormatStart = 0;
    QTextFormat normalFormat(QTextFormat::CharFormat);
    QTextFormat highlightFormat(QTextFormat::CharFormat);
    highlightFormat.setBackground(Qt::green);
    
    AbstractFunctionDeclaration* decl = dynamic_cast<AbstractFunctionDeclaration*>(dec);
    FunctionType::Ptr functionType = dec->type<FunctionType>();
    
    if (functionType && decl) {

        QVector<Declaration*> parameters;
        if (DUChainUtils::getArgumentContext(dec))
            parameters = DUChainUtils::getArgumentContext(dec)->localDeclarations();

        uint defaultParamNum = 0;

        int firstDefaultParam = parameters.count() - decl->defaultParametersSize();

        ret = '(';
        bool first = true;
        int num = 0;
        
        bool skipFirst = false;
        if ( parameters.count() > functionType->arguments().count() ) {
            // the function is a class method, and its first argument is "self". Don't display that.
            skipFirst = true;
        }
        
        foreach(Declaration* dec, parameters) {
            if ( skipFirst ) {
                skipFirst = false;
                continue;
            }
            // that has nothing to do with the skip, it's just for the comma
            if (first)
                first = false;
            else
                ret += ", ";

            bool doHighlight = false;
            QTextFormat doFormat;
            
            if ( num == atArg - 1 )
                doFormat = highlightFormat;
            else
                doFormat = normalFormat;

            doHighlight = true;

            if (doHighlight) {
                if (highlighting && ret.length() != textFormatStart) {
                    //Add a default-highlighting for the passed text
                    *highlighting <<  QVariant(textFormatStart);
                    *highlighting << QVariant(ret.length() - textFormatStart);
                    *highlighting << QVariant(normalFormat);
                    textFormatStart = ret.length();
                }
            }

            if (num < functionType->arguments().count()) {
                if (AbstractType::Ptr type = functionType->arguments().at(num)) {
                    if ( type->toString() != "<unknown>" ) {
                        ret += type->toString() + ' ';
                    }
                }
            }

            ret += dec->identifier().toString();

            if (doHighlight) {
                if (highlighting && ret.length() != textFormatStart) {
                    *highlighting <<  QVariant(textFormatStart);
                    *highlighting << QVariant(ret.length() - textFormatStart);
                    *highlighting << doFormat;
                    textFormatStart = ret.length();
                }
            }


            if (num >= firstDefaultParam) {
                ret += " = " + decl->defaultParameters()[defaultParamNum].str();
                ++defaultParamNum;
            }

            ++num;
        }
        ret += ')';

        if (highlighting && ret.length() != textFormatStart) {
            *highlighting <<  QVariant(textFormatStart);
            *highlighting << QVariant(ret.length());
            *highlighting << normalFormat;
            textFormatStart = ret.length();
        }
        return;
    }
}

}