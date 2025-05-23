cmake_minimum_required(VERSION 3.19)

# KDE Gear version, managed by release service script
set(RELEASE_SERVICE_VERSION_MAJOR "25")
set(RELEASE_SERVICE_VERSION_MINOR "07")
set(RELEASE_SERVICE_VERSION_MICRO "70")

# generate patch level from release service version
set(_micro ${RELEASE_SERVICE_VERSION_MICRO})
if (_micro LESS "10")
    string(PREPEND _micro "0") # pad with 0
endif()
set(RELEASE_SERVICE_BASED_PATCHLEVEL "${RELEASE_SERVICE_VERSION_MAJOR}${RELEASE_SERVICE_VERSION_MINOR}${_micro}")

project(kdevpython VERSION "6.0.${RELEASE_SERVICE_BASED_PATCHLEVEL}")

# KDevplatform dependency version
set(KDEVPLATFORM_VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}")

set(KDE_COMPILERSETTINGS_LEVEL 6.0)
set(QT_MIN_VERSION "6.5.0")
set(KF_MIN_VERSION "6.0.0")

find_package(ECM ${KF_MIN_VERSION} REQUIRED)
set(CMAKE_MODULE_PATH ${kdevpython_SOURCE_DIR}/cmake/modules ${CMAKE_MODULE_PATH} ${ECM_MODULE_PATH})

include(KDEInstallDirs)
include(KDECMakeSettings)
include(KDECompilerSettings NO_POLICY_SCOPE)

include(GenerateExportHeader)

include(ECMAddTests)
include(ECMSetupVersion)
include(ECMQtDeclareLoggingCategory)

if (CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wdocumentation")
endif()

add_definitions( -DTRANSLATION_DOMAIN=\"kdevpython\" )

set(Python3_USE_STATIC_LIBS FALSE)
set(Python3_FIND_STRATEGY VERSION)
find_package(Python3 3.4.3...<3.14 COMPONENTS Interpreter Development REQUIRED)

configure_file(kdevpythonversion.h.cmake "${CMAKE_CURRENT_BINARY_DIR}/kdevpythonversion.h" @ONLY)

find_package(KDevPlatform ${KDEVPLATFORM_VERSION} REQUIRED)
find_package(KDevelop ${KDEVPLATFORM_VERSION} REQUIRED)

find_package(Qt6 ${QT_MIN_VERSION} REQUIRED COMPONENTS
    Core
    Core5Compat
    Widgets
    Test
)

find_package(KF6 ${KF_MIN_VERSION} REQUIRED COMPONENTS
    Config
    CoreAddons
    I18n
    Parts
    Service
    TextEditor
    ThreadWeaver
    WidgetsAddons
    XmlGui
)

if ( NOT WIN32 )
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wfatal-errors -Wall")
endif ( NOT WIN32 )

# then, build the plugin
include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/duchain
    ${CMAKE_CURRENT_SOURCE_DIR}/parser
    ${CMAKE_CURRENT_BINARY_DIR}/parser
)

add_subdirectory(app_templates)
add_subdirectory(parser)
add_subdirectory(duchain)
add_subdirectory(codecompletion)
add_subdirectory(debugger)
add_subdirectory(docfilekcm)

set(kdevpythonlanguagesupport_PART_SRCS
    codegen/correctionfilegenerator.cpp
    codegen/refactoring.cpp
    pythonlanguagesupport.cpp
    pythonparsejob.cpp
    pythonhighlighting.cpp
    pythonstylechecking.cpp

    # config pages:
    docfilekcm/docfilewizard.cpp
    docfilekcm/docfilemanagerwidget.cpp
    docfilekcm/kcm_docfiles.cpp
    pep8kcm/kcm_pep8.cpp
    projectconfig/projectconfigpage.cpp
)
ecm_qt_declare_logging_category(kdevpythonlanguagesupport_PART_SRCS
    HEADER codegendebug.h
    IDENTIFIER KDEV_PYTHON_CODEGEN
    CATEGORY_NAME "kdevelop.plugins.python.codegen"
    DESCRIPTION "KDevelop plugin: Python language support - codegen"
    EXPORT KDEVPYTHON
)
ecm_qt_declare_logging_category(kdevpythonlanguagesupport_PART_SRCS
    HEADER pythondebug.h
    IDENTIFIER KDEV_PYTHON
    CATEGORY_NAME "kdevelop.plugins.python"
    DESCRIPTION "KDevelop plugin: Python language support"
    EXPORT KDEVPYTHON
)

ki18n_wrap_ui(kdevpythonlanguagesupport_PART_SRCS
    codegen/correctionwidget.ui
    projectconfig/projectconfig.ui
    pep8kcm/pep8.ui
)

kdevplatform_add_plugin(kdevpythonlanguagesupport JSON kdevpythonsupport.json SOURCES ${kdevpythonlanguagesupport_PART_SRCS})

target_link_libraries(kdevpythonlanguagesupport
    KDev::Interfaces
    KDev::Language
    KDev::Util
    KF6::Service
    KF6::ThreadWeaver
    KF6::TextEditor
    kdevpythoncompletion
    kdevpythonparser
    kdevpythonduchain
)

get_target_property(DEFINESANDINCLUDES_INCLUDE_DIRS KDev::DefinesAndIncludesManager INTERFACE_INCLUDE_DIRECTORIES)
include_directories(${DEFINESANDINCLUDES_INCLUDE_DIRS})

install(DIRECTORY documentation_files DESTINATION ${KDE_INSTALL_DATADIR}/kdevpythonsupport)
install(DIRECTORY correction_files DESTINATION ${KDE_INSTALL_DATADIR}/kdevpythonsupport)
install(FILES codestyle.py DESTINATION ${KDE_INSTALL_DATADIR}/kdevpythonsupport)

install(FILES org.kde.kdev-python.metainfo.xml DESTINATION ${KDE_INSTALL_METAINFODIR})

# kdebugsettings file
ecm_qt_install_logging_categories(
    EXPORT KDEVPYTHON
    FILE kdevpythonsupport.categories
    DESTINATION ${KDE_INSTALL_LOGGINGCATEGORIESDIR}
)

ki18n_install(po)

feature_summary(WHAT ALL FATAL_ON_MISSING_REQUIRED_PACKAGES)
