#include "pythonparsejob.h"
#include <kdebug.h>
#include "Thread.h"
#include "pythonlanguagesupport.h"
#include <parsejob.h>

PythonParseJob::PythonParseJob( const KUrl &url,PythonLanguageSupport *parent)
            : KDevelop::ParseJob( url, parent )
{
    kDebug() << "########Parsing ########"
             << url
             << endl;
}

PythonParseJob::~PythonParseJob()
{}

PythonLanguageSupport *PythonParseJob::python() const
{
    return qobject_cast<PythonLanguageSupport*>(const_cast<QObject*>(parent()));
}
#include "pythonparsejob.moc"

