#include <contextbuilder.h>
#include <duchain.h>
#include <duchainlock.h>
#include <parsesession.h>

using namespace KDevelop;
using namespace python;

ContextBuilder::ContextBuilder(ParseSession* session)
    :m_session(session)
{
    kDebug() << "=====Building Contexts===="<<endl;

}

ContextBuilder::~ContextBuilder ()
{
}

TopDUContext* ContextBuilder::buildContexts()
{
    
}
