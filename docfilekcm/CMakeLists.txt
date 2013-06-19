set(kcm_docfiles_SRCS
    docfilewizard.cpp
    docfilemanagerwidget.cpp
    kcm_docfiles.cpp
)

kde4_add_plugin(kcm_docfiles ${kcm_docfiles_SRCS})

target_link_libraries(kcm_docfiles
    ${KDE4_KIO_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${KDEVPLATFORM_PROJECT_LIBRARIES}
    ${KDEVPLATFORM_UTIL_LIBRARIES}
    ${KDE4_KNEWSTUFF3_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
)

install(TARGETS kcm_docfiles
        DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kcm_kdevpythondocfiles.desktop
        DESTINATION ${SERVICES_INSTALL_DIR})

install(FILES kdev_python_docfiles.knsrc
        DESTINATION ${CONFIG_INSTALL_DIR})

install(FILES ../documentation_src/introspection/introspect.py
        DESTINATION ${DATA_INSTALL_DIR}/kdevpythonsupport/scripts)