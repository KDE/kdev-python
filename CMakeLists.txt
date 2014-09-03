PROJECT(kdevpython)

# write the plugin version to a file
set(KDEVPYTHON_VERSION_MAJOR 1)
set(KDEVPYTHON_VERSION_MINOR 90)
set(KDEVPYTHON_VERSION_PATCH 90)
# KDevplatform dependency version
set( KDEVPLATFORM_VERSION "${KDEVPYTHON_VERSION_MAJOR}.${KDEVPYTHON_VERSION_MINOR}.${KDEVPYTHON_VERSION_PATCH}" )

find_package(ECM 0.0.9 REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${kdevpython_SOURCE_DIR}/cmake/modules ${ECM_MODULE_PATH})
#set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH})

set(REQUIRED QT_VERSION 5.2.0)

cmake_minimum_required(VERSION 2.8.12)

include(CMakePackageConfigHelpers)

include(ECMAddTests)
include(ECMOptionalAddSubdirectory)
include(ECMSetupVersion)

include(KDEInstallDirs)
include(KDECMakeSettings)
include(KDECompilerSettings)

find_package(Qt5 ${QT_MIN_VERSION} CONFIG REQUIRED Widgets Test WebKitWidgets)
find_package(KF5 REQUIRED I18n NewStuff ItemModels ThreadWeaver KDELibs4Support TextEditor)
find_package(KDevPlatform ${KDEVPLATFORM_VERSION} REQUIRED)


# find the system python 3 interpreter, only used for determining search paths.
find_package(PythonInterp 3.0 REQUIRED)
configure_file( "${kdevpython_SOURCE_DIR}/kdevpythonversion.h.cmake" "${kdevpython_BINARY_DIR}/kdevpythonversion.h" @ONLY )


enable_testing()

if ( NOT WIN32 )
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wfatal-errors -Wall")
endif ( NOT WIN32 )

# then, build the plugin
include_directories(
    ${KDEVPLATFORM_INCLUDE_DIR}
    
#    ${KDE4_INCLUDE_DIR}/threadweaver
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/duchain
    ${CMAKE_CURRENT_SOURCE_DIR}/parser
    ${CMAKE_CURRENT_BINARY_DIR}/parser
    ${KDEVELOP_INCLUDE_DIR}
)


add_definitions( -DKDE_DEFAULT_DEBUG_AREA=9011 )

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID STREQUAL "Clang" OR CMAKE_CXX_COMPILER_ID STREQUAL "Intel")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
endif()

include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}/parser
)

add_subdirectory(app_templates)
add_subdirectory(parser)
add_subdirectory(duchain)
add_subdirectory(codecompletion)
add_subdirectory(debugger)
add_subdirectory(docfilekcm)
add_subdirectory(pep8kcm)
add_subdirectory(checks)

set(kdevpythonlanguagesupport_PART_SRCS
    codegen/correctionfilegenerator.cpp
    codegen/refactoring.cpp
    pythonlanguagesupport.cpp
    pythonparsejob.cpp
    pythonhighlighting.cpp

    checks/basiccheck.cpp
    checks/controlflowgraphbuilder.cpp
    checks/dataaccessvisitor.cpp
)

ki18n_wrap_ui(kdevpythonlanguagesupport_PART_SRCS codegen/correctionwidget.ui)

add_library(kdevpythonlanguagesupport MODULE ${kdevpythonlanguagesupport_PART_SRCS})

target_link_libraries(kdevpythonlanguagesupport
    
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    KF5::ThreadWeaver
    KF5::TextEditor
    kdev4pythoncompletion
    kdev4pythonparser
    kdev4pythonduchain
)

install(TARGETS kdevpythonlanguagesupport DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kdevpythonsupport.desktop DESTINATION ${SERVICES_INSTALL_DIR})

install(DIRECTORY documentation_files DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport)
install(DIRECTORY correction_files DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport)
