PROJECT(kdevpython)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${kdevpython_SOURCE_DIR}/cmake/)
#To properly find kdevelop-pg add -DKDEVPG_DATA_DIR=<kdevpg-install-path>/share to the
#cmake run if you installed it in a different directory than this plugin
#TODO: a cmake run is needed after changing one of the CMakeLists.txt, make will
#complain about the FindKDevelop-PG.cmake file not findable.
find_package(KDE4 REQUIRED)

find_package(KDevPlatform 1.0.0 REQUIRED)

include_directories(
    ${KDEVPLATFORM_INCLUDE_DIR}
    ${KDE4_INCLUDES}
    ${KDE4_INCLUDE_DIR}/threadweaver
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/duchain
    ${CMAKE_CURRENT_SOURCE_DIR}/parser
    ${CMAKE_CURRENT_BINARY_DIR}/parser
)

add_definitions( -DKDE_DEFAULT_DEBUG_AREA=9011 )

find_package(KDevelop-PG-Qt REQUIRED)
include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}/parser
    ${KDEVPGQT_INCLUDE_DIR}
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
    kdev4pythonparser
    kdev4pythonduchain
    kdev4pythoncompletion
)

install(TARGETS kdevpythonlanguagesupport DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kdevpythonsupport.desktop DESTINATION ${SERVICES_INSTALL_DIR})
