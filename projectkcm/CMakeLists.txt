set( pythonprojectkcm_SRCS
    pythonprojectkcm.cpp
)

kde4_add_kcfg_files( pythonprojectkcm_SRCS pythonprojectsettings.kcfgc )
kde4_add_plugin( kcm_kdevpythonproject ${pythonprojectkcm_SRCS} )

include_directories( ${CMAKE_CURRENT_BINARY_DIR} )

target_link_libraries( kcm_kdevpythonproject
    ${KDE4_KCMUTILS_LIBS}
    ${KDE4_KDEUI_LIBS}
    ${KDEVPLATFORM_PROJECT_LIBRARIES}
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    ${KDEVPLATFORM_UTIL_LIBRARIES}
)

install( TARGETS kcm_kdevpythonproject DESTINATION ${PLUGIN_INSTALL_DIR} )
install( FILES kcm_kdevpythonproject.desktop DESTINATION ${SERVICES_INSTALL_DIR} )
