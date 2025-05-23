/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "pdblauncher.h"
#include <interfaces/idocumentcontroller.h>
#include "debugjob.h"

#include <executescript/iexecutescriptplugin.h>
#include <interfaces/launchconfigurationpage.h>
#include <interfaces/ilaunchconfiguration.h>
#include <interfaces/iplugincontroller.h>
#include <interfaces/icore.h>
#include <interfaces/iuicontroller.h>

#include <KLocalizedString>
#include <KMessageBox>
#include <KParts/MainWindow>
#include <KConfigGroup>
#include <QFileInfo>

#include <QDebug>
#include "debuggerdebug.h"
#include <util/environmentprofilelist.h>


namespace Python {
    
PdbLauncher::PdbLauncher()
{

}

QList< KDevelop::LaunchConfigurationPageFactory* > PdbLauncher::configPages() const
{
    return QList<KDevelop::LaunchConfigurationPageFactory*>();
}

QString PdbLauncher::description() const
{
    return i18n("A plugin to debug Python applications with pdb.");
}

QString PdbLauncher::id()
{
    return QStringLiteral("pdbdebugger");
}

QString PdbLauncher::name() const
{
    return QStringLiteral("pdbdebugger");
}

KJob* PdbLauncher::start(const QString& launchMode, KDevelop::ILaunchConfiguration* cfg)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "start of debugger process requested";
    if ( launchMode == QStringLiteral("debug") ) {
        IExecuteScriptPlugin* iface = KDevelop::ICore::self()->pluginController()
                                      ->pluginForExtension(QStringLiteral("org.kdevelop.IExecuteScriptPlugin"))->extension<IExecuteScriptPlugin>();
        Q_ASSERT(iface);
        QString err;

        const auto interpreter = iface->interpreter(cfg, err);
        // TODO: replace this minimal safety check with proper ILaunchConfiguration
        //       error handling like that in ScriptAppJob from the executescript plugin
        if (interpreter.empty()) {
            return nullptr;
        }

        // check the interpreter
        QProcess p;
        p.setProcessChannelMode(QProcess::MergedChannels);
        // Do not pass the interpreter command line arguments to the interpreter version check command,
        // because the arguments are more likely to break the check than to improve version detection accuracy.
        p.start(interpreter.constFirst(), {QStringLiteral("--version")});
        p.waitForFinished(500);
        QByteArray version = p.readAll();
        qCDebug(KDEV_PYTHON_DEBUGGER) << "interpreter version:" << version;
        if ( ! version.startsWith("Python 3.") ) {
            KMessageBox::error(ICore::self()->uiController()->activeMainWindow(),
                            i18n("Sorry, debugging is only supported for Python 3.x applications."),
                            i18n("Unsupported interpreter"));
            return nullptr;
        }

        QUrl scriptUrl;
        if ( iface->runCurrentFile(cfg) ) {
            auto document = KDevelop::ICore::self()->documentController()->activeDocument();
            if ( ! document ) {
                qCDebug(KDEV_PYTHON_DEBUGGER) << "no current document";
                return nullptr;
            }
            scriptUrl = document->url();
        }
        else {
            scriptUrl = iface->script(cfg, err);
        }
        const auto scriptPath = scriptUrl.toLocalFile();

        auto wd = iface->workingDirectory(cfg);
        if( !wd.isValid() || wd.isEmpty() )
        {
            wd = QUrl::fromLocalFile(QFileInfo{scriptPath}.absolutePath());
        }

        DebugJob* job = new DebugJob();
        const auto scriptFileName = scriptPath.sliced(scriptPath.lastIndexOf(QLatin1Char{'/'}) + 1);
        job->setObjectName(scriptFileName);
        job->m_scriptPath = scriptPath;
        job->m_interpreter = interpreter;
        job->m_args = iface->arguments(cfg, err);
        job->m_workingDirectory = wd;

        const KDevelop::EnvironmentProfileList environmentProfiles(KSharedConfig::openConfig());
        QString envProfileName = iface->environmentProfileName(cfg);

        if (envProfileName.isEmpty()) {
            qCWarning(KDEV_PYTHON_DEBUGGER) << "No environment profile specified, looks like a broken "
                                       "configuration, please check run configuration " << cfg->name() <<
                                       ". Using default environment profile.";
            envProfileName = environmentProfiles.defaultProfileName();
        }
        job->m_envProfileName = envProfileName;

        return job;
    }
    qCDebug(KDEV_PYTHON_DEBUGGER) << "unknown launch mode";
    return nullptr;
}

QStringList PdbLauncher::supportedModes() const
{
    return QStringList() << QStringLiteral("debug");
}

}
