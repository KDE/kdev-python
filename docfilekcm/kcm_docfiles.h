/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PY_KCM_DOCFILES_H
#define PY_KCM_DOCFILES_H

#include <interfaces/configpage.h>

class DocfileManagerWidget;

class DocfilesKCModule : public KDevelop::ConfigPage
{
Q_OBJECT
public:
    DocfilesKCModule(KDevelop::IPlugin* plugin, QWidget* parent);
    ~DocfilesKCModule() override;

    KDevelop::ConfigPage::ConfigPageType configPageType() const override;

    QString name() const override;
    QString fullName() const override;
    QIcon icon() const override;

    void apply() override;
    void reset() override;
    void defaults() override;

private:
    DocfileManagerWidget* managerWidget;
    QString knsrc;
};

#endif
