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
    pythondriver.cpp
)

# This will build the stuff in python-src/.
# I know it would be better to use INSTALL() instead of cp, but I've no idea how...
if ( EXISTS ${kdevpython_SOURCE_DIR}/python-src/Makefile )
    message(STATUS "Skipping reconfiguration of python sources, assuming nothing changed here. If you want to force reconfiguring, delete the Makefile in python-src/.")
elseif ( NOT EXISTS ${kdevpython_SOURCE_DIR}/python-src/Makefile )
    message(STATUS "Configuring python 2.7...")
    execute_process(COMMAND /bin/bash ${kdevpython_SOURCE_DIR}/python-src/configure --enable-shared WORKING_DIRECTORY ${kdevpython_SOURCE_DIR}/python-src)
endif( EXISTS ${kdevpython_SOURCE_DIR}/python-src/Makefile )

execute_process(COMMAND /usr/bin/env make -f ${kdevpython_SOURCE_DIR}/python-src/Makefile WORKING_DIRECTORY ${kdevpython_SOURCE_DIR}/python-src)
message(STATUS "Any warnings about missing dependencies for python can be ignored, you won't need any of them for sure.")

execute_process(COMMAND /usr/bin/env cp ${kdevpython_SOURCE_DIR}/python-src/libpython2.7.so ${BIN_INSTALL_DIR})

kde4_add_library( kdev4pythonparser SHARED ${parser_SRCS} ${parser_STAT_SRCS} )
target_link_libraries(kdev4pythonparser 
    ${KDE4_KDECORE_LIBS} 
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${QT_QTCORE_LIBRARY} 
    ${BIN_INSTALL_DIR}/libpython2.7.so
)

install(TARGETS kdev4pythonparser DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

