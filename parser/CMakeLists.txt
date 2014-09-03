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
)

find_package(PythonLibs 3.4 REQUIRED)
if ( NOT ${PYTHONLIBS_FOUND} OR ${PYTHON_VERSION_MINOR} GREATER 4 )
    message(FATAL_ERROR "Python 3.4 with --enable-shared is required to build kdev-python")
endif()

include_directories(kdev4pythonparser ${PYTHON_INCLUDE_DIRS})

add_library( kdev4pythonparser SHARED ${parser_SRCS} ${parser_STAT_SRCS} )
target_link_libraries(kdev4pythonparser LINK_PRIVATE
    KF5::KDELibs4Support
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    Qt5::Core
    ${PYTHON_LIBRARY}
)

#add_dependencies(kdev4pythonparser parser)
install(TARGETS kdev4pythonparser DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

add_subdirectory(tests)
