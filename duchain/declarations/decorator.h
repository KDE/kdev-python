/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2012 Sven Brauch <svenbrauch@googlemail.com>                *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/

#ifndef DECORATOR_H
#define DECORATOR_H

#include <QStringList>
#include <serialization/indexedstring.h>

using namespace KDevelop;

namespace Python {

/**
 * @brief This class represents a Decorator of a function or class declaration
 * 
 * m_name is the name of the decorator
 * m_additionalInformation is some piece of additional information you can use for whatever you want;
 *  currently this is used by python to store the value of the first argument passed to the decorator,
 *  because this is needed for the way some of the documentation works.
 **/
class Decorator {
public:
    /**
    * @brief Constructs a new Decorator with a default name
    *
    **/
    Decorator() {
        m_name = IndexedString("(no name)");
        m_additionalInformation = IndexedString();
    }
    /**
    * @brief Constructs a new Decorator with the given name
    *
    * @param name name of the decorator
    **/
    Decorator(const QString& name) {
        m_name = IndexedString(name);
        m_additionalInformation = IndexedString();
    };
    /**
    * @brief Gets the additional information associated with this Decorator
    *
    * @return IndexedString the additional information, as IndexedString
    **/
    inline const IndexedString additionalInformation() const {
        return m_additionalInformation;
    }
    /**
    * @brief Gets the name of the decorator, reconstructed from the IndexedString which is stored.
    *
    * @return const QString the name
    **/
    inline const QString name() const {
        return m_name.str();
    }
    /**
    * @brief Gets the name of the decorator as IndexedString. Other than name(), this is fast and should be used if possible.
    *
    * @return :IndexedString the name, as indexed string
    **/
    inline const IndexedString fastName() const {
        return m_name;
    }
    /**
    * @brief Sets the name of the Decorator.
    *
    * @param name well, the name to use.
    **/
    inline void setName(const QString& name) {
        m_name = IndexedString(name);
    }
    /**
    * @brief Sets the additional information which should be stored with this Decorator.
    *
    * @param arg ...
    **/
    inline void setAdditionalInformation(const QString& arg) {
        m_additionalInformation = IndexedString(arg);
    }
private:
    IndexedString m_additionalInformation;
    IndexedString m_name;
};

}

#endif
