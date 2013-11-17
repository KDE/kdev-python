
include_directories(${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    )

set(duchain_SRCS
    declarations/functiondeclaration.cpp
    declarations/classdeclaration.cpp

    types/variablelengthcontainer.cpp
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


kde4_add_library( kdev4pythonduchain SHARED ${duchain_SRCS} )
target_link_libraries( kdev4pythonduchain
    ${KDE4_KDECORE_LIBS}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${KDEVPLATFORM_PROJECT_LIBRARIES}
    ${KDE4_KTEXTEDITOR_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    ${QT_QTWEBKIT_LIBRARY}
    kdev4pythonparser
 )

install(TARGETS kdev4pythonduchain DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})


add_subdirectory(navigation)

add_subdirectory(tests)

add_subdirectory(types)
add_subdirectory(declarations)

add_subdirectory(assistants)
