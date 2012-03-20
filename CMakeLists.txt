PROJECT(kdevpython)

message("** Important: ** If you have trouble building this, please read the INSTALL file first.")

cmake_minimum_required(VERSION 2.8)

enable_testing()

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${kdevpython_SOURCE_DIR}/cmake/)

find_package(KDE4 REQUIRED)
find_package(KDevPlatform 1.3.60 REQUIRED)
find_package(KDevelop-PG-Qt REQUIRED)

set(CMAKE_CXX_FLAGS_DEBUG "-Wfatal-errors -Wall")

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
    ${KDEVPGQT_INCLUDE_DIR}
)

add_definitions( -DKDE_DEFAULT_DEBUG_AREA=9011 )

include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}/parser
)

add_subdirectory(app_templates)
add_subdirectory(parser)
add_subdirectory(duchain)
add_subdirectory(codecompletion)
add_subdirectory(python-src)
add_subdirectory(codegen)

set(kdevpythonlanguagesupport_PART_SRCS
    codegen/simplerefactoring.cpp
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

install(TARGETS kdevpythonlanguagesupport DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kdevpythonsupport.desktop DESTINATION ${SERVICES_INSTALL_DIR})

install(DIRECTORY documentation_files DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport)
install(DIRECTORY python-src/Lib/encodings DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport/encodings)

