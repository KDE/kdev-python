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

add_library(kdevpythoncompletion SHARED ${completion_SRCS})

generate_export_header(kdevpythoncompletion EXPORT_MACRO_NAME KDEVPYTHONCOMPLETION_EXPORT
                                             EXPORT_FILE_NAME pythoncompletionexport.h
)

add_dependencies(kdevpythoncompletion
    kdevpythonparser 
    kdevpythonduchain
)

target_link_libraries(kdevpythoncompletion LINK_PRIVATE
    KDev::Language
    KDev::Interfaces
    KDev::Project
    kdevpythonduchain
    kdevpythonparser
)

install(TARGETS kdevpythoncompletion DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

add_subdirectory(tests)
