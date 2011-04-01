#include "helpers.h"
#include <language/duchain/abstractfunctiondeclaration.h>
#include <language/duchain/duchainutils.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/types/functiontype.h>
#include <QTextFormat>
#include <QStringList>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/declaration.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>

using namespace KDevelop;

namespace Python {

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