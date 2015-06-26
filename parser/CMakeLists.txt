include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

set(parser_STAT_SRCS
    codehelpers.cpp
    parsesession.cpp
    ast.cpp
    astdefaultvisitor.cpp
    astvisitor.cpp
    astbuilder.cpp
    cythonsyntaxremover.cpp
    parserdebug.cpp
)

find_package(PythonLibs 3.5.0 REQUIRED)
if ( (NOT PYTHONLIBS_FOUND) OR ${PYTHON_VERSION_MINOR} GREATER 5 )
    message(FATAL_ERROR "Python >= 3.5.0 with --enable-shared is required to build kdev-python")
endif()

include_directories(kdevpythonparser ${PYTHON_INCLUDE_DIRS})

add_library( kdevpythonparser SHARED ${parser_STAT_SRCS} )

generate_export_header(kdevpythonparser EXPORT_MACRO_NAME KDEVPYTHONPARSER_EXPORT
                                        EXPORT_FILE_NAME parserexport.h)

target_link_libraries(kdevpythonparser LINK_PRIVATE
    KDev::Language
    KDev::Util
    Qt5::Core
    ${PYTHON_LIBRARIES}
)

install(TARGETS kdevpythonparser DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

add_subdirectory(tests)
