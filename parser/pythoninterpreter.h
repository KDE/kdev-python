#ifndef PYTHONINTERPRETER_H
#define PYTHONINTERPRETER_H

#include "parserexport.h"

#include <kross/core/action.h>

#include <QStringList>
#include <QMutex>
#include <QVariant>

namespace Python {

class KDEVPYTHONPARSER_EXPORT PythonInterpreter
{
public:
    static PythonInterpreter* instance()
    {
        static QMutex mutex;
        if (!m_Instance)
        {
            mutex.lock();

            if (!m_Instance) {
                m_Instance = new PythonInterpreter;
                m_Instance->m_isinitialized = false;
                kDebug() << "Initializing interpreter";
                m_Instance->init();
                kDebug() << "Initializing interpreter: Done";
            }

            mutex.unlock();
        }

        return m_Instance;
    }

    static void drop()
    {
        static QMutex mutex;
        mutex.lock();
        delete m_Instance;
        m_Instance = 0;
        mutex.unlock();
    }

    void init();
    QVariant call(const QString& name, const QVariantList& args = QVariantList());
    QVariant evaluate(const QString &expression);

    QStringList getPythonPath();
    void appendToPythonPath(const QString &path);
    QString pydoc(const QString &name);

    QString code();


private:    
    PythonInterpreter() {}

    PythonInterpreter(const PythonInterpreter &); // hide copy constructor
    PythonInterpreter& operator=(const PythonInterpreter &); // hide assign op
                                 // we leave just the declarations, so the compiler will warn us
                                 // if we try to use those two functions by accident

    static PythonInterpreter* m_Instance;
    Kross::Action* m_action;
    Kross::Action* m_util;
    QMutex m_mutex;
    bool m_isinitialized;
};

};
#endif // PYTHONINTERPRETER_H
