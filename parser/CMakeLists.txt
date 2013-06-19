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
)

set(Python_ADDITIONAL_VERSIONS 3.4)
message(WARNING "Note to self: fix finding python before a release, this is not going to work")
set(PYTHON_INCLUDE_DIR /usr/include/python3.4m)
set(PYTHON_LIBRARY /usr/lib)
find_package(PythonLibs 3.4 EXACT REQUIRED)
if ( NOT ${PYTHONLIBS_FOUND} )
    message(FATAL_ERROR "python libs not found")
endif()

include_directories(kdev4pythonparser ${PYTHON_INCLUDE_DIRS})

kde4_add_library( kdev4pythonparser SHARED ${parser_SRCS} ${parser_STAT_SRCS} )
target_link_libraries(kdev4pythonparser
    ${KDE4_KDECORE_LIBS}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${QT_QTCORE_LIBRARY}
    ${PYTHON_LIBRARIES}/libpython3.4m.so.1.0
)

add_dependencies(kdev4pythonparser parser)
install(TARGETS kdev4pythonparser DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

add_subdirectory(tests)
