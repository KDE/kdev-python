#ifndef PARSEJOB_H
#define PARSEJOB_H

#include <parsejob.h>

class PythonLanguageSupport;

class PythonParseJob : public KDevelop::ParseJob
{
    Q_OBJECT
public:
    PythonParseJob( const KUrl &url, PythonLanguageSupport* parent);
    virtual ~PythonParseJob();
    PythonLanguageSupport* python() const;
};
#endif

