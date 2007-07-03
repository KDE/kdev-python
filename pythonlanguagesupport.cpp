#include "pythonlanguagesupport.h"

#include <kdebug.h>
#include <kcomponentdata.h>
#include <kstandarddirs.h>
#include <kgenericfactory.h>
#include <icore.h>
#include <QExtensionFactory>
#include <ilanguagecontroller.h>
#include <ilanguage.h>
#include <idocument.h>
#include <backgroundparser.h>
#include <idocumentcontroller.h>
#include <QExtensionFactory>

typedef KGenericFactory<PythonLanguageSupport> KDevPythonSupportFactory;
K_EXPORT_COMPONENT_FACTORY( kdevpythonlanguagesupport, KDevPythonSupportFactory( "kdevpythonsupport" ) )

PythonLanguageSupport::PythonLanguageSupport( QObject* parent, const QStringList& /*args*/ )
        : KDevelop::IPlugin( KDevPythonSupportFactory::componentData(), parent ),
        KDevelop::ILanguageSupport()
{
    KDEV_USE_EXTENSION_INTERFACE( KDevelop::ILanguageSupport )
    connect( core()->documentController(),
             SIGNAL( documentStateChanged( KDevelop::IDocument* ) ),
             this, SLOT( documentChanged( KDevelop::IDocument* ) ) );
    connect( core()->documentController(),
             SIGNAL( documentContentChanged( KDevelop::IDocument* ) ),
             this, SLOT( documentChanged( KDevelop::IDocument* ) ) );
    connect( core()->documentController(),
             SIGNAL( documentActivated( KDevelop::IDocument* ) ),
             this, SLOT( documentChanged( KDevelop::IDocument* ) ) );
}

void PythonLanguageSupport::documentChanged( KDevelop::IDocument* doc )
{
        kDebug() << "-------------Adding document to parser--------------" << endl;
        language()->backgroundParser()->addDocument(doc->url());
}
PythonLanguageSupport::~PythonLanguageSupport()
{
}

KDevelop::ParseJob *PythonLanguageSupport::createParseJob(const KUrl &url)
{
    kDebug() << ">>>>>>>>>Parsing<<<<<<<<<"
             << url
             << endl;
    return 0;
}

QString PythonLanguageSupport::name() const
{
    return "Python";
}

KDevelop::ILanguage *PythonLanguageSupport::language()
{
    return core()->languageController()->language(name());
}
#include "pythonlanguagesupport.moc"
