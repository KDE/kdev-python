cmake_minimum_required(VERSION 3.0)
project(kdevpython)

# write the plugin version to a file
set(KDEVPYTHON_VERSION_MAJOR 5)
set(KDEVPYTHON_VERSION_MINOR 3)
set(KDEVPYTHON_VERSION_PATCH 40)

# KDevplatform dependency version
set( KDEVPLATFORM_VERSION "${KDEVPYTHON_VERSION_MAJOR}.${KDEVPYTHON_VERSION_MINOR}" )

find_package (ECM "5.14.0" REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${kdevpython_SOURCE_DIR}/cmake/modules ${CMAKE_MODULE_PATH} ${ECM_MODULE_PATH})

include(KDECompilerSettings NO_POLICY_SCOPE)
include(KDEInstallDirs)
include(KDECMakeSettings)

include(GenerateExportHeader)

include(ECMAddTests)
include(ECMSetupVersion)
include(ECMQtDeclareLoggingCategory)

if(NOT CMAKE_VERSION VERSION_LESS "3.10.0")
    # Avoids bogus warnings with CMake 3.10+
    list(APPEND CMAKE_AUTOMOC_MACRO_NAMES "K_PLUGIN_FACTORY_WITH_JSON")
endif()
if(POLICY CMP0071)
    # Avoids compat messages from CMake 3.10+, with Qt < 5.9.4
    # See https://bugreports.qt.io/browse/QTBUG-63442
    cmake_policy(SET CMP0071 OLD)
endif()

if (CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wdocumentation")
endif()

add_definitions( -DTRANSLATION_DOMAIN=\"kdevpython\" )

# CMake looks for exactly the specified version first and ignores newer versions.
# To avoid that, start looking for the newest supported version and work down.
set(Python_ADDITIONAL_VERSIONS 3.6 3.5 3.4)
foreach(_PYTHON_V ${Python_ADDITIONAL_VERSIONS})
    find_package(PythonInterp ${_PYTHON_V})
    if ( PYTHONINTERP_FOUND )
        break()
    endif()
endforeach()
# Must unset before searching for libs, otherwise these are checked before the required version...
unset(Python_ADDITIONAL_VERSIONS)

if ( PYTHONINTERP_FOUND AND PYTHON_VERSION_STRING VERSION_GREATER "3.4" )
    # Find libraries that match the found interpreter (mismatched versions not supported).
    # This assumes libs are available for the newest Python version on the system.
    # KDevelop should _always_ be built against the newest possible version, so notabug.
    find_package(PythonLibs "${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}" REQUIRED EXACT)
endif()

if ( NOT PYTHONLIBS_FOUND OR PYTHONLIBS_VERSION_STRING VERSION_LESS "3.4.3" )
    message(FATAL_ERROR "Python >= 3.4.3 but < 3.7 with --enable-shared is required to build kdev-python")
endif()

configure_file(kdevpythonversion.h.cmake "${CMAKE_CURRENT_BINARY_DIR}/kdevpythonversion.h" @ONLY)

set(QT_MIN_VERSION "5.5.0")
find_package(Qt5 ${QT_MIN_VERSION} CONFIG REQUIRED Core Widgets Test)
set(KF5_DEP_VERSION "5.15.0")
find_package(KF5 ${KF5_DEP_VERSION} REQUIRED
    I18n
    ThreadWeaver
    TextEditor
)
find_package(KDevPlatform ${KDEVPLATFORM_VERSION} CONFIG REQUIRED)
find_package(KDevelop ${KDEVPLATFORM_VERSION} REQUIRED)

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
    CATEGORY_NAME "kdevelop.languages.python.codegen"
)
ecm_qt_declare_logging_category(kdevpythonlanguagesupport_PART_SRCS
    HEADER pythondebug.h
    IDENTIFIER KDEV_PYTHON
    CATEGORY_NAME "kdevelop.languages.python"
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
    KF5::ThreadWeaver
    KF5::TextEditor
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
install(FILES kdevpythonsupport.categories DESTINATION ${KDE_INSTALL_CONFDIR})

feature_summary(WHAT ALL FATAL_ON_MISSING_REQUIRED_PACKAGES)
