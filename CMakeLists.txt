
#To properly find kdevelop-pg add -DKDEVPG_DATA_DIR=<kdevpg-install-path>/share to the
#cmake run if you installed it in a different directory than this plugin
#TODO: a cmake run is needed after changing one of the CMakeLists.txt, make will
#complain about the FindKDevelop-PG.cmake file not findable.
if( KDEVPG_DATA_DIR )
    set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${KDEVPG_DATA_DIR}/cmake/modules )
else( KDEVPG_DATA_DIR )
    set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_INSTALL_PREFIX}/share/cmake/modules )
endif( KDEVPG_DATA_DIR )

find_package(KDE4 REQUIRED)
find_package(KDevPlatform REQUIRED)

find_package(KDevelop-PG)
find_package(Flex)


INCLUDE_DIRECTORIES(
    ${KDEVPLATFORM_INCLUDE_DIR}/language/interfaces
    ${KDEVPLATFORM_INCLUDE_DIR}/interfaces
    ${KDEVPLATFORM_INCLUDE_DIR}/language
    ${KDEVPLATFORM_INCLUDE_DIR}/language/backgroundparser
    ${KDE4_INCLUDES}
    ${KDE4_INCLUDE_DIR}/threadweaver
    ${CMAKE_CURRENT_BINARY_DIR}
    parser
)


set(parser_STAT_SRCS
    ${CMAKE_CURRENT_SOURCE_DIR}/parser/decoder.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/parser/python_io.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/parser/pythondriver.cpp
    )

set(parser_gen_SRCS)
set(lexer_gen_SRCS)
set(parser_SRCS)
set(lexer_SRCS)

if(KDEVPG_FOUND AND FLEX_FOUND)
    include_directories(${KDEVPG_INCLUDE_DIR})
    add_custom_command(
        OUTPUT  "${CMAKE_CURRENT_BINARY_DIR}/python_ast.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_parser.cpp"
                "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.cpp"
                "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.cpp"
        DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/parser/python.g"
                "${CMAKE_CURRENT_SOURCE_DIR}/parser/python_lexer.h"
        COMMAND ${KDEVPG_EXECUTABLE}
        ARGS    --output=python
                "${CMAKE_CURRENT_SOURCE_DIR}/parser/python.g"
        WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
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
    
    set( parser_gen_SRCS
        "${CMAKE_CURRENT_BINARY_DIR}/python_parser.cpp"
        "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.cpp"
        "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.cpp")
    
    set_source_files_properties(
        ${parser_gen_SRCS}
        "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h"
        "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.h"
        "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.h"
        GENERATED
        )
    add_custom_command(
        OUTPUT  "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp"
        DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/parser/python_lexer.ll"
                "${CMAKE_CURRENT_SOURCE_DIR}/parser/python_lexer.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h"
        COMMAND ${FLEX_EXECUTABLE}
        ARGS    -o"${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp"
                -d
                "${CMAKE_CURRENT_SOURCE_DIR}/parser/python_lexer.ll"
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        )
    
    set(lexer_gen_SRCS ${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp)
    
    set_source_files_properties(
        ${lexer_gen_SRCS}
        GENERATED
        )

else(KDEVPG_FOUND AND FLEX_FOUND)
    include_directories(${CMAKE_SOURCE_DIR}/parser/generated)
    message(STATUS "Assuming existence of generated parser files")
    set(parser_SRCS
        ${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_parser.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_visitor.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_default_visitor.cpp
    )
    message( STATUS "Assuming existence of generated lexer files")
    set(lexer_SRCS
        ${CMAKE_CURRENT_SOURCE_DIR}/parser/generated/python_lexer.cpp )

endif(KDEVPG_FOUND AND FLEX_FOUND)

add_subdirectory(parser)


set(kdevpythonlanguagesupport_PART_SRCS
    pythonlanguagesupport.cpp
    pythonparsejob.cpp
    parser/parsesession.cpp
    ${lexer_gen_SRCS} ${parser_gen_SRCS} 
    ${lexer_SRCS} ${parser_SRCS} ${parser_STAT_SRCS}
)

kde4_automoc(${kdevpythonlanguagesupport_PART_SRCS})

kde4_add_plugin(kdevpythonlanguagesupport ${kdevpythonlanguagesupport_PART_SRCS})

target_link_libraries(kdevpythonlanguagesupport
    ${KDE4_KDEUI_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARY}
    ${KDEVPLATFORM_LANGUAGE_LIBRARY}
    ${KDE4_THREADWEAVER_LIBRARIES}
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



