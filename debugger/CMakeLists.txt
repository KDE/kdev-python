project(pdb)

include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${KDEVPLATFORM_INCLUDE_DIR}
    ${KDEVELOP_INCLUDE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}  ${KDE4_ENABLE_EXCEPTIONS}")

set(kdevpdb_PART_SRCS
    breakpointcontroller.cpp
    variable.cpp
    variablecontroller.cpp
    pdbframestackmodel.cpp
    pdblauncher.cpp
    debugjob.cpp
    debugsession.cpp
    pdbdebuggerplugin.cpp
)

kde4_add_plugin(kdevpdb ${kdevpdb_PART_SRCS})
target_link_libraries(kdevpdb sublime
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${KDEVPLATFORM_DEBUGGER_LIBRARIES}
    ${KDEVPLATFORM_OUTPUTVIEW_LIBRARIES}
    ${KDEVPLATFORM_PROJECT_LIBRARIES}
    ${KDE4_KDEUI_LIBS}
    ${KDEVPLATFORM_UTIL_LIBRARIES}
    ${KDE4_KTEXTEDITOR_LIBS}
    ${KDE4WORKSPACE_PROCESSUI_LIBS}
)

install(TARGETS kdevpdb DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kdevpdb.desktop DESTINATION ${SERVICES_INSTALL_DIR})
