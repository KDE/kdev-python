cmake_minimum_required(VERSION 2.8.12)

project(kdevpython)

# write the plugin version to a file
set(KDEVPYTHON_VERSION_MAJOR 5)
set(KDEVPYTHON_VERSION_MINOR 0)
set(KDEVPYTHON_VERSION_PATCH 80)

# KDevplatform dependency version
set( KDEVPLATFORM_VERSION "${KDEVPYTHON_VERSION_MAJOR}.${KDEVPYTHON_VERSION_MINOR}" )

find_package(ECM 0.0.9 REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${kdevpython_SOURCE_DIR}/cmake/modules ${CMAKE_MODULE_PATH} ${ECM_MODULE_PATH})

set(REQUIRED QT_VERSION 5.2.0)

include(KDECompilerSettings NO_POLICY_SCOPE)
include(GenerateExportHeader)
include(CMakePackageConfigHelpers)

include(ECMAddTests)
include(ECMOptionalAddSubdirectory)
include(ECMSetupVersion)

include(KDEInstallDirs)

include(KDECMakeSettings)

add_definitions( -DTRANSLATION_DOMAIN=\"kdevpython\" )

# find the system python 3 interpreter, only used for determining search paths.
# must be called before find_package(KF5) because it searchs for python too, but finds python2
set(Python_ADDITIONAL_VERSIONS 3.6 3.5)
find_package(PythonInterp 3.5 REQUIRED)
find_package(PythonLibs 3.5 REQUIRED)
configure_file( "${kdevpython_SOURCE_DIR}/kdevpythonversion.h.cmake" "${kdevpython_BINARY_DIR}/kdevpythonversion.h" @ONLY )
if ( (NOT PYTHON_LIBRARIES) OR "${PYTHON_VERSION_MINOR}" GREATER 6 )
    message(FATAL_ERROR "Python >= 3.5.0 but < 3.7 with --enable-shared is required to build kdev-python")
endif()

find_package(Qt5 ${QT_MIN_VERSION} CONFIG REQUIRED Widgets Test)
find_package(KF5 REQUIRED I18n NewStuff ItemModels ThreadWeaver TextEditor KCMUtils)
find_package(KDevPlatform ${KDEVPLATFORM_VERSION} REQUIRED)
find_package(KDevelop ${KDEVPLATFORM_VERSION} REQUIRED)

enable_testing()

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
    codegen/codegendebug.cpp
    pythonlanguagesupport.cpp
    pythonparsejob.cpp
    pythonhighlighting.cpp
    pythondebug.cpp
    pythonstylechecking.cpp

    # config pages:
    docfilekcm/docfilewizard.cpp
    docfilekcm/docfilemanagerwidget.cpp
    docfilekcm/kcm_docfiles.cpp
    pep8kcm/kcm_pep8.cpp
    projectconfig/projectconfigpage.cpp
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
    KF5::NewStuff
    kdevpythoncompletion
    kdevpythonparser
    kdevpythonduchain
)

get_target_property(DEFINESANDINCLUDES_INCLUDE_DIRS KDev::DefinesAndIncludesManager INTERFACE_INCLUDE_DIRECTORIES)
include_directories(${DEFINESANDINCLUDES_INCLUDE_DIRS})

install(DIRECTORY documentation_files DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport)
install(DIRECTORY correction_files DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport)
install(FILES codestyle.py DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport)

feature_summary(WHAT ALL FATAL_ON_MISSING_REQUIRED_PACKAGES)
