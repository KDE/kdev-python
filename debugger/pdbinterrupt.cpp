/*
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

/**
 * Implement platform specific void interruptProcess(KProcess * process)
 * required to interrupt a long running debugger command.
 */
#include <KProcess>

#ifdef Q_OS_WIN
#include <windows.h>
namespace Python {
void interruptProcess(KProcess* process)
{
    GenerateConsoleCtrlEvent(CTRL_C_EVENT, process->processId());
}
}
#else
#include <signal.h>
namespace Python {
void interruptProcess(KProcess* process)
{
    kill(process->processId(), SIGINT);
}
}

#endif
