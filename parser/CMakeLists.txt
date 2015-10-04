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

# no more need to hunt for Python things here; already done in the toplevel CMake file
# TODO: test for the exact Python version required; PYTHON_VERSION_MICRO is available if needed.
if ( (NOT PYTHON_FOUND) OR (${PYTHON_VERSION_MINOR} GREATER 4) OR (${PYTHON_VERSION_MICRO} LESS 3) )
    message(FATAL_ERROR "Python >= 3.4.3 and < 3.5 with --enable-shared is required to build this version of kdev-python")
endif()

include_directories(kdev4pythonparser ${PYTHON_INCLUDE_DIRS})

kde4_add_library( kdev4pythonparser SHARED ${parser_SRCS} ${parser_STAT_SRCS} )
target_link_libraries(kdev4pythonparser LINK_PRIVATE
    ${KDE4_KDECORE_LIBS}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${QT_QTCORE_LIBRARY}
    ${PYTHON_LIBRARIES}
)

add_dependencies(kdev4pythonparser parser)
install(TARGETS kdev4pythonparser DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

add_subdirectory(tests)
