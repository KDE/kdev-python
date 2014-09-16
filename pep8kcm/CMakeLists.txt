set(kcm_pep8_SRCS
    kcm_pep8.cpp
)

add_library(kcm_pep8 MODULE ${kcm_pep8_SRCS})

target_link_libraries(kcm_pep8
    KF5::KIOCore
    KDev::Interfaces
    KDev::Language
    KDev::Project
    KDev::Util
    KF5::NewStuff
    KF5::KCMUtils
)

install(TARGETS kcm_pep8
         DESTINATION ${PLUGIN_INSTALL_DIR})

install(FILES kcm_kdevpythonpep8.desktop
        DESTINATION ${SERVICES_INSTALL_DIR})
