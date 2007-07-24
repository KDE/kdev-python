#include <contextbuilder.h>
#include <duchain.h>
#include <duchainlock.h>
#include <parsesession.h>
#include <topducontext.h>

using namespace KDevelop;
using namespace python;
using namespace KTextEditor;

ContextBuilder::ContextBuilder(ParseSession* session, const KUrl &url)
    :m_session(session)
    ,m_url(url)
    ,m_compilingContexts(false)
    ,m_recompiling(false)
{
    kDebug() << "=====Building Contexts for===="<<m_url<<endl;

}

ContextBuilder::~ContextBuilder ()
{
}

TopDUContext* ContextBuilder::buildContexts()
{
    m_compilingContexts = true;
    TopDUContext* topLevelContext = 0;
    {
        DUChainWriteLocker lock(DUChain::lock());
        topLevelContext = DUChain::self()->chainForDocument(m_url);
        if (topLevelContext)
        {
            kDebug() << "ContextBuilder::buildContexts: recompiling" << endl;
            m_recompiling = true;
            Q_ASSERT(topLevelContext->textRangePtr());
        }
        else 
        {
            kDebug() << "ContextBuilder::buildContexts: compiling" << endl;
            m_recompiling = false;
            Q_ASSERT(m_compilingContexts);
        }
    }
}
