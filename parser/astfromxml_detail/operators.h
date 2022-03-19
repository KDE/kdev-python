/*
 *  SPDX-FileCopyrightText: 2022 Sven Brauch <mail@svenbrauch.de>
 *
 *  SPDX-License-Identifier: LGPL-2.0-or-later
 */

#pragma once

#include "ast.h"

using namespace Python;

Ast::OperatorTypes operatorType(QStringRef const& name) {
    if (name == "Add") return Ast::OperatorAdd;
    if (name == "Sub") return Ast::OperatorSub;
    if (name == "Mult") return Ast::OperatorMult;
    if (name == "MatMult") return Ast::OperatorMatMult;
    if (name == "Div") return Ast::OperatorDiv;
    if (name == "Mod") return Ast::OperatorMod;
    if (name == "Pow") return Ast::OperatorPow;
    if (name == "LeftShift") return Ast::OperatorLeftShift;
    if (name == "RightShift") return Ast::OperatorRightShift;
    if (name == "BitwiseOr") return Ast::OperatorBitwiseOr;
    if (name == "BitwiseXor") return Ast::OperatorBitwiseXor;
    if (name == "BitwiseAnd") return Ast::OperatorBitwiseAnd;
    if (name == "FloorDivision") return Ast::OperatorFloorDivision;

    return Ast::OperatorInvalid;
}

Ast::ComparisonOperatorTypes comparisonOperatorType(QStringRef const& name) {
    return Ast::ComparisonOperatorEquals; // FIXME
}
