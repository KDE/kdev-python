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

add_library(kdevpdb MODULE ${kdevpdb_PART_SRCS})
target_link_libraries(kdevpdb
    sublime
    kdev4pythonparser
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${KDEVPLATFORM_DEBUGGER_LIBRARIES}
    ${KDEVPLATFORM_OUTPUTVIEW_LIBRARIES}
    ${KDEVPLATFORM_PROJECT_LIBRARIES}
    
    ${KDEVPLATFORM_UTIL_LIBRARIES}
    KF5::TextEditor
    ${KDE4WORKSPACE_PROCESSUI_LIBS}
)

install(TARGETS kdevpdb DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kdevpdb.desktop DESTINATION ${SERVICES_INSTALL_DIR})

install(FILES __kdevpython_debugger_utils.py DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport/debugger)
install(FILES kdevpdb.py DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport/debugger)
