
#To properly find kdevelop-pg add -DKDEVPG_DATA_DIR=<kdevpg-install-path>/share to the
#cmake run if you installed it in a different directory than this plugin
#TODO: a cmake run is needed after changing one of the CMakeLists.txt, make will
#complain about the FindKDevelop-PG.cmake file not findable.
find_package(KDE4 REQUIRED)

find_package(KDevPlatform REQUIRED)

INCLUDE_DIRECTORIES(
    ${KDEVPLATFORM_INCLUDE_DIR}/language/interfaces
    ${KDEVPLATFORM_INCLUDE_DIR}/interfaces
    ${KDEVPLATFORM_INCLUDE_DIR}/language
    ${KDEVPLATFORM_INCLUDE_DIR}/editor
    ${KDEVPLATFORM_INCLUDE_DIR}/language/backgroundparser
    ${KDE4_INCLUDES}
    ${KDE4_INCLUDE_DIR}/threadweaver
    ${CMAKE_CURRENT_BINARY_DIR}
    ${KDEVPLATFORM_INCLUDE_DIR}/language/duchain
    ${CMAKE_SOURCE_DIR}/duchain
    ${CMAKE_SOURCE_DIR}/parser
)

#Don't error out if the FindXXX are missing for these two
find_package(KDevelop-PG QUIET)
find_package(Flex QUIET)

if(KDEVPG_FOUND AND FLEX_FOUND)
    include_directories(
        ${CMAKE_BINARY_DIR}/parser
        ${KDEVPG_INCLUDE_DIR}
    )
else(KDEVPG_FOUND AND FLEX_FOUND)
    include_directories(
        ${CMAKE_SOURCE_DIR}/parser/generated
        ${CMAKE_SOURCE_DIR}/parser/generated/kdevelop-pg
    )
endif(KDEVPG_FOUND AND FLEX_FOUND)


add_subdirectory(parser)
add_subdirectory(duchain)

set(kdevpythonlanguagesupport_PART_SRCS
    pythonlanguagesupport.cpp
    pythonparsejob.cpp
    pythonhighlighting.cpp
)

kde4_add_plugin(kdevpythonlanguagesupport ${kdevpythonlanguagesupport_PART_SRCS})

target_link_libraries(kdevpythonlanguagesupport
    ${KDE4_KDEUI_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARY}
    ${KDEVPLATFORM_LANGUAGE_LIBRARY}
    ${KDE4_THREADWEAVER_LIBRARIES}
    ${KDEVPLATFORM_EDITOR_LIBRARY}
    ${KDE4_KTEXTEDITOR_LIBS}
    kdev4pythonparser
    kdev4pythonduchain
)

install(TARGETS kdevpythonlanguagesupport DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kdevpythonsupport.desktop DESTINATION ${SERVICES_INSTALL_DIR})



