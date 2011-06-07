add_custom_target(
    generate_python ALL
#     OUTPUT libkdevpythonparser.so.1.0 libkdevpythonparser.so
    COMMAND /bin/bash ${CMAKE_CURRENT_SOURCE_DIR}/configure --enable-shared --without-pymalloc WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMAND /usr/bin/env make -C ${CMAKE_CURRENT_SOURCE_DIR}
    COMMAND mv ${CMAKE_CURRENT_SOURCE_DIR}/libpython2.7.so ${CMAKE_CURRENT_SOURCE_DIR}/libkdevpythonparser.so
    COMMAND mv ${CMAKE_CURRENT_SOURCE_DIR}/libpython2.7.so.1.0 ${CMAKE_CURRENT_SOURCE_DIR}/libkdevpythonparser.so.1.0
)

install(FILES libkdevpythonparser.so DESTINATION ${LIB_INSTALL_DIR})
install(FILES libkdevpythonparser.so.1.0 DESTINATION ${LIB_INSTALL_DIR})

