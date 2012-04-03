if(WIN32)
    include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../python-src/PC)
endif(WIN32)
include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

set(parser_STAT_SRCS
    parsesession.cpp
    ast.cpp
    astdefaultvisitor.cpp
    astvisitor.cpp
    astbuilder.cpp
)

kde4_add_library( kdev4pythonparser SHARED ${parser_SRCS} ${parser_STAT_SRCS} )
target_link_libraries(kdev4pythonparser 
    ${KDE4_KDECORE_LIBS} 
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${QT_QTCORE_LIBRARY} 
)
if(NOT WIN32)
    target_link_libraries(kdev4pythonparser
        ${kdevpython_SOURCE_DIR}/python-src/libpython2.7-kdevelop.so
    )
endif(NOT WIN32)

install(TARGETS kdev4pythonparser DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

