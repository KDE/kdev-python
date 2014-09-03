
include_directories(${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    )

set(duchain_SRCS
    declarations/functiondeclaration.cpp
    declarations/classdeclaration.cpp

    types/hintedtype.cpp
    types/unsuretype.cpp
    types/indexedcontainer.cpp

    expressionvisitor.cpp
    helpers.cpp
    pythonducontext.cpp
    contextbuilder.cpp
    pythoneditorintegrator.cpp
    declarationbuilder.cpp
    usebuilder.cpp
    dumpchain.cpp

    navigation/navigationwidget.cpp
    navigation/declarationnavigationcontext.cpp

    correctionhelper.cpp

    assistants/missingincludeassistant.cpp
    ../docfilekcm/docfilewizard.cpp # for the docfile generation assistant widget, to be used in the problem resolver
)


add_library( kdev4pythonduchain SHARED ${duchain_SRCS} )
target_link_libraries( kdev4pythonduchain LINK_PRIVATE
    KF5::KDELibs4Support
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${KDEVPLATFORM_PROJECT_LIBRARIES}
    KF5::TextEditor
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    Qt5::WebKitWidgets
    kdev4pythonparser
 )

install(TARGETS kdev4pythonduchain DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})


add_subdirectory(navigation)

add_subdirectory(tests)

add_subdirectory(types)
add_subdirectory(declarations)

add_subdirectory(assistants)
