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
ecm_qt_declare_logging_category(kdevpdb_PART_SRCS
    HEADER debuggerdebug.h
    IDENTIFIER KDEV_PYTHON_DEBUGGER
    CATEGORY_NAME "kdevelop.plugins.python.debugger"
    DESCRIPTION "KDevelop plugin: Python language support - debugger"
    EXPORT KDEVPYTHON
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
    KF${KF_MAJOR_VERSION}::TextEditor
)

install(FILES __kdevpython_debugger_utils.py DESTINATION ${KDE_INSTALL_DATADIR}/kdevpythonsupport/debugger)
install(FILES kdevpdb.py DESTINATION ${KDE_INSTALL_DATADIR}/kdevpythonsupport/debugger)
