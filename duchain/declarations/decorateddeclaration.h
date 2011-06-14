/**
    This file is part of KDevelop
    Copyright (C) 2011  Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
**/


#ifndef DECORATEDDECLARATION_H
#define DECORATEDDECLARATION_H

#include "ast.h"
#include <QVariant>
#include <language/duchain/functiondeclaration.h>
#include <language/duchain/classdeclaration.h>

namespace Python {

class Decorator {
public:
    Identifier name;
    QList<QVariant> args;
};

class DecoratedDeclaration {
public:
    QList<Decorator> decorators;
};

class PythonFunctionDeclaration : public KDevelop::FunctionDeclaration, public DecoratedDeclaration {
    
};

class PythonClassDeclaration : public KDevelop::ClassDeclaration, public DecoratedDeclaration {

};

typedef PythonFunctionDeclaration FunctionDeclaration;
typedef PythonClassDeclaration ClassDeclaration;

#endif // DECORATEDDECLARATION_H
