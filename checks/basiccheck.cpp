/*****************************************************************************
 * Copyright (c) 2014 Sven Brauch <svenbrauch@gmail.com>                     *
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

#include "basiccheck.h"
#include <language/duchain/duchainlock.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/declaration.h>
#include <language/duchain/use.h>
#include <language/duchain/problem.h>
#include <language/checks/controlflowgraph.h>
#include <language/checks/controlflownode.h>
#include <language/checks/dataaccessrepository.h>

using namespace KDevelop;

QString BasicCheck::name() const
{
    return "test check";
}

class UnusedResultChecker {
public:
    struct Data {
        Data() = default;
        Data(const Data&) = default;
        QMap<Declaration*, RangeInRevision> lastWrite;
        QSet<Declaration*> currentlyUnused;
    };

    struct Error {
        Declaration* decl;
        RangeInRevision range;
    };

    UnusedResultChecker(ControlFlowNode* root, DataAccessRepository* access, const ReferencedTopDUContext& top)
        : node(root), top(top), access(access)
    { }

    QVector<Error> run() {
        auto context = top->findContextAt(node->nodeRange().start);
        auto decls = context->localDeclarations();
        auto errors = QVector<Error>();
        while ( node && node->next() ) {
            auto alternative = node->alternative();
            node = node->next();

            auto runOnCurrentNode = [&]() {
                auto accesses = access->accessesInRange(node->nodeRange());
                for ( const auto& access: accesses ) {
                    // check all data accesses in the compound
                    auto pos = access->pos();
                    auto use = context->findUseAt(pos);
                    Declaration* usedDeclaration = nullptr;
                    if ( use != -1 ) {
                        usedDeclaration = context->uses()[use].usedDeclaration(top.data());
                    }
                    if ( ! usedDeclaration ) {
                        usedDeclaration = context->findDeclarationAt(pos);
                    }
                    if ( ! usedDeclaration ) {
                        continue;
                    }
                    if ( access->isWrite() ) {
                        auto end = pos + CursorInRevision(0, usedDeclaration->identifier().toString().length());
                        auto range = RangeInRevision(pos, end);
                        d.lastWrite[usedDeclaration] = range;

                        if ( d.currentlyUnused.contains(usedDeclaration) ) {
                            // write before reading result -> error
                            errors << Error{usedDeclaration, range};
                        }
                        else {
                            d.currentlyUnused.insert(usedDeclaration);
                        }
                    }
                    if ( access->isRead() || access->isCall() ) {
                        d.currentlyUnused.remove(usedDeclaration);
                    }
                }
            };

            auto initialState = state();
            runOnCurrentNode();
            // handle the else, if it exists
            if ( alternative ) {
                auto state_after_if = state();

                node = alternative;
                setState(initialState);
                runOnCurrentNode();
                auto state_after_else = state();

                // merge the two end states
                d.currentlyUnused = state_after_if.currentlyUnused.unite(state_after_else.currentlyUnused);
            }
        }

        // unused at end
        for ( const auto& unused: d.currentlyUnused ) {
            errors << Error{unused, d.lastWrite[unused]};
        }

        return errors;
    }

    Data state() const {
        return Data(d);
    }
    void setState(const Data& state) {
        d = state;
    }

private:
    Data d;
    const ControlFlowNode* node;
    ReferencedTopDUContext top;
    DataAccessRepository* access;
};

void BasicCheck::runCheck(const KDevelop::CheckData& data)
{
    DUChainWriteLocker lock;
    for ( auto root: data.flow->rootNodes() ) {
        auto checker = UnusedResultChecker(root, data.access, data.top);
        auto errors = checker.run();

        for ( const auto& error: errors ) {
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(IndexedString(data.url), error.range.castToSimpleRange()));
            p->setSource(KDevelop::ProblemData::SemanticAnalysis);
            p->setSeverity(KDevelop::ProblemData::Hint);
            p->setDescription(i18n("Unused computation result"));
            ProblemPointer ptr(p);
            data.top->addProblem(ptr);
        }
    }
}
