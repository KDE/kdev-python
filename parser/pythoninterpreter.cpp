#include <KDebug>

#include "pythoninterpreter.h"
#include "pythoncode.h"

namespace Python {

PythonInterpreter* PythonInterpreter::m_Instance = 0;

void PythonInterpreter::init()
{
  m_action = new Kross::Action(0, "action");
  m_action->setInterpreter("python");

  m_util = new Kross::Action(0, "kdevutil");
  m_util->setInterpreter("python");
  m_util->setCode(KDEVUTIL);
  m_util->trigger();
}

QStringList PythonInterpreter::getPythonPath()
{
  return m_util->callFunction("get_python_path").toStringList();
}

void PythonInterpreter::appendToPythonPath(const QString& path)
{
  QVariantList args;
  args << path;
  m_util->callFunction("append_to_python_path", args);
}

QVariant PythonInterpreter::call(const QString &name, const QVariantList &args)
{
  return m_action->callFunction(name, args);
}

QVariant PythonInterpreter::evaluate(const QString &expression)
{
  return m_action->evaluate(expression.toLatin1().data());
}

QString Python::PythonInterpreter::pydoc(const QString &name)
{
  QVariantList args;
  args << name;
  return m_util->callFunction("getdoc", args).toString();
}

QString PythonInterpreter::code() {
  return m_util->code();
}

}
