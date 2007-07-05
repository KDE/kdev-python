
#To properly find kdevelop-pg add -DKDEVPG_DATA_DIR=<kdevpg-install-path>/share to the
#cmake run if you installed it in a different directory than this plugin
#TODO: a cmake run is needed after changing one of the CMakeLists.txt, make will
#complain about the FindKDevelop-PG.cmake file not findable.
if( KDEVPG_DATA_DIR )
    set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${KDEVPG_DATA_DIR}/cmake/modules )
else( KDEVPG_DATA_DIR )
    set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_INSTALL_PREFIX}/share/cmake/modules )
endif( KDEVPG_DATA_DIR )

find_package(KDE4 REQUIRED)
find_package(KDevPlatform REQUIRED)

find_package(KDevelop-PG)
find_package(Flex)

add_subdirectory(parser)

INCLUDE_DIRECTORIES(
    ${KDEVPLATFORM_INCLUDE_DIR}/language/interfaces
    ${KDEVPLATFORM_INCLUDE_DIR}/interfaces
    ${KDEVPLATFORM_INCLUDE_DIR}/language
    ${KDEVPLATFORM_INCLUDE_DIR}/language/backgroundparser
    ${KDE4_INCLUDES}
    ${KDE4_INCLUDE_DIR}/threadweaver
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_SOURCE_DIR}/parser
)

if(KDEVPG_FOUND)
    include_directorieS(${CMAKE_CURRENT_BINARY_DIR}/parser
        ${KDEVPG_INCLUDE_DIR}
    )
else(KDEVPG_FOUND)
    include_directories(${CMAKE_SOURCE_DIR}/parser/generated)
endif(KDEVPG_FOUND)


set(kdevpythonlanguagesupport_PART_SRCS
    pythonlanguagesupport.cpp
    pythonparsejob.cpp
    parser/parsesession.cpp
)

kde4_automoc(${kdevpythonlanguagesupport_PART_SRCS})

kde4_add_plugin(kdevpythonlanguagesupport ${kdevpythonlanguagesupport_PART_SRCS})

target_link_libraries(kdevpythonlanguagesupport
    ${KDE4_KDEUI_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARY}
    ${KDEVPLATFORM_LANGUAGE_LIBRARY}
    ${KDE4_THREADWEAVER_LIBRARIES}
    kdevpythonparser
)

install(TARGETS kdevpythonlanguagesupport DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kdevpythonsupport.desktop DESTINATION ${SERVICES_INSTALL_DIR})

