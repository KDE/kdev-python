set(duchain_SRCS
    declarations/functiondeclaration.cpp

    types/nonetype.cpp
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

    navigation/navigationwidget.cpp
    navigation/declarationnavigationcontext.cpp

    correctionhelper.cpp

    assistants/missingincludeassistant.cpp
    ../docfilekcm/docfilewizard.cpp # for the docfile generation assistant widget, to be used in the problem resolver
)

ecm_qt_declare_logging_category(duchain_SRCS
    HEADER duchaindebug.h
    IDENTIFIER KDEV_PYTHON_DUCHAIN
    CATEGORY_NAME "kdevelop.plugins.python.duchain"
    DESCRIPTION "KDevelop plugin: Python language support - duchain"
    EXPORT KDEVPYTHON
)

add_library( kdevpythonduchain SHARED ${duchain_SRCS} )

generate_export_header( kdevpythonduchain EXPORT_MACRO_NAME KDEVPYTHONDUCHAIN_EXPORT
                                           EXPORT_FILE_NAME pythonduchainexport.h
)

target_link_libraries( kdevpythonduchain LINK_PRIVATE
    KF${KF_MAJOR_VERSION}::TextEditor
    KDev::Interfaces
    KDev::Language
    KDev::Project
    KDev::Util
    kdevpythonparser
)

install(TARGETS kdevpythonduchain DESTINATION ${KDE_INSTALL_TARGETS_DEFAULT_ARGS})


add_subdirectory(navigation)

if (BUILD_TESTING)
    add_subdirectory(tests)
endif()

add_subdirectory(types)
add_subdirectory(declarations)

add_subdirectory(assistants)
