/*****************************************************************************
 * This file is part of KDevelop
 * Copyright (c) 2011-2012 Sven Brauch <svenbrauch@googlemail.com>           *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *           
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *   
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */


#ifndef PYCOMPLETIONHELPERS_H
#define PYCOMPLETIONHELPERS_H

#include <language/duchain/declaration.h>

#include <QString>
#include <QList>
#include <QVariant>

#include "pythoncompletionexport.h"

using namespace KDevelop;

namespace Python {

void createArgumentList(Declaration* dec, QString& ret, QList<QVariant>* highlighting,
                        int atArg = 0, bool includeTypes = true);

// export needed for unit tests
KDEVPYTHONCOMPLETION_EXPORT int identifierMatchQuality(const QString& identifier1_, const QString& identifier2_);
KDEVPYTHONCOMPLETION_EXPORT QString camelCaseToUnderscore(const QString& camelCase);

class TokenList;

class KDEVPYTHONCOMPLETION_EXPORT ExpressionParser {
public:
    ExpressionParser(QString code);
    
    enum Status {
        InvalidStatus,
        NothingFound,
        ExpressionFound,
        CommaFound,
        EventualCallFound,
        InitializerFound,
        FromFound,
        MemberAccessFound,
        ImportFound,
        GeneratorFound,
        RaiseFound,
        ForFound,
        ExceptFound,
        ColonFound,
        InFound,
        ClassFound,
        DefFound,
        EqualsFound,
        MeaninglessKeywordFound, // "and", "if", "return", ...
        NoCompletionKeywordFound // "for"
    };
    
    QString popExpression(Status* status);
    QString getRemainingCode();
    QString getScannedCode();
    QString skipUntilStatus(Status requestedStatus, bool* ok, int* expressionsSkipped = nullptr);
    TokenList popAll();
    void reset();
    int trailingWhitespace();
    
private:
    QString m_code;
    int m_cursorPositionInString;
};

struct TokenListEntry {
public:
    TokenListEntry(ExpressionParser::Status status_, QString expression_, int charOffset_)
    : status(status_)
    , expression(expression_)
    , charOffset(charOffset_) {};
    ExpressionParser::Status status;
    QString expression;
    int charOffset;
};

class TokenList : public QList<TokenListEntry> {
public:
    /**
     * @brief Reset the internal pointer to the last item, or offsetAtEnd items before
     **/
    void reset(int offsetAtEnd = 0) {
        m_internalPtr = length() - offsetAtEnd;
    };
    /**
     * @brief Set the internal pointer to "index".
     **/
    void seek(int index) {
        m_internalPtr = index;
    };
    /**
     * @brief Get the last item and advance the internal pointer.
     *
     * @return :TokenListEntry the item if the internal pointer is valid, an invalid item otherwise
     **/
    TokenListEntry weakPop() {
        m_internalPtr --;
        if ( m_internalPtr < 0 ) {
            return TokenListEntry(ExpressionParser::InvalidStatus, QString::null, -1);
        }
        return at(m_internalPtr);
    };
    // First returned value is the *expression count* index, the second one is the *character count*.
    // The expressions count from the right, the characters count from the left.
    // (see PythonCodeCompletionContext::summonParentForEventualCall for an example why that makes sense)
    QPair<int, int> nextIndexOfStatus(ExpressionParser::Status status, int offsetFromEnd = 0) const {
        int currentIndex = length() - 1 - offsetFromEnd;
        while ( currentIndex >= 0 ) {
            if ( at(currentIndex).status == status ) {
                return QPair<int, int>(length() - currentIndex, at(currentIndex).charOffset);
            }
            currentIndex -= 1;
        }
        return QPair<int, int>(-1, -1);
    };
    
    QString toString() {
        QString ret;
        int pos = 0;
        foreach ( TokenListEntry item, *this ) {
            ret.append(
                "offset " + QString::number(item.charOffset) + 
                " position " + QString::number(pos) +
                ": status " + QString::number(item.status) +
                ", expression " + item.expression + "\n"
            );
            pos ++;
        }
        return ret;
    };
private:
    int m_internalPtr;
};

class ReplacementVariable;

struct RangeInString {
    RangeInString() : beginIndex(-1), endIndex(-1) {}
    RangeInString(int beginIndex_, int endIndex_)
        : beginIndex(beginIndex_)
        , endIndex(endIndex_) {}

    bool isValid()
    {
        return beginIndex != -1 && endIndex != -1 && beginIndex < endIndex;
    }

    int beginIndex, endIndex;
};

class KDEVPYTHONCOMPLETION_EXPORT StringFormatter {
public:
    StringFormatter(const QString &string);

    bool isInsideReplacementVariable(int cursorPosition) const;
    const ReplacementVariable *getReplacementVariable(int cursorPosition) const;
    RangeInString getVariablePosition(int cursorPosition) const;

    int nextIdentifierId() const;

private:
    QString m_string;
    QList<ReplacementVariable> m_replacementVariables;
    QList<RangeInString> m_variablePositions;
};

class ReplacementVariable {

public:
    ReplacementVariable(QString identifier, QChar conversion = QChar(), QString formatSpec = QString())
        : m_identifier(identifier),
          m_conversion(conversion),
          m_formatSpec(formatSpec)
    {
    }

    const QString &identifier() const
    {
        return m_identifier;
    }

    bool isIdentifierNumeric() const
    {
        bool isNumeric;
        m_identifier.toInt(&isNumeric);
        return isNumeric;
    }

    const QChar &conversion() const
    {
        return m_conversion;
    }

    bool hasConversion() const
    {
        return ! m_conversion.isNull();
    }

    const QString &formatSpec() const
    {
        return m_formatSpec;
    }

    bool hasFormatSpec() const
    {
        return ! ( m_formatSpec.isNull() || m_formatSpec.isEmpty() );
    }

    // Convenience functions for extracting some of the parts of the format spec

    QChar fillCharacter() const
    {
        return hasFillCharacter() ? m_formatSpec.at(0) : QChar();
    }

    bool hasFillCharacter() const
    {
        QStringList alignChars = QStringList() << "<" << ">" << "^" << "=";
        return hasAlign() && alignChars.indexOf(m_formatSpec.at(1)) != -1;
    }

    QChar align() const
    {
        if ( hasAlign() ) {
            return hasFillCharacter() ? m_formatSpec.at(1) : m_formatSpec.at(0);
        }
        return QChar();
    }

    bool hasAlign() const
    {
        QRegExp regex("^.?[<>\\^=]");
        return m_formatSpec.contains(regex);
    }

    bool hasPrecision() const
    {
        if (fillCharacter() == '.') {
            return m_formatSpec.count('.') == 2;
        }
        return m_formatSpec.contains('.');
    }

    QChar type() const
    {
        return hasType() ? m_formatSpec.at(m_formatSpec.size() - 1) : QChar();
    }

    bool hasType() const
    {
        QStringList possibleTypes = QStringList() << "b" << "c" << "d" << "e" << "E"
                                                  << "f" << "F" << "g" << "G" << "n"
                                                  << "o" << "s" << "x" << "X" << "%";

        return (hasFormatSpec() && possibleTypes.indexOf(m_formatSpec.at(m_formatSpec.size() - 1)) != -1);
    }

    QString toString() const
    {
        QString variable = "{" + m_identifier;
        if (hasConversion()) {
            variable += '!' + m_conversion;
        }
        if (hasFormatSpec()) {
            variable += ':' + m_formatSpec;
        }
        variable += "}";

        return variable;
    }

private:
    QString m_identifier;
    QChar m_conversion;
    QString m_formatSpec;
};

}

#endif
