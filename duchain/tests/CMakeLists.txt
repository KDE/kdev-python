automoc4(pyduchaintest waitforupdate.cpp)
kde4_add_unit_test(pyduchaintest pyduchaintest.cpp)
kde4_add_unit_test(duchainbench duchainbench.cpp)

add_definitions(-DDUCHAIN_PY_DATA_DIR="${CMAKE_CURRENT_SOURCE_DIR}")

target_link_libraries(pyduchaintest
    kdev4pythonduchain
    kdev4pythonparser
    ${kdev4pythonparser_LIBRARIES}
    ${QT_QTTEST_LIBRARY}
    ${KDEVPLATFORM_TESTS_LIBRARIES}
)

target_link_libraries(duchainbench
    kdev4pythonduchain
    kdev4pythonparser
    ${kdev4pythonparser_LIBRARIES}
    ${QT_QTTEST_LIBRARY}
    ${KDEVPLATFORM_TESTS_LIBRARIES}
)
