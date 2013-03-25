set(kcm_pep8_SRCS
    kcm_pep8.cpp
)

kde4_add_plugin(kcm_pep8 ${kcm_pep8_SRCS})

target_link_libraries(kcm_pep8
    ${KDE4_KIO_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${KDEVPLATFORM_PROJECT_LIBRARIES}
    ${KDEVPLATFORM_UTIL_LIBRARIES}
    ${KDE4_KNEWSTUFF3_LIBS}
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
)

install(TARGETS kcm_pep8
         DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kcm_kdevpythonpep8.desktop
        DESTINATION ${SERVICES_INSTALL_DIR})
