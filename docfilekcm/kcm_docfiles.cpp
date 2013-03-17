/************************************************************************
 * KDevelop4 Python Language Support                                    *
 * Copyright 2013 Sven Brauch <svenbrauch@gmail.com>                    *
 *                                                                      *
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

#include "kcm_docfiles.h"

#include <QLabel>
#include <QLayout>
#include <QBoxLayout>
#include <QDebug>

#include <KPluginFactory>

#include "docfilemanagerwidget.h"

K_PLUGIN_FACTORY(DocfilesKCModuleFactory, registerPlugin<DocfilesKCModule>(); )
K_EXPORT_PLUGIN(DocfilesKCModuleFactory("kcm_docfiles", "kdevpythonsupport"))

DocfilesKCModule::DocfilesKCModule(QWidget* parent, const QVariantList& args)
    : KCModule(DocfilesKCModuleFactory::componentData(), parent, args)
{
   managerWidget = new DocfileManagerWidget(parent);
   parent->layout()->addWidget(managerWidget);
}

DocfilesKCModule::~DocfilesKCModule()
{

}

