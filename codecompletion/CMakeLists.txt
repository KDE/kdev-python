include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

set(completion_SRCS
    context.cpp 
    model.cpp
    worker.cpp
    helpers.cpp
    codecompletiondebug.cpp
    
    items/missingincludeitem.cpp
    items/declaration.cpp
    items/functiondeclaration.cpp
    items/implementfunction.cpp
    items/importfile.cpp
    items/keyword.cpp
    items/replacementvariable.cpp
)

add_library(kdev4pythoncompletion SHARED ${completion_SRCS})

generate_export_header(kdev4pythoncompletion EXPORT_MACRO_NAME KDEVPYTHONCOMPLETION_EXPORT
                                             EXPORT_FILE_NAME pythoncompletionexport.h
)

add_dependencies(kdev4pythoncompletion
    kdev4pythonparser 
    kdev4pythonduchain
)

target_link_libraries(kdev4pythoncompletion LINK_PRIVATE
    KF5::KDELibs4Support
    KDev::Language
    KDev::Interfaces
    KDev::Project
    kdev4pythonduchain
    kdev4pythonparser
)

install(TARGETS kdev4pythoncompletion DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

add_subdirectory(tests)
