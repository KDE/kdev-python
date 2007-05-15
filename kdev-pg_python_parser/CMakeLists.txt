PROJECT( python_parser )
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR})

SET(parser_srcs)

find_program(KDEVPG_EXECUTABLE
	NAMES kdev-pg
	PATHS /usr/bin/
	     /home/andreas/kdev-pg/bin
	     /home/piyush/soc/kdev-pg/build/kdev-pg/
	     /root/soc/kdevelop/build/kdev-pg
	DOC "KDev-Pg")


find_program(FLEX_EXECUTABLE
	NAMES flex
	PATHS /usr/bin/
	DOC "Flex")

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

set( parser_srcs
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

    ADD_CUSTOM_COMMAND(
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

    SET(parser_srcs ${CMAKE_CURRENT_BINARY_DIR}/python_lexer.cpp ${parser_srcs})

    SET_SOURCE_FILES_PROPERTIES(
        ${CMAKE_CURRENT_BINARY_DIR}/cool_lexer.cpp
        GENERATED
        )

set( assembled_parser_srcs
	${parser_srcs}
	python_io.cpp
	)

add_executable( python-parser ${assembled_parser_srcs} decoder.cpp main.cpp )

