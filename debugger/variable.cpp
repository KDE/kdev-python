/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "variable.h"
#include "debugsession.h"
#include <interfaces/icore.h>

#include <QDebug>
#include <QRegularExpression>
#include "debuggerdebug.h"

namespace Python {

Variable::Variable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display)
    : KDevelop::Variable(model, parent, expression, display)
    , m_notifyCreated(nullptr)
    , m_pythonPtr(0)
{

}

void Variable::dataFetched(QByteArray rawData)
{
    // TODO
}

void Variable::attachMaybe(QObject* callback, const char* callbackMethod)
{
    IDebugSession* is = ICore::self()->debugController()->currentSession();
    DebugSession* s = static_cast<DebugSession*>(is);
    // TODO
}

// TODO: make it really fetch *more*, not just some
void Variable::fetchMoreChildren()
{
    // TODO
}

void Variable::setId(unsigned long int id)
{
    m_pythonPtr = id;
}

void Variable::moreChildrenFetched(QByteArray rawData)
{
    deleteChildren();
    // TODO
}

}

#include "moc_variable.cpp"
