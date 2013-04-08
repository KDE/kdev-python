PROJECT(kdevpython)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${kdevpython_SOURCE_DIR}/cmake/)

# this must go uninterfered with all the include_directories, so have it before
# finding even KDE # TODO what?
find_package(KDE4 REQUIRED)
find_package(KDevPlatform 1.5.60 REQUIRED)
find_package(KDevelop-PG-Qt REQUIRED)

# write the plugin version to a file
set(KDEVPYTHON_VERSION_MAJOR 1)
set(KDEVPYTHON_VERSION_MINOR 5)
set(KDEVPYTHON_VERSION_PATCH 60)
configure_file( "${kdevpython_SOURCE_DIR}/kdevpythonversion.h.cmake" "${kdevpython_BINARY_DIR}/kdevpythonversion.h" @ONLY )

cmake_minimum_required(VERSION 2.8)

enable_testing()

if ( NOT WIN32 )
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wfatal-errors -Wall")
endif ( NOT WIN32 )

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
add_subdirectory(debugger)
add_subdirectory(codegen)
add_subdirectory(docfilekcm)
add_subdirectory(pep8kcm)

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
