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
    debuggerdebug.cpp
)

kdevplatform_add_plugin(kdevpdb JSON kdevpdb.json SOURCES ${kdevpdb_PART_SRCS})

generate_export_header(kdevpdb EXPORT_MACRO_NAME KDEVPYTHONDEBUG_EXPORT)

target_link_libraries(kdevpdb
    kdevpythonparser
    KDev::Interfaces
    KDev::Language
    KDev::Debugger
    KDev::OutputView
    KDev::Project    
    KDev::Util
    KF5::TextEditor
    ${KDE4WORKSPACE_PROCESSUI_LIBS}
)

install(FILES __kdevpython_debugger_utils.py DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport/debugger)
install(FILES kdevpdb.py DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport/debugger)
