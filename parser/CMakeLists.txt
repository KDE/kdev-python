set(parser_STAT_SRCS
    codehelpers.cpp
    parsesession.cpp
    ast.cpp
    astdefaultvisitor.cpp
    astvisitor.cpp
    astbuilder.cpp
    asttransformer.cpp
    cythonsyntaxremover.cpp
    rangefixvisitor.cpp
)
ecm_qt_declare_logging_category(parser_STAT_SRCS
    HEADER parserdebug.h
    IDENTIFIER KDEV_PYTHON_PARSER
    CATEGORY_NAME "kdevelop.plugins.python.parser"
    DESCRIPTION "KDevelop plugin: Python language support - parser"
    EXPORT KDEVPYTHON
)

include_directories(${PYTHON_INCLUDE_DIRS})

add_library( kdevpythonparser SHARED ${parser_STAT_SRCS} )

generate_export_header(kdevpythonparser EXPORT_MACRO_NAME KDEVPYTHONPARSER_EXPORT
                                        EXPORT_FILE_NAME parserexport.h)

target_link_libraries(kdevpythonparser LINK_PRIVATE
    KDev::Language
    Qt5::Core
    ${PYTHON_LIBRARIES}
)

install(TARGETS kdevpythonparser DESTINATION ${KDE_INSTALL_TARGETS_DEFAULT_ARGS})

if (BUILD_TESTING)
    add_subdirectory(tests)
endif()
