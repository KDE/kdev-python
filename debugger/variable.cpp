/*
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012  <copyright holder> <email>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
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

namespace Python {

Variable::Variable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display):
    KDevelop::Variable(model, parent, expression, display)
{

}

void Variable::dataFetched(QByteArray rawData)
{
    QList<QByteArray> data = rawData.split('\n');
    data.removeLast();
    QByteArray value;
    foreach ( const QByteArray item, data ) {
        value.append(item);
    }
    setValue(value);
    setHasMore(true);
    kDebug() << "value set to" << value << ", calling update method";
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
    QString formatObject = "'\\n'.join(['.%s => %s' % (i, str(getattr("+expression()+", i)).replace('\\n', r'\\n')) for i in dir("+expression()+")])";
    QString formatDict = "'\\n'.join(['[%s] => %s' % (str(k).replace('\\n', r'\\n'), str(v).replace('\\n', r'\\n')) for k, v in "+expression()+".iteritems()])";
    QString formatOtherIterable = "'\\n'.join(['[%s] => %s' % (i, str("+expression()+"[i]).replace('\\n', r'\\n')) for i in range(len("+expression()+"))])";
    QString isDict = "type("+expression()+") == dict";
    QString isOtherIterable = "hasattr("+expression()+", '__getitem__')";
    QString fetchChildren = "print ( '\\n'.join("+expression()+"[0:10]) if hasattr("+expression()+",'__getitem__') else  )";
    QString cmd = "print (" + formatDict + " if " + isDict + " else " + formatOtherIterable + " if " + isOtherIterable + " else " + formatObject + ")\n";
    InternalPdbCommand* fetchChildrenScript = new InternalPdbCommand(this, "moreChildrenFetched", cmd);
    static_cast<DebugSession*>(ICore::self()->debugController()->currentSession())->addCommand(fetchChildrenScript);
}

void Variable::moreChildrenFetched(QByteArray rawData)
{
    QList<QByteArray> data = rawData.split('\n');
    data.removeLast();
    int i = 0;
    int initialLength = data.length();
    QRegExp formatExtract("([\\[\\]\\.a-zA-Z0-9_]+) \\=\\> (.*)");
    while ( i < data.length() ) {
        QByteArray d = data.at(i);
        // sort magic functions at the end of the list, they're not too interesting usually
        if ( d.startsWith('_') and i < initialLength ) {
            data.append(d);
            i++;
            continue;
        }
        QString childName = expression() + "_" + QString::number(i);
        QString realValue = QString::null;
        if ( formatExtract.exactMatch(d) ) {
            childName = expression() + formatExtract.capturedTexts().at(1);
            realValue = formatExtract.capturedTexts().at(2);
        }
        Variable* v = new Variable(model_, this, childName);
        v->setValue(! realValue.isNull() ? realValue : d);
        kDebug() << "adding child:" << expression() << i << d;
        v->setHasMoreInitial(true);
        appendChild(v);
        i++;
    }
}

}

