#ifndef KDEVPYTHONLANGUAGESUPPORT_H
#define KDEVPYTHONLANGUAGESUPPORT_H

#include <iplugin.h>
#include <ilanguagesupport.h>

namespace KDevelop
{
    class IDocument;
}

class PythonLanguageSupport : public KDevelop::IPlugin, public KDevelop::ILanguageSupport
{
Q_OBJECT
Q_INTERFACES( KDevelop::ILanguageSupport )
public:
    PythonLanguageSupport( QObject *parent, const QStringList& args = QStringList() );
    virtual ~PythonLanguageSupport();
    virtual QString name() const;
    /*Name Of the Language*/
    virtual KDevelop::ParseJob *createParseJob(const KUrl &url);
    /*Parsejob used by background parser to parse given Url*/
    virtual KDevelop::ILanguage *language();
    /*The Language*/
private slots:
    void documentChanged( KDevelop::IDocument*);
};

#endif
