PROJECT(kdevpython)

cmake_minimum_required(VERSION 2.8)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${kdevpython_SOURCE_DIR}/cmake/)

find_package(KDE4 REQUIRED)
find_package(KDevPlatform 1.0.0 REQUIRED)

# first, build our custom python distribution
configure_file("${CMAKE_CURRENT_SOURCE_DIR}/python-src/build-for-kdevelop.sh.in" "${CMAKE_CURRENT_SOURCE_DIR}/python-src/build-for-kdevelop.sh")
execute_process(
    COMMAND /bin/bash ${CMAKE_CURRENT_SOURCE_DIR}/python-src/build-for-kdevelop.sh
)

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
