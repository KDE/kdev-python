/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef KCM_PEP8_H
#define KCM_PEP8_H
#include <KConfigGroup>
#include <QUrl>
#include <QLineEdit>
#include <QCheckBox>

#include <KPluginFactory>

#include <interfaces/configpage.h>

#include "ui_pep8.h"

class PEP8KCModule : public KDevelop::ConfigPage
{
Q_OBJECT
public:
    PEP8KCModule(KDevelop::IPlugin* plugin, QWidget* parent = nullptr);
    ~PEP8KCModule() override;

    KDevelop::ConfigPage::ConfigPageType configPageType() const override;

    QString name() const override;
    QString fullName() const override;
    QIcon icon() const override;


    // TODO: use KConfigXT instead (this will additionally allow removing apply/reset/defaults)
    static bool isPep8Enabled(const KConfigGroup& group);

    void apply() override;
    void reset() override;
    void defaults() override;
private:
    KConfigGroup configGroup;
    Ui_pep8 m_ui;
};

#endif
