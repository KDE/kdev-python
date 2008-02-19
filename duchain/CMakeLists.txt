
include_directories(${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    )

set(duchain_SRCS
    contextbuilder.cpp
    pythoneditorintegrator.cpp
    declarationbuilder.cpp
#     usebuilder.cpp
    dumpchain.cpp
#     typebuilder.cpp
    )


kde4_add_library( kdev4pythonduchain SHARED ${duchain_SRCS} )
target_link_libraries( kdev4pythonduchain
    ${KDE4_KDECORE_LIBS}
    ${KDEVPLATFORM_LANGUAGE_LIBRARY}
    ${KDEVPLATFORM_EDITOR_LIBRARY}
    ${KDE4_KTEXTEDITOR_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARY}
    kdev4pythonparser
 )

install(TARGETS kdev4pythonduchain DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})

