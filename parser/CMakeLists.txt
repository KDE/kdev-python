


include_directories(${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    )

set(parser_STAT_SRCS
    pythondriver.cpp
    parsesession.cpp
    pythonlexer.cpp
    kwcheck.cpp
    numbercheck.cpp
    ast.cpp
    astdefaultvisitor.cpp
    astvisitor.cpp
    astbuilder.cpp
    astprinter.cpp
    )

if(KDEVPGQT_FOUND)
     kdevpgqt_generate(_kdevpgList python NAMESPACE PythonParser
        "${kdevpython_SOURCE_DIR}/parser/python.g"
        "${kdevpython_SOURCE_DIR}/parser/pythonlexer.h"
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
    set( parser_SRCS
        ${_kdevpgList}
    )
else(KDEVPGQT_FOUND)
    message(STATUS "Assuming existence of generated parser files")
    message( STATUS "Assuming existence of generated lexer files")
    set(parser_SRCS
        generated/pythonparser.cpp
        generated/pythonvisitor.cpp
        generated/pythondefaultvisitor.cpp )

endif(KDEVPGQT_FOUND)

add_subdirectory(tests)

kde4_add_library( kdev4pythonparser SHARED ${parser_SRCS} ${parser_STAT_SRCS} )
target_link_libraries( kdev4pythonparser ${KDE4_KDECORE_LIBS} )

kde4_add_executable( python-parser main.cpp )

target_link_libraries(python-parser ${QT_QTCORE_LIBRARY} kdev4pythonparser)

install(TARGETS python-parser ${INSTALL_TARGETS_DEFAULT_ARGS})
install(TARGETS kdev4pythonparser DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})


add_custom_target( copy-generated
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${kdevpython_BINARY_DIR}/parser/pythonparser.cpp" "${kdevpython_SOURCE_DIR}/parser/generated/pythonparser.cpp"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${kdevpython_BINARY_DIR}/parser/pythonparser.h" "${kdevpython_SOURCE_DIR}/parser/generated/pythonparser.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${kdevpython_BINARY_DIR}/parser/pythonast.h" "${kdevpython_SOURCE_DIR}/parser/generated/pythonast.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${kdevpython_BINARY_DIR}/parser/pythonvisitor.h" "${kdevpython_SOURCE_DIR}/parser/generated/pythonvisitor.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${kdevpython_BINARY_DIR}/parser/pythonvisitor.cpp" "${kdevpython_SOURCE_DIR}/parser/generated/pythonvisitor.cpp"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${kdevpython_BINARY_DIR}/parser/pythondefaultvisitor.h" "${kdevpython_SOURCE_DIR}/parser/generated/pythondefaultvisitor.h"
    COMMAND ${CMAKE_COMMAND} -E copy_if_different "${kdevpython_BINARY_DIR}/parser/pythondefaultvisitor.cpp" "${kdevpython_SOURCE_DIR}/parser/generated/pythondefaultvisitor.cpp"
    DEPENDS "${kdevpython_BINARY_DIR}/parser/pythonparser.cpp"
    DEPENDS "${kdevpython_BINARY_DIR}/parser/pythonparser.h"
    DEPENDS "${kdevpython_BINARY_DIR}/parser/pythonvisitor.cpp"
    DEPENDS "${kdevpython_BINARY_DIR}/parser/pythonvisitor.h"
    DEPENDS "${kdevpython_BINARY_DIR}/parser/pythondefaultvisitor.cpp"
    DEPENDS "${kdevpython_BINARY_DIR}/parser/pythondefaultvisitor.h"
    DEPENDS "${kdevpython_BINARY_DIR}/parser/pythonast.h"
    )

