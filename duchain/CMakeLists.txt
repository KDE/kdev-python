
include_directories(${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    )

set(duchain_SRCS
    declarations/functiondeclaration.cpp
    declarations/classdeclaration.cpp

    types/hintedtype.cpp
    types/unsuretype.cpp
    types/indexedcontainer.cpp

    expressionvisitor.cpp
    helpers.cpp
    pythonducontext.cpp
    contextbuilder.cpp
    pythoneditorintegrator.cpp
    declarationbuilder.cpp
    usebuilder.cpp
    dumpchain.cpp
    duchaindebug.cpp

    navigation/navigationwidget.cpp
    navigation/declarationnavigationcontext.cpp

    correctionhelper.cpp

    assistants/missingincludeassistant.cpp
    ../docfilekcm/docfilewizard.cpp # for the docfile generation assistant widget, to be used in the problem resolver
)


add_library( kdevpythonduchain SHARED ${duchain_SRCS} )

generate_export_header( kdevpythonduchain EXPORT_MACRO_NAME KDEVPYTHONDUCHAIN_EXPORT
                                           EXPORT_FILE_NAME pythonduchainexport.h
)

target_link_libraries( kdevpythonduchain LINK_PRIVATE
    Qt5::WebKitWidgets
    KF5::KDELibs4Support
    KF5::TextEditor
    KDev::Interfaces
    KDev::Language
    KDev::Project
    kdevpythonparser
 )

install(TARGETS kdevpythonduchain DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})


add_subdirectory(navigation)

add_subdirectory(tests)

add_subdirectory(types)
add_subdirectory(declarations)

add_subdirectory(assistants)
