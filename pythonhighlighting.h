#ifndef KDEVCPPHIGHLIGHTING_H
#define KDEVCPPHIGHLIGHTING_H

#include <QObject>
#include <QHash>
#include <QModelIndex>

#include <ktexteditor/attribute.h>
#include <icodehighlighting.h>

namespace KTextEditor
{
    class SmartRange;
}

namespace KDevelop
{
    class DUContext;
    class Declaration;
}

class PythonHighlighting : public QObject, public KDevelop::ICodeHighlighting
{
    Q_OBJECT
    Q_INTERFACES(KDevelop::ICodeHighlighting)
public:

    enum Types 
    {
        FunctionType,
        ClassType,
        ArgumentType,
        FunctionVariableType,
        ClassVariableType
    };
    enum Contexts 
    {
        DefinitionContext,
        DeclarationContext
    };
    PythonHighlighting(QObject* parent);
    virtual ~PythonHighlighting();

    void highlightTree(KTextEditor::SmartRange* topRange) const;
    void highlightDUChain(KDevelop::TopDUContext* context) const;

    virtual void highlightDefinition(KDevelop::Definition* definition) const;
    virtual void highlightDeclaration(KDevelop::Declaration* declaration) const;
    KTextEditor::Attribute::Ptr attributeForType(Types type, Contexts context) const;
private:
    void highlightDUChain(KDevelop::DUContext* context) const;
    void outputRange( KTextEditor::SmartRange * range ) const;

    Types typeForDeclaration(KDevelop::Declaration* dec) const;

    mutable QHash<Types, KTextEditor::Attribute::Ptr> m_definitionAttributes;
    mutable QHash<Types, KTextEditor::Attribute::Ptr> m_declarationAttributes;
};

#endif
