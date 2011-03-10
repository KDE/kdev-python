PROJECT(kdevpython)

cmake_minimum_required(VERSION 2.8)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${kdevpython_SOURCE_DIR}/cmake/)

find_package(KDE4 REQUIRED)
find_package(KDevPlatform 1.0.0 REQUIRED)

# first, build our custom python distribution
if ( EXISTS ${kdevpython_SOURCE_DIR}/python-src/Makefile )
    message(STATUS "Skipping reconfiguration of python sources, assuming nothing changed here. If you want to force reconfiguring, delete the Makefile in python-src/.")
elseif ( NOT EXISTS ${kdevpython_SOURCE_DIR}/python-src/Makefile )
    message(STATUS "Configuring python 2.7...")
    execute_process(COMMAND /bin/bash ${kdevpython_SOURCE_DIR}/python-src/configure --enable-shared WORKING_DIRECTORY ${kdevpython_SOURCE_DIR}/python-src)
endif( EXISTS ${kdevpython_SOURCE_DIR}/python-src/Makefile )

execute_process(COMMAND /usr/bin/env make -f ${kdevpython_SOURCE_DIR}/python-src/Makefile WORKING_DIRECTORY ${kdevpython_SOURCE_DIR}/python-src)
install(FILES ${kdevpython_SOURCE_DIR}/python-src/libpython2.7.so DESTINATION ${BIN_INSTALL_DIR})

message(STATUS "Any warnings about missing dependencies for python can be ignored, you won't need any of them for sure.")
message(STATUS "Fine, going to build the actual plugin now.")

set(CMAKE_CXX_FLAGS_DEBUG -Wfatal-errors -Wall)

# then, build the plugin
include_directories(
    ${KDEVPLATFORM_INCLUDE_DIR}
    ${KDE4_INCLUDES}
    ${KDE4_INCLUDE_DIR}/threadweaver
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/duchain
    ${CMAKE_CURRENT_SOURCE_DIR}/parser
    ${CMAKE_CURRENT_SOURCE_DIR}/python-src
    ${CMAKE_CURRENT_BINARY_DIR}/parser
)

add_definitions( -DKDE_DEFAULT_DEBUG_AREA=9011 )

include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}/parser
)


add_subdirectory(parser)
add_subdirectory(duchain)
add_subdirectory(codecompletion)

set(kdevpythonlanguagesupport_PART_SRCS
    pythonlanguagesupport.cpp
    pythonparsejob.cpp
    pythonhighlighting.cpp
)

kde4_add_plugin(kdevpythonlanguagesupport ${kdevpythonlanguagesupport_PART_SRCS})

target_link_libraries(kdevpythonlanguagesupport
    ${KDE4_KDEUI_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${KDE4_THREADWEAVER_LIBRARIES}
    ${KDE4_KTEXTEDITOR_LIBS}
    kdev4pythoncompletion
    kdev4pythonparser
    kdev4pythonduchain
)

configure_file("${CMAKE_CURRENT_SOURCE_DIR}/parser/parserConfig.h.in" "${CMAKE_CURRENT_SOURCE_DIR}/parser/parserConfig.h" )

install(TARGETS kdevpythonlanguagesupport DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kdevpythonsupport.desktop DESTINATION ${SERVICES_INSTALL_DIR})
install(FILES pythonpythonparser.py DESTINATION ${BIN_INSTALL_DIR})
install(FILES documentation/pydoc.py DESTINATION ${BIN_INSTALL_DIR})
install(FILES documentation/test.py DESTINATION ${BIN_INSTALL_DIR}) # TODO fix me
