set(kcm_pep8_SRCS
    kcm_pep8.cpp
)

add_library(kcm_pep8 MODULE ${kcm_pep8_SRCS})

target_link_libraries(kcm_pep8
    KF5::KIOCore
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
    ${KDEVPLATFORM_PROJECT_LIBRARIES}
    ${KDEVPLATFORM_UTIL_LIBRARIES}
    KF5::NewStuff
    ${KDEVPLATFORM_INTERFACES_LIBRARIES}
)

install(TARGETS kcm_pep8
         DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kcm_kdevpythonpep8.desktop
        DESTINATION ${SERVICES_INSTALL_DIR})
