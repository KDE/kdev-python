/*
    SPDX-FileCopyrightText: 2010-2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "worker.h"
#include "model.h"
#include "context.h"
#include <language/duchain/declaration.h>
#include <KLocalizedString>
#include "codehelpers.h"
#include <KTextEditor/View>

#include <QDebug>
#include "codecompletiondebug.h"

namespace Python {

PythonCodeCompletionWorker::PythonCodeCompletionWorker(PythonCodeCompletionModel *parent, const QUrl& /*document*/)
    : KDevelop::CodeCompletionWorker(parent), parent(parent)
{

}



KDevelop::CodeCompletionContext* PythonCodeCompletionWorker::createCompletionContext(const KDevelop::DUContextPointer& context,
                                                                                     const QString& contextText,
                                                                                     const QString& followingText,
                                                                                     const KDevelop::CursorInRevision& position) const
{
    if ( !context ) {
        return nullptr;
    }
    PythonCodeCompletionContext* completionContext = new PythonCodeCompletionContext(
        context, contextText, followingText, position, 0, this
    );
    return completionContext;
}

void PythonCodeCompletionWorker::updateContextRange(KTextEditor::Range &contextRange, KTextEditor::View *view,
                                                    const KDevelop::DUContextPointer& context) const
{
    if ( ! context ) {
        return;
    }
    if ( ! contextRange.start().isValid() ) {
        contextRange.setStart({0, 0});
    }
    if ( CodeHelpers::endsInside(view->document()->text(contextRange)) == CodeHelpers::String ) {
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "we're dealing with string completion. extend the range";
        contextRange = context->rangeInCurrentRevision();
    }
}


}
