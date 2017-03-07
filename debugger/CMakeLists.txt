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
)

install(FILES __kdevpython_debugger_utils.py DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport/debugger)
install(FILES kdevpdb.py DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport/debugger)
