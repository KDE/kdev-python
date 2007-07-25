
#To properly find kdevelop-pg add -DKDEVPG_DATA_DIR=<kdevpg-install-path>/share to the
#cmake run if you installed it in a different directory than this plugin
#TODO: a cmake run is needed after changing one of the CMakeLists.txt, make will
#complain about the FindKDevelop-PG.cmake file not findable.
find_package(KDE4 REQUIRED)

find_package(KDevPlatform REQUIRED)

#Don't error out if the FindXXX are missing for these two
find_package(KDevelop-PG QUIET)
find_package(Flex QUIET)


INCLUDE_DIRECTORIES(
    ${KDEVPLATFORM_INCLUDE_DIR}/language/interfaces
    ${KDEVPLATFORM_INCLUDE_DIR}/interfaces
    ${KDEVPLATFORM_INCLUDE_DIR}/language
    ${KDEVPLATFORM_INCLUDE_DIR}/editor
    ${KDEVPLATFORM_INCLUDE_DIR}/language/backgroundparser
    ${KDE4_INCLUDES}
    ${KDE4_INCLUDE_DIR}/threadweaver
    ${CMAKE_CURRENT_BINARY_DIR}
    ${KDEVPLATFORM_INCLUDE_DIR}/language/duchain
    parser
)


set(parser_STAT_SRCS
    ${CMAKE_SOURCE_DIR}/parser/decoder.cpp
    ${CMAKE_SOURCE_DIR}/parser/python_io.cpp
    ${CMAKE_SOURCE_DIR}/parser/pythondriver.cpp
    )

macro(GET_PARSER_SRCS _srcsList)
    if(KDEVPG_FOUND AND FLEX_FOUND)
        include_directories(${KDEVPG_INCLUDE_DIR})
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
         set( ${_srcsList} ${_kdevpgList}
	    "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp")
    else(KDEVPG_FOUND AND FLEX_FOUND)
        include_directories(${CMAKE_SOURCE_DIR}/parser/generated ${CMAKE_SOURCE_DIR}/parser/generated/kdevelop-pg  )
        message(STATUS "Assuming existence of generated parser files")
        message( STATUS "Assuming existence of generated lexer files")
        set(${_srcsList}
            ${CMAKE_SOURCE_DIR}/parser/generated/python_parser.cpp
            ${CMAKE_SOURCE_DIR}/parser/generated/python_visitor.cpp
            ${CMAKE_SOURCE_DIR}/parser/generated/python_default_visitor.cpp
            ${CMAKE_SOURCE_DIR}/parser/generated/python_lexer.cpp )
    
    endif(KDEVPG_FOUND AND FLEX_FOUND)
endmacro(GET_PARSER_SRCS)

add_subdirectory(parser)

get_parser_srcs(parser_SRCS)

set(kdevpythonlanguagesupport_PART_SRCS
    pythonlanguagesupport.cpp
    pythonparsejob.cpp
    parser/parsesession.cpp
    parser/contextbuilder.cpp
    parser/pythoneditorintegrator.cpp
    ${parser_SRCS} ${parser_STAT_SRCS}
)

kde4_add_plugin(kdevpythonlanguagesupport ${kdevpythonlanguagesupport_PART_SRCS})

target_link_libraries(kdevpythonlanguagesupport
    ${KDE4_KDEUI_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARY}
    ${KDEVPLATFORM_LANGUAGE_LIBRARY}
    ${KDE4_THREADWEAVER_LIBRARIES}
    ${KDEVPLATFORM_EDITOR_LIBRARY}
)

install(TARGETS kdevpythonlanguagesupport DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kdevpythonsupport.desktop DESTINATION ${SERVICES_INSTALL_DIR})

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



