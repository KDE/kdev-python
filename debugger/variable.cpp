/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#include "variable.h"
#include "debugsession.h"
#include <interfaces/icore.h>

#include <QDebug>
#include "debuggerdebug.h"

namespace Python {

Variable::Variable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display):
    KDevelop::Variable(model, parent, expression, display), m_pythonPtr(0)
{

}

void Variable::dataFetched(QByteArray rawData)
{
    QList<QByteArray> data = rawData.split('\n');
    data.removeLast();
    QByteArray value;
    foreach ( const QByteArray& item, data ) {
        value.append(item);
    }
    setValue(value);
    setHasMore(true);
    qCDebug(KDEV_PYTHON_DEBUGGER) << "value set to" << value << ", calling update method";
    QMetaObject::invokeMethod(m_notifyCreated, m_notifyCreatedMethod, Qt::QueuedConnection, Q_ARG(bool, true));
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
        cmd = "__kdevpython_debugger_utils.format_ptr_children("+QString::number(m_pythonPtr)+")\n";
    }
    else {
        cmd = "__kdevpython_debugger_utils.format_object_children("+expression()+")\n";
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
    QList<QByteArray> data = rawData.split('\n');
    data.removeLast();
    int i = 0;
    int initialLength = data.length();
    QRegExp formatExtract("(ptr:<(\\d*)>\\s)?([\\[\\]\\.a-zA-Z0-9_]+) \\=\\> (.*)$");
    formatExtract.setPatternSyntax(QRegExp::RegExp2);
    formatExtract.setMinimal(true);
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
        if ( formatExtract.exactMatch(d) ) {
            QString id = formatExtract.capturedTexts().at(2);
            if ( ! id.isEmpty() ) {
                pythonId = id.toLong();
            }
            childName = expression() + formatExtract.capturedTexts().at(3);
            prettyName = formatExtract.capturedTexts().at(3);
            realValue = formatExtract.capturedTexts().at(4);
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

