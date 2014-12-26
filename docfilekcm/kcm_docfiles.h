/************************************************************************
 * KDevelop4 Python Language Support                                    *
 *                                                                      *
 * Copyright 2013 Sven Brauch <svenbrauch@gmail.com>                    *
 *                                                                      *
 * This program is free software; you can redistribute it and/or modify *
 * it under the terms of the GNU General Public License as published by *
 * the Free Software Foundation; either version 2 or version 3 of the License, or    *
 * (at your option) any later version.                                  *
 *                                                                      *
 * This program is distributed in the hope that it will be useful, but  *
 * WITHOUT ANY WARRANTY; without even the implied warranty of           *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU     *
 * General Public License for more details.                             *
 *                                                                      *
 * You should have received a copy of the GNU General Public License    *
 * along with this program; if not, see <http://www.gnu.org/licenses/>. *
 ************************************************************************/

#ifndef KCM_PY_DOCFILES_H
#define KCM_PY_DOCFILES_H
#include <KCModule>
#include <QUrl>

#include <KPluginFactory>

class DocfileManagerWidget;

class DocfilesKCModule : public KCModule
{
Q_OBJECT
public:
    DocfilesKCModule( QWidget* parent, const QVariantList& args = QVariantList() );
    virtual ~DocfilesKCModule();

private:
    DocfileManagerWidget* managerWidget;
    QString knsrc;
};

#endif
