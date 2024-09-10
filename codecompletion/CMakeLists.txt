set(completion_SRCS
    context.cpp 
    model.cpp
    worker.cpp
    helpers.cpp

    items/missingincludeitem.cpp
    items/declaration.cpp
    items/functiondeclaration.cpp
    items/implementfunction.cpp
    items/importfile.cpp
    items/keyword.cpp
    items/replacementvariable.cpp
)
ecm_qt_declare_logging_category(completion_SRCS
    HEADER codecompletiondebug.h
    IDENTIFIER KDEV_PYTHON_CODECOMPLETION
    CATEGORY_NAME "kdevelop.plugins.python.codecompletion"
    DESCRIPTION "KDevelop plugin: Python language support - codecompletion"
    EXPORT KDEVPYTHON
)

add_library(kdevpythoncompletion SHARED ${completion_SRCS})

generate_export_header(kdevpythoncompletion EXPORT_MACRO_NAME KDEVPYTHONCOMPLETION_EXPORT
                                             EXPORT_FILE_NAME pythoncompletionexport.h
)

add_dependencies(kdevpythoncompletion
    kdevpythonparser 
    kdevpythonduchain
)

target_link_libraries(kdevpythoncompletion LINK_PRIVATE
    KDev::Language
    KDev::Interfaces
    KDev::Project
    kdevpythonduchain
    kdevpythonparser
)

install(TARGETS kdevpythoncompletion DESTINATION ${KDE_INSTALL_TARGETS_DEFAULT_ARGS})

if (BUILD_TESTING)
    add_subdirectory(tests)
endif()
