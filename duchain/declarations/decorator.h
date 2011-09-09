#ifndef DECORATOR_H
#define DECORATOR_H

#include <QStringList>
#include <language/duchain/indexedstring.h>

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
    * @return :IndexedString the additional information, as IndexedString
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
    * @return void
    **/
    inline void setName(const QString& name) {
        m_name = IndexedString(name);
    }
    /**
    * @brief Sets the additional information which should be stored with this Decorator.
    *
    * @param arg ...
    * @return void
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