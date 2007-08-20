#include "pythonhighlighting.h"

#include <ktexteditor/smartrange.h>

#include <topducontext.h>
#include <declaration.h>
#include <definition.h>
#include <use.h>
#include <duchain.h>
#include <duchainlock.h>

using namespace KTextEditor;
using namespace KDevelop;

PythonHighlighting::PythonHighlighting( QObject * parent )
  : QObject(parent)
{
}

PythonHighlighting::~PythonHighlighting( )
{
}

KTextEditor::Attribute::Ptr PythonHighlighting::attributeForType( Types type, Contexts context ) const
{
    KTextEditor::Attribute::Ptr a;
    a = m_definitionAttributes[type];
    if (!a)
    {
        a = KTextEditor::Attribute::Ptr(new KTextEditor::Attribute());
        a->setBackgroundFillWhitespace(true);
        m_definitionAttributes.insert(type, a);
        switch (type)
        {
            case ArgumentType:
                a->setBackground(QColor(Qt::green).light(175));
                break;
            case ClassType:
                a->setForeground(Qt::blue);
                break;
            case FunctionType:
                a->setBackground(QColor(Qt::blue).light(175));
                break;
            case FunctionVariableType:
                a->setForeground(QColor(0x1F88A7));
                break;
            case ClassVariableType:
                a->setForeground(QColor(0xFF800D));
                break;
        }
        a->setFontBold();
    }
    return a;
}

void PythonHighlighting::highlightTree( KTextEditor::SmartRange * range ) const
{
    foreach (KTextEditor::SmartRange* child, range->childRanges())
        highlightTree(child);
}

void PythonHighlighting::outputRange( KTextEditor::SmartRange * range ) const
{
    Q_ASSERT(range->start() <= range->end());
    foreach (SmartRange* child, range->childRanges())
        outputRange(child);
}

void PythonHighlighting::highlightDUChain(KDevelop::TopDUContext* context) const
{
    DUChainReadLocker lock(DUChain::lock());
    Q_ASSERT(context->topContext() == context);
    highlightDUChain(static_cast<DUContext*>(context));
}

void PythonHighlighting::highlightDUChain(DUContext* context) const
{
    if (!context->smartRange())
        return;
    foreach (Declaration* dec, context->localDeclarations())
        highlightDeclaration(dec);
    foreach (Definition* def, context->localDefinitions())
        highlightDefinition(def);
    foreach (DUContext* child, context->childContexts())
        highlightDUChain(child);
}

#include "pythonhighlighting.moc"

PythonHighlighting::Types PythonHighlighting::typeForDeclaration(Declaration * dec) const
{
    Types type;
    switch (dec->context()->type()) 
    {
      case DUContext::Class:
        type = ClassVariableType;
        break;
      case DUContext::Function:
        type = FunctionVariableType;
        break;
      default:
        break;
    }
    return type;
}

void PythonHighlighting::highlightDefinition(Definition * definition) const
{
    if (Declaration* declaration = definition->declaration())
        if (SmartRange* range = definition->smartRange())
            range->setAttribute(attributeForType(typeForDeclaration(declaration), DeclarationContext));
}

void PythonHighlighting::highlightDeclaration(Declaration * declaration) const
{
    if (SmartRange* range = declaration->smartRange())
        range->setAttribute(attributeForType(typeForDeclaration(declaration), DeclarationContext));
}
