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
#include <language/duchain/duchainpointer.h>

namespace Python {

class Decorator {
public:
    Decorator() : name("<none set>") {
        
    };
    Identifier name;
    QList<QVariant> args;
};

class DecoratedDeclaration {
public:
    QList<Decorator> decorators;
    inline const Decorator* findDecoratorByName(const QString& name) const {
        foreach ( const Decorator& d, decorators ) {
            if ( d.name == name )
                return &d;
        }
        return 0;
    }
};

class PythonFunctionDeclaration : public KDevelop::FunctionDeclaration, public DecoratedDeclaration {
public:
    PythonFunctionDeclaration(const KDevelop::RangeInRevision& range, KDevelop::DUContext* context);
    PythonFunctionDeclaration(const FunctionDeclaration& rhs);
    PythonFunctionDeclaration(KDevelop::FunctionDeclarationData& data);
    PythonFunctionDeclaration(KDevelop::FunctionDeclarationData& data, const KDevelop::RangeInRevision& );
};

class PythonClassDeclaration : public KDevelop::ClassDeclaration, public DecoratedDeclaration {
public:
    PythonClassDeclaration(const KDevelop::RangeInRevision& range, KDevelop::DUContext* context);
    PythonClassDeclaration(const ClassDeclaration& rhs);
    PythonClassDeclaration(KDevelop::ClassDeclarationData& data);
    PythonClassDeclaration(KDevelop::ClassDeclarationData& data, const KDevelop::RangeInRevision& range, KDevelop::DUContext* context);
};

typedef PythonFunctionDeclaration FunctionDeclaration;
typedef PythonClassDeclaration ClassDeclaration;
typedef KDevelop::DUChainPointer<PythonFunctionDeclaration> FunctionDeclarationPointer;

}

#endif // DECORATEDDECLARATION_H
