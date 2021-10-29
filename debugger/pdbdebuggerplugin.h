/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PDBDEBUGGERPLUGIN_H
#define PDBDEBUGGERPLUGIN_H

#include <interfaces/iplugin.h>
#include "kdevpdb_export.h"
#include <QVariantList>

namespace Python {

class PdbDebuggerPlugin : public KDevelop::IPlugin
{
Q_OBJECT
public:
    PdbDebuggerPlugin(QObject* parent, const QVariantList& = QVariantList());
    ~PdbDebuggerPlugin() override;
};

}

#endif // PDBDEBUGGERPLUGIN_H
