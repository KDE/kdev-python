add_custom_target(
    parser
    COMMAND /bin/bash ${CMAKE_CURRENT_SOURCE_DIR}/configure --enable-shared --without-pymalloc WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMAND /usr/bin/env make -C ${CMAKE_CURRENT_SOURCE_DIR}
)

install(FILES libpython2.7-kdevelop.so DESTINATION ${LIB_INSTALL_DIR})
install(FILES libpython2.7-kdevelop.so.1.0 DESTINATION ${LIB_INSTALL_DIR})

