include_directories(${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    )

set(parser_STAT_SRCS
    parsesession.cpp
    ast.cpp
    astdefaultvisitor.cpp
    astvisitor.cpp
    astbuilder.cpp
)

# kdevpgqt_generate(_kdevpgList python NAMESPACE PythonParser
#     "${kdevpython_SOURCE_DIR}/parser/python.g"
#     "${kdevpython_SOURCE_DIR}/parser/pythonlexer.h"
# )

# add_custom_target( debuginfo
#             ${KDEVPG_EXECUTABLE} --terminals
#             "${CMAKE_CURRENT_SOURCE_DIR}/parser/python.g" ">terminals"
#     COMMAND  ${KDEVPG_EXECUTABLE} --symbols
#             "${CMAKE_CURRENT_SOURCE_DIR}/parser/python.g" ">symbols"
#     COMMAND  ${KDEVPG_EXECUTABLE} --rules
#             "${CMAKE_CURRENT_SOURCE_DIR}/parser/python.g" ">rules" "2>errors"
#     WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
# )
# set( parser_SRCS
#     ${_kdevpgList}
# )
#add_subdirectory(tests)

kde4_add_library( kdev4pythonparser SHARED ${parser_SRCS} ${parser_STAT_SRCS} )
target_link_libraries(kdev4pythonparser 
    ${KDE4_KDECORE_LIBS} 
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${QT_QTCORE_LIBRARY} 
)

install(TARGETS kdev4pythonparser DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

