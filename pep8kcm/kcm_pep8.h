/************************************************************************
 * KDevelop4 Python Language Support                                    *
 *                                                                      *
 * Copyright 2013 Sven Brauch <svenbrauch@gmail.com>                    *
 *                                                                      *
 * This program is free software; you can redistribute it and/or modify *
 * it under the terms of the GNU General Public License as published by *
 * the Free Software Foundation; either version 2 or version 3 of the   *
 * License, or (at your option) any later version.                      *
 *                                                                      *
 * This program is distributed in the hope that it will be useful, but  *
 * WITHOUT ANY WARRANTY; without even the implied warranty of           *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU     *
 * General Public License for more details.                             *
 *                                                                      *
 * You should have received a copy of the GNU General Public License    *
 * along with this program; if not, see <http://www.gnu.org/licenses/>. *
 ************************************************************************/

#ifndef KCM_PEP8_H
#define KCM_PEP8_H
#include <KCModule>
#include <KConfigGroup>
#include <QUrl>
#include <QLineEdit>
#include <QCheckBox>

#include <KPluginFactory>

#include <interfaces/configpage.h>

class PEP8KCModule : public KDevelop::ConfigPage
{
Q_OBJECT
public:
    PEP8KCModule(KDevelop::IPlugin* plugin, QWidget* parent = nullptr);
    ~PEP8KCModule() override;

    QString name() const override;
    QString fullName() const override;
    QIcon icon() const override;


    // TODO: use KConfigXT instead (this will additionally allow removing apply/reset/defaults)
    static QString pep8Path(const KConfigGroup& group);
    static bool isPep8Enabled(const KConfigGroup& group);
    static QString pep8Arguments(const KConfigGroup& group);

    void apply() override;
    void reset() override;
    void defaults() override;
private:
    KConfigGroup configGroup;
    QLineEdit* pep8url;
    QLineEdit* pep8arguments;
    QCheckBox* enableChecking;
};

#endif
