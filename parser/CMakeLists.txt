


include_directories(${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    )

set(parser_STAT_SRCS
    decoder.cpp
    python_io.cpp
    pythondriver.cpp
    parsesession.cpp
    )

if(KDEVPG_FOUND AND FLEX_FOUND)
    kdevpg_generate(_kdevpgList python
        "${CMAKE_SOURCE_DIR}/parser/python.g"
        "${CMAKE_SOURCE_DIR}/parser/python_lexer.h"
    )

    add_custom_target( debuginfo
                ${KDEVPG_EXECUTABLE} --terminals
                "${CMAKE_CURRENT_SOURCE_DIR}/parser/python.g" ">terminals"
        COMMAND  ${KDEVPG_EXECUTABLE} --symbols
                "${CMAKE_CURRENT_SOURCE_DIR}/parser/python.g" ">symbols"
        COMMAND  ${KDEVPG_EXECUTABLE} --rules
                "${CMAKE_CURRENT_SOURCE_DIR}/parser/python.g" ">rules" "2>errors"
        WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
    )
    # Copy python_lexer.ll to the builddir, so that flex doesn't write out
    # absolute paths in the generated file when we pass them as arguments.
    # In short, I don't want stuff like
    # '#line 2 "/home/kde/build/.../python_lexer.cpp" in SVN.
    add_custom_command(
        OUTPUT  "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.ll"
        MAIN_DEPENDENCY "${CMAKE_SOURCE_DIR}/parser/python_lexer.ll"
        COMMAND ${CMAKE_COMMAND} ARGS -E copy_if_different
                "${CMAKE_SOURCE_DIR}/parser/python_lexer.ll"
                "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.ll"
        )
    add_custom_command(
        OUTPUT  "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp"
        MAIN_DEPENDENCY "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.ll"
        DEPENDS "${CMAKE_SOURCE_DIR}/parser/python_lexer.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h"
        COMMAND ${FLEX_EXECUTABLE}
        ARGS    -o"python_lexer.cpp"
                -d python_lexer.ll
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        )

    set( parser_SRCS
        ${_kdevpgList}
        "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp"
    )
else(KDEVPG_FOUND AND FLEX_FOUND)
    message(STATUS "Assuming existence of generated parser files")
    message( STATUS "Assuming existence of generated lexer files")
    set(parser_SRCS
        generated/python_parser.cpp
        generated/python_visitor.cpp
        generated/python_default_visitor.cpp
        generated/python_lexer.cpp )

endif(KDEVPG_FOUND AND FLEX_FOUND)

add_subdirectory(tests)

kde4_add_library( kdev4pythonparser ${parser_SRCS} ${parser_STAT_SRCS} )
target_link_libraries( kdev4pythonparser ${KDE4_KDECORE_LIBS} )

kde4_add_executable( python-parser main.cpp )

target_link_libraries(python-parser ${QT_QTCORE_LIBRARY} kdev4pythonparser)

install(TARGETS python-parser DESTINATION ${BIN_INSTALL_DIR})
install(TARGETS kdev4pythonparser DESTINATION ${LIB_INSTALL_DIR})


add_custom_target( copy-generated
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_parser.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_parser.cpp"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h" "${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_parser.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_ast.h" "${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_ast.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.h" "${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_visitor.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_visitor.cpp"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.h" "${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_default_visitor.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_default_visitor.cpp"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_lexer.cpp"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_parser.cpp"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.cpp"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.h"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.cpp"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.h"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_ast.h"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp"
    )

