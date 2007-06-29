project( python_parser )

find_package(Qt4 REQUIRED)

find_package(KDevelop-PG)
find_package(Flex)

add_subdirectory(tests)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
include_directories(${QT_INCLUDES})

set(parser_STAT_SRCS
    decoder.cpp
    python_io.cpp
    pythondriver.cpp
    )

if (CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS_DEBUGFULL  "-g3 -O0 -fno-inline")
    set(CMAKE_C_FLAGS_DEBUGFULL  "-g3 -O0 -fno-inline")
endif (CMAKE_COMPILER_IS_GNUCXX)


#find_package(KDE4 REQUIRED)
#include (KDE4Defaults)
#include (MacroLibrary)



if(KDEVPG_FOUND AND FLEX_FOUND)
    add_custom_command(
        OUTPUT  "${CMAKE_CURRENT_BINARY_DIR}/python_ast.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_parser.cpp"
                "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.cpp"
                "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.cpp"
        DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/python.g"
                "${CMAKE_CURRENT_SOURCE_DIR}/python_lexer.h"
        COMMAND ${KDEVPG_EXECUTABLE}
        ARGS    --output=python
                "${CMAKE_CURRENT_SOURCE_DIR}/python.g"
        WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
    )
    
    add_custom_target( debuginfo
                ${KDEVPG_EXECUTABLE} --terminals
                "${CMAKE_CURRENT_SOURCE_DIR}/python.g" ">terminals"
        COMMAND  ${KDEVPG_EXECUTABLE} --symbols
                "${CMAKE_CURRENT_SOURCE_DIR}/python.g" ">symbols"
        COMMAND  ${KDEVPG_EXECUTABLE} --rules
                "${CMAKE_CURRENT_SOURCE_DIR}/python.g" ">rules" "2>errors"
        WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
    )
    
    set( parser_SRCS
        "${CMAKE_CURRENT_BINARY_DIR}/python_parser.cpp"
        "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.cpp"
        "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.cpp")
    
    set_source_files_properties(
        "${CMAKE_CURRENT_BINARY_DIR}/python_parser.cpp"
        "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.cpp"
        "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.cpp"
        "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h"
        "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.h"
        "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.h"
        GENERATED
        )
    add_custom_command(
        OUTPUT  "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp"
        DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/python_lexer.ll"
                "${CMAKE_CURRENT_SOURCE_DIR}/python_lexer.h"
                "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h"
        COMMAND ${FLEX_EXECUTABLE}
        ARGS    -o"${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp"
                -d
                "${CMAKE_CURRENT_SOURCE_DIR}/python_lexer.ll"
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        )
    
    set(lexer_SRCS ${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp)
    
    set_source_files_properties(
        ${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp
        GENERATED
        )

else(KDEVPG_FOUND AND FLEX_FOUND)
    message(STATUS "Assuming existence of generated parser files")
    set(parser_SRCS
        ${CMAKE_CURRENT_SOURCE_DIR}/generated/python_parser.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/generated/python_visitor.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/generated/python_default_visitor.cpp
    )
    message( STATUS "Assuming existence of generated lexer files")
    set(lexer_SRCS
        ${CMAKE_CURRENT_SOURCE_DIR}/generated/python_lexer.cpp )

    include_directories(${CMAKE_CURRENT_SOURCE_DIR}/generated)
endif(KDEVPG_FOUND AND FLEX_FOUND)

add_library(kdevpythonparser SHARED ${parser_STAT_SRCS} ${parser_SRCS} ${lexer_SRCS})
target_link_libraries(kdevpythonparser ${QT_QTCORE_LIBRARY})
set_target_properties(kdevpythonparser PROPERTIES VERSION 1.0.0 SOVERSION 1 )

add_executable( python-parser main.cpp )
target_link_libraries(python-parser ${QT_QTCORE_LIBRARY} kdevpythonparser)

add_custom_target( copy-generated
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_parser.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/generated/python_parser.cpp"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h" "${CMAKE_CURRENT_SOURCE_DIR}/generated/python_parser.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_ast.h" "${CMAKE_CURRENT_SOURCE_DIR}/generated/python_ast.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.h" "${CMAKE_CURRENT_SOURCE_DIR}/generated/python_visitor.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/generated/python_visitor.cpp"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.h" "${CMAKE_CURRENT_SOURCE_DIR}/generated/python_default_visitor.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/generated/python_default_visitor.cpp"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp" "${CMAKE_CURRENT_SOURCE_DIR}/generated/python_lexer.cpp"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_parser.cpp"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_parser.h"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.cpp"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_visitor.h"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.cpp"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_default_visitor.h"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_ast.h"
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp"
    )

