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
    QList<QByteArray> data = rawData.split('\n');
    data.removeLast();
    QByteArray value;
    for ( const QByteArray& item : data ) {
        value.append(item);
    }
    setValue(QString::fromLatin1(value));
    setHasMore(true);
    qCDebug(KDEV_PYTHON_DEBUGGER) << "value set to" << value << ", calling update method";
    if ( m_notifyCreated ) {
        QMetaObject::invokeMethod(m_notifyCreated, m_notifyCreatedMethod, Qt::QueuedConnection, Q_ARG(bool, true));
        m_notifyCreated = nullptr;
    }
}

void Variable::attachMaybe(QObject* callback, const char* callbackMethod)
{
    IDebugSession* is = ICore::self()->debugController()->currentSession();
    DebugSession* s = static_cast<DebugSession*>(is);
    s->createVariable(this, callback, callbackMethod);
}

// TODO: make it really fetch *more*, not just some
void Variable::fetchMoreChildren()
{
    QString cmd;
    if ( m_pythonPtr ) {
        cmd = QStringLiteral("__kdevpython_debugger_utils.format_ptr_children(") + QString::number(m_pythonPtr) + QStringLiteral(")\n");
    }
    else {
        cmd = QStringLiteral("__kdevpython_debugger_utils.format_object_children(") + expression() + QStringLiteral(")\n");
    }
    InternalPdbCommand* fetchChildrenScript = new InternalPdbCommand(this, "moreChildrenFetched", cmd);
    static_cast<DebugSession*>(ICore::self()->debugController()->currentSession())->addCommand(fetchChildrenScript);
}

void Variable::setId(unsigned long int id)
{
    m_pythonPtr = id;
}

void Variable::moreChildrenFetched(QByteArray rawData)
{
    deleteChildren();

    QList<QByteArray> data = rawData.split('\n');
    data.removeLast();
    int i = 0;
    int initialLength = data.length();
    QRegularExpression formatExtract(QStringLiteral("(ptr:<(\\d*)>\\s)?([\\[\\]\\.a-zA-Z0-9_]+) \\=\\> (.*)$"),
                                     QRegularExpression::InvertedGreedinessOption);
    while ( i < data.length() ) {
        QByteArray d = data.at(i);
        // sort magic functions at the end of the list, they're not too interesting usually
        if ( d.startsWith('_') && i < initialLength ) {
            data.append(d);
            i++;
            continue;
        }

        QString childName;
        QString realValue;
        QString prettyName;
        unsigned long int pythonId = 0;
        auto match = formatExtract.match(QString::fromLatin1(d));
        if ( match.hasMatch() ) {
            QString id = match.captured(2);
            if ( ! id.isEmpty() ) {
                pythonId = id.toLong();
            }
            childName = expression() + match.captured(3);
            prettyName = match.captured(3);
            realValue = match.captured(4);
        }
        else {
            i++;
            continue;
        }
        Variable* v = new Variable(model_, this, childName, prettyName);
        appendChild(v);
        qCDebug(KDEV_PYTHON_DEBUGGER) << "adding child:" << expression() << i << d;
        v->setValue(realValue);
        v->setId(pythonId);
        v->setHasMoreInitial(true);
        i++;
    }
}

}

#include "moc_variable.cpp"
