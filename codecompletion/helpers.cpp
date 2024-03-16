/*
    SPDX-FileCopyrightText: 2011-2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

// Note to confused people reading this code: This is not the parser.
// It's just a minimalist helper class for code completion. The parser is in the parser/ directory.

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

#include <QDebug>
#include "codecompletiondebug.h"

#include "duchain/declarations/functiondeclaration.h"
#include "parser/codehelpers.h"

using namespace KDevelop;

namespace Python {

QString camelCaseToUnderscore(const QString& camelCase)
{
    QString underscore;
    for ( int i = 0; i < camelCase.size(); i++ ) {
        const QChar& c = camelCase.at(i);
        if ( c.isUpper() && i != 0 ) {
            underscore.append(QLatin1Char('_'));
        }
        underscore.append(c.toLower());
    }
    return underscore;
}

int identifierMatchQuality(const QString& identifier1_, const QString& identifier2_)
{
    QString identifier1 = camelCaseToUnderscore(identifier1_).toLower().replace(QLatin1Char('.'), QLatin1Char('_'));
    QString identifier2 = camelCaseToUnderscore(identifier2_).toLower().replace(QLatin1Char('.'), QLatin1Char('_'));

    if ( identifier1 == identifier2 ) {
        return 3;
    }
    if ( identifier1.contains(identifier2) || identifier2.contains(identifier1) ) {
        return 2;
    }
    QStringList parts1 = identifier1.split(QLatin1Char('_'));
    QStringList parts2 = identifier2.split(QLatin1Char('_'));
    parts1.removeAll(QString());
    parts2.removeAll(QString());
    parts1.removeDuplicates();
    parts2.removeDuplicates();
    if ( parts1.length() > 5 || parts2.length() > 5 ) {
        // don't waste time comparing huge identifiers,
        // the matching is probably pointless anyways for people using
        // more than 5 words for their variable names
        return 0;
    }
    for ( const QString& part1 : parts1 ) {
        for ( const QString& part2 : parts2 ) {
            // Don't take very short name parts into account,
            // those are not very descriptive eventually
            if ( part1.size() < 3 || part2.size() < 3 ) {
                continue;
            }
            if ( part1 == part2 ) {
                // partial match
                return 1;
            }
        }
    }
    return 0;
}

typedef QPair<QString, ExpressionParser::Status> keyword;

static QList<keyword> supportedKeywords;
static QList<keyword> controlChars;
static QList<QString> miscKeywords;
static QList<QString> noCompletionKeywords;
static QMutex keywordPopulationLock;

// Keywords known to me:
// and       del       for       is        raise    
// assert    elif      from      lambda    return   
// break     else      global    not       try      
// class     except    if        or        while    
// continue  exec      import    pass      yield    
// def       finally   in        print     with
// async     await

ExpressionParser::ExpressionParser(QString code)
    : m_code(code)
    , m_cursorPositionInString(m_code.length())
{
    keywordPopulationLock.lock();
    if ( supportedKeywords.isEmpty() ) {
        noCompletionKeywords << QStringLiteral("break") << QStringLiteral("class") << QStringLiteral("continue") << QStringLiteral("pass")
                             << QStringLiteral("try") << QStringLiteral("else") << QStringLiteral("as") << QStringLiteral("finally")
                             << QStringLiteral("global") << QStringLiteral("lambda");
        miscKeywords << QStringLiteral("and") << QStringLiteral("assert") << QStringLiteral("del") << QStringLiteral("elif") << QStringLiteral("exec")
                     << QStringLiteral("if") << QStringLiteral("is") << QStringLiteral("not")
                     << QStringLiteral("or") << QStringLiteral("print") << QStringLiteral("return") << QStringLiteral("while")
                     << QStringLiteral("yield") << QStringLiteral("with") << QStringLiteral("await");
        supportedKeywords << keyword(QStringLiteral("import"), ExpressionParser::ImportFound);
        supportedKeywords << keyword(QStringLiteral("from"), ExpressionParser::FromFound);
        supportedKeywords << keyword(QStringLiteral("raise"), ExpressionParser::RaiseFound);
        supportedKeywords << keyword(QStringLiteral("in"), ExpressionParser::InFound);
        supportedKeywords << keyword(QStringLiteral("for"), ExpressionParser::ForFound);
        supportedKeywords << keyword(QStringLiteral("class"), ExpressionParser::ClassFound);
        supportedKeywords << keyword(QStringLiteral("def"), ExpressionParser::DefFound);
        supportedKeywords << keyword(QStringLiteral("except"), ExpressionParser::ExceptFound);
        controlChars << keyword(QStringLiteral(":"), ExpressionParser::ColonFound);
        controlChars << keyword(QStringLiteral(","), ExpressionParser::CommaFound);
        controlChars << keyword(QStringLiteral("("), ExpressionParser::InitializerFound);
        controlChars << keyword(QStringLiteral("{"), ExpressionParser::InitializerFound);
        controlChars << keyword(QStringLiteral("["), ExpressionParser::InitializerFound);
        controlChars << keyword(QStringLiteral("."), ExpressionParser::MemberAccessFound);
        controlChars << keyword(QStringLiteral("="), ExpressionParser::EqualsFound);
    }
    keywordPopulationLock.unlock();
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

QString ExpressionParser::skipUntilStatus(ExpressionParser::Status requestedStatus, bool* ok, int* expressionsSkipped)
{
    if ( expressionsSkipped ) {
        *expressionsSkipped = 0;
    }
    QString lastExpression;
    Status currentStatus = InvalidStatus;
    while ( currentStatus != requestedStatus ) {
        lastExpression = popExpression(&currentStatus);
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << lastExpression << currentStatus;
        if ( currentStatus == NothingFound ) {
            *ok = ( requestedStatus == NothingFound ); // ok exactly if the caller requested NothingFound as end status
            return QString();
        }
        if ( expressionsSkipped && currentStatus == ExpressionFound ) {
            *expressionsSkipped += 1;
        }
    }
    *ok = true;
    return lastExpression;
}

TokenList ExpressionParser::popAll()
{
    Status currentStatus = InvalidStatus;
    TokenList items;
    while ( currentStatus != NothingFound ) {
        QString result = popExpression(&currentStatus);
        items << TokenListEntry(currentStatus, result, m_cursorPositionInString);
    }
    std::reverse(items.begin(), items.end());
    return items;
}

bool endsWithSeperatedKeyword(const QString& str, const QString& shouldEndWith) {
    bool endsWith = str.endsWith(shouldEndWith);
    if ( ! endsWith ) {
        return false;
    }
    int l = shouldEndWith.length();
    if ( str.length() == l ) {
        return true;
    }
    if ( str.right(l + 1).at(0).isSpace() ) {
        return true;
    }
    return false;
}

QString ExpressionParser::popExpression(ExpressionParser::Status* status)
{
    const auto remaining = getRemainingCode();
    auto trimmed = remaining.trimmed();
    auto operatingOn = trimmed.replace(QLatin1Char('\t'), QLatin1Char(' '));
    bool lineIsEmpty = false;
    for ( auto it = remaining.constEnd()-1; it != remaining.constEnd(); it-- ) {
        if ( ! it->isSpace() ) {
            break;
        }
        if ( *it == QLatin1Char('\n') ) {
            lineIsEmpty = true;
            break;
        }
    }
    if ( operatingOn.isEmpty() || lineIsEmpty ) {
        m_cursorPositionInString = 0;
        *status = NothingFound;
        return QString();
    }
    bool lastCharIsSpace = getRemainingCode().right(1).at(0).isSpace();
    m_cursorPositionInString -= trailingWhitespace();
    if ( operatingOn.endsWith(QLatin1Char('(')) ) {
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "eventual call found";
        m_cursorPositionInString -= 1;
        *status = EventualCallFound;
        return QString();
    }
    for ( const keyword& kw : controlChars ) {
        if ( operatingOn.endsWith(kw.first) ) {
            m_cursorPositionInString -= kw.first.length();
            *status = kw.second;
            return QString();
        }
    }
    if ( lastCharIsSpace ) {
        for ( const keyword& kw : supportedKeywords ) {
            if ( endsWithSeperatedKeyword(operatingOn, kw.first) ) {
                m_cursorPositionInString -= kw.first.length();
                *status = kw.second;
                return QString();
            }
        }
        for ( const QString& kw : miscKeywords ) {
            if ( endsWithSeperatedKeyword(operatingOn, kw) ) {
                m_cursorPositionInString -= kw.length();
                *status = MeaninglessKeywordFound;
                return QString();
            }
        }
        for ( const QString& kw : noCompletionKeywords ) {
            if ( endsWithSeperatedKeyword(operatingOn, kw) ) {
                m_cursorPositionInString -= kw.length();
                *status = NoCompletionKeywordFound;
                return QString();
            }
        }
    }
    // Otherwise, there's a real expression at the cursor, so scan it.
    QStringList lines = operatingOn.split(QLatin1Char('\n'));
    Python::TrivialLazyLineFetcher f(lines);
    int lastLine = lines.length()-1;
    KTextEditor::Cursor startCursor;
    QString expr = CodeHelpers::expressionUnderCursor(f, KTextEditor::Cursor(lastLine, f.fetchLine(lastLine).length() - 1),
                                                      startCursor, true);
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
void createArgumentList(Declaration* dec_, QString& ret, QList< QVariant >* highlighting, int atArg, bool includeTypes)
{
    auto dec = dynamic_cast<Python::FunctionDeclaration*>(dec_);
    if ( ! dec ) {
        return;
    }
    int textFormatStart = 0;
    QTextFormat normalFormat(QTextFormat::CharFormat);
    QTextFormat highlightFormat(QTextFormat::CharFormat);
    highlightFormat.setBackground(QColor::fromRgb(142, 186, 255));
    highlightFormat.setProperty(QTextFormat::FontWeight, 99);
    
    AbstractFunctionDeclaration* decl = dynamic_cast<AbstractFunctionDeclaration*>(dec);
    FunctionType::Ptr functionType = dec->type<FunctionType>();
    
    if (functionType && decl) {

        QVector<Declaration*> parameters;
        if (DUChainUtils::argumentContext(dec))
            parameters = DUChainUtils::argumentContext(dec)->localDeclarations();

        ret = QLatin1Char('(');
        bool first = true;
        int num = 0;
        
        bool skipFirst = false;
        if ( dec->context() && dec->context()->type() == DUContext::Class && ! dec->isStatic() ) {
            // the function is a class method, and its first argument is "self". Don't display that.
            skipFirst = true;
        }

        uint defaultParamNum = 0;
        int firstDefaultParam = parameters.count() - decl->defaultParametersSize() - skipFirst;

        // disable highlighting when in default arguments, it doesn't make much sense then
        bool disableHighlighting = false;
        
        for (Declaration* dec : parameters) {
            if ( skipFirst ) {
                skipFirst = false;
                continue;
            }
            // that has nothing to do with the skip, it's just for the comma
            if (first)
                first = false;
            else
                ret += QStringLiteral(", ");

            bool doHighlight = false;
            QTextFormat doFormat;
            
            if ( num == atArg - 1 )
                doFormat = highlightFormat;
            else
                doFormat = normalFormat;
            
            if ( num == firstDefaultParam ) {
                ret += QStringLiteral("[");
                ++defaultParamNum;
                disableHighlighting = true;
            }
            
            if ( ! disableHighlighting ) {
                doHighlight = true;
            }
            
            if ( includeTypes ) {
                if (num < functionType->arguments().count()) {
                    if (AbstractType::Ptr type = functionType->arguments().at(num)) {
                        if ( type->toString() != QStringLiteral("<unknown>") ) {
                            ret += type->toString() + QLatin1Char(' ');
                        }
                    }
                }
                
                if (doHighlight) {
                    if (highlighting && ret.length() != textFormatStart) {
                        //Add a default-highlighting for the passed text
                        *highlighting << QVariant(textFormatStart);
                        *highlighting << QVariant(ret.length() - textFormatStart);
                        *highlighting << QVariant(normalFormat);
                        textFormatStart = ret.length();
                    }
                }
            }
            
            
            ret += dec->identifier().toString();

            if (doHighlight) {
                if (highlighting && ret.length() != textFormatStart) {
                    *highlighting << QVariant(textFormatStart + 1);
                    *highlighting << QVariant(ret.length() - textFormatStart - 1);
                    *highlighting << doFormat;
                    textFormatStart = ret.length();
                }
            }

            ++num;
        }
        if ( defaultParamNum != 0 ) {
            ret += QLatin1Char(']');
        }
        ret += QLatin1Char(')');

        if (highlighting && ret.length() != textFormatStart) {
            *highlighting <<  QVariant(textFormatStart);
            *highlighting << QVariant(ret.length());
            *highlighting << normalFormat;
            textFormatStart = ret.length();
        }
        return;
    }
}

StringFormatter::StringFormatter(const QString &string)
    : m_string(string)
{
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "String being parsed: " << string;
    QRegularExpression regex(QStringLiteral("\\{(\\w+)(?:!([rs]))?(?:\\:(.*))?\\}"),
                             QRegularExpression::InvertedGreedinessOption);

    QRegularExpressionMatchIterator i = regex.globalMatch(string);
    while (i.hasNext()) {
        QRegularExpressionMatch match = i.next();
        QString identifier = match.captured(1);
        QString conversionStr = match.captured(2);
        QChar conversion = (conversionStr.isNull() || conversionStr.isEmpty()) ? QChar() : conversionStr.at(0);
        QString formatSpec = match.captured(3);

        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "variable: " << match.captured(0);

        // The regex guarantees that conversion is only a single character
        ReplacementVariable variable(identifier, conversion, formatSpec);
        m_replacementVariables.append(variable);

        RangeInString variablePosition(match.capturedStart(), match.capturedEnd());
        m_variablePositions.append(variablePosition);
    }
}

bool StringFormatter::isInsideReplacementVariable(int cursorPosition) const
{
    return getReplacementVariable(cursorPosition) != nullptr;
}

const ReplacementVariable *StringFormatter::getReplacementVariable(int cursorPosition) const
{
    int index = 0;
    for ( const RangeInString &variablePosition : m_variablePositions ) {
        if ( cursorPosition >= variablePosition.beginIndex && cursorPosition <= variablePosition.endIndex ) {
            return &m_replacementVariables.at(index);
        }
        index++;
    }

    return nullptr;
}

RangeInString StringFormatter::getVariablePosition(int cursorPosition) const
{
    int index = 0;
    for ( const RangeInString &variablePosition : m_variablePositions ) {
        if ( cursorPosition >= variablePosition.beginIndex && cursorPosition <= variablePosition.endIndex ) {
            return m_variablePositions.at(index);
        }
        index++;
    }
    return RangeInString();
}

int StringFormatter::nextIdentifierId() const
{
    int highestIdFound = -1;
    for ( const ReplacementVariable &variable : m_replacementVariables ) {
        bool isNumeric;
        int identifier = variable.identifier().toInt(&isNumeric);
        if ( isNumeric && identifier > highestIdFound ) {
            highestIdFound = identifier;
        }
    }
    return highestIdFound + 1;
}

}
