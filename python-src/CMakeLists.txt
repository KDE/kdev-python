add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/libpython2.7-kdevelop.so
    COMMAND /bin/bash ${CMAKE_CURRENT_SOURCE_DIR}/configure --enable-shared --without-pymalloc WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    COMMAND /usr/bin/env make -C ${CMAKE_CURRENT_BINARY_DIR}
)

add_custom_target(
    parser
    COMMAND cmake -E echo
    DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/libpython2.7-kdevelop.so
)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/libpython2.7-kdevelop.so.1.0 DESTINATION ${LIB_INSTALL_DIR})

