/*****************************************************************************
 * Copyright 2010 Miquel Canes Gonzalez <miquelcanes@gmail.com>              *
 * Copyright 2011-2013 Sven Brauch <svenbrauch@googlemail.com>               *
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

#ifndef EXPRESSIONVISITOR_H
#define EXPRESSIONVISITOR_H

#include <QHash>
#include <KLocalizedString>

#include <language/duchain/types/abstracttype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/types/typeregister.h>
#include <language/duchain/duchainpointer.h>
#include <language/duchain/declaration.h>
#include <language/duchain/types/structuretype.h>
#include <language/duchain/functiondeclaration.h>

#include "astdefaultvisitor.h"
#include "pythonduchainexport.h"
#include "pythoneditorintegrator.h"

#include "duchain/declarations/classdeclaration.h"
#include "duchain/declarations/functiondeclaration.h"
#include "types/variablelengthcontainer.h"

namespace KDevelop {
    class Identifier;
}

using namespace KDevelop;

namespace Python
{

typedef DUChainPointer<FunctionDeclaration> FunctionDeclarationPointer;

class KDEVPYTHONDUCHAIN_EXPORT ExpressionVisitor : public AstDefaultVisitor
{
    public:
        ExpressionVisitor(KDevelop::DUContext* ctx, PythonEditorIntegrator* editor = 0);
        // use this to construct the expression-visitor recursively
        ExpressionVisitor(ExpressionVisitor* parent);
        
        virtual void visitBinaryOperation(BinaryOperationAst* node);
        virtual void visitUnaryOperation(UnaryOperationAst* node);
        virtual void visitBooleanOperation(BooleanOperationAst* node);
        virtual void visitCompare(CompareAst* node);
        
        virtual void visitString(StringAst* node);
        virtual void visitNumber(NumberAst* node);
        virtual void visitName(NameAst* node);
        virtual void visitList(ListAst* node);
        virtual void visitDict(DictAst* node);
        virtual void visitSet(SetAst* node);
        virtual void visitSubscript(SubscriptAst* node);
        virtual void visitCall(CallAst* node);
        virtual void visitAttribute(AttributeAst* node);
        virtual void visitTuple(TupleAst* node);
        virtual void visitListComprehension(ListComprehensionAst* node);
        virtual void visitDictionaryComprehension(DictionaryComprehensionAst* node);
        virtual void visitSetComprehension(SetComprehensionAst* node);
        virtual void visitIfExpression(IfExpressionAst* node);
        virtual void visitNameConstant(NameConstantAst* node);
        
        void addUnknownName(const QString& name);

        /// Checks the decorators of the given function declaration. Returns true
        /// if one determining the type of the expression was found.
        void checkForDecorators(CallAst* node, Python::FunctionDeclaration* funcDecl,
                                Python::ClassDeclaration* classDecl, bool isConstructor);
        
        // whether type of expression should be known or not, i.e. if at the point where the chain breaks the previous type
        // was already unknown, then this is an IDE error, otherwise probably the user's code is wrong; used for error reporting
        inline bool shouldBeKnown() const {
            return m_shouldBeKnown;
        };
        
        /**
         * @brief Resolve the given declaration if it is an alias declaration.
         *
         * @param decl the declaration to resolve
         * @return :Declaration* decl if not an alias declaration, decl->aliasedDeclaration().data otherwise
         * DUChain must be read locked
         **/
        Declaration* resolveAliasDeclaration(Declaration* decl);
        
        inline KDevelop::AbstractType::Ptr lastType() const {
            return ( m_lastType.isEmpty() ? AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)) : m_lastType.last());
        }
        inline DeclarationPointer lastDeclaration() const {
            if ( m_lastDeclaration.isEmpty() ) {
                return DeclarationPointer(0);
            }
            return m_lastDeclaration.last().last();
        }
        inline QList<DeclarationPointer> lastDeclarations() const {
            if ( m_lastDeclaration.isEmpty() ) {
                return QList<DeclarationPointer>() << DeclarationPointer(0);
            }
            return m_lastDeclaration.last();
        }
        
        template<typename T> static TypePtr<T> typeObjectForIntegralType(QString typeDescriptor, DUContext* ctx);
        
        // used by autocompletion to disable range checks on declaration searches
        bool m_forceGlobalSearching;
        // used by autocompletion to detect unknown NameAst elements in expressions
        bool m_reportUnknownNames;
        CursorInRevision m_scanUntilCursor;
        QList<QString> m_unknownNames;
        
        // this tells the difference between "class foo" and "instance of foo" -- TODO need a better solution!
        bool m_isAlias;
    
    private:
        static QHash<NameConstantAst::NameConstantTypes, KDevelop::AbstractType::Ptr> m_defaultTypes;

        KDevelop::DUContext* m_ctx;
        PythonEditorIntegrator* m_editor;
        
        enum EncounterFlags {
            MergeTypes = 1,
            AutomaticallyDetermineDeclaration = 2
        };
        
        void encounter(AbstractType::Ptr type, EncounterFlags flags = (EncounterFlags) 0);
        AbstractType::Ptr fromBinaryOperator(AbstractType::Ptr lhs, AbstractType::Ptr rhs, const QString& op);
        AbstractType::Ptr encounterPreprocess(AbstractType::Ptr type, bool merge = false);
        template<typename T> void encounter(TypePtr<T> type, EncounterFlags flags = (EncounterFlags) 0);
        void encounterDeclaration(Declaration* ptr, bool isAlias = false);
        void encounterDeclarations(QList<DeclarationPointer> ptrs, bool isAlias = false);
        
        void unknownTypeEncountered();
        AbstractType::Ptr unknownType();
        QList< TypePtr< StructureType > > possibleStructureTypes(AbstractType::Ptr type);
        QList< TypePtr< StructureType > > typeListForDeclarationList(QList< DeclarationPointer > decls);
        
        inline QList< DeclarationPointer > toSharedPtrList(QList< Declaration* > foundDecls) {
            QList<DeclarationPointer> result;
            foreach ( Declaration* d, foundDecls ) {
                result << DeclarationPointer(d);
            }
            return result;
        };
        
        bool m_shouldBeKnown;
        
        QStack<KDevelop::AbstractType::Ptr> m_lastType;
        QStack< QList<DeclarationPointer> > m_lastDeclaration;
        QStack<AbstractType::Ptr> m_callTypeStack;
        QStack<DeclarationPointer> m_callStack;
        
        ExpressionVisitor* m_parentVisitor;
        int m_depth;
};

}

#endif // EXPRESSIONVISITOR_H
