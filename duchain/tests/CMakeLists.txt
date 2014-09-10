set(pyduchaintest_SRCS
    pyduchaintest.cpp
    ../duchaindebug.cpp)

ecm_add_test(${pyduchaintest_SRCS}
    TEST_NAME pyduchaintest)

set(duchainbench_SRCS
    duchainbench.cpp
    ../duchaindebug.cpp)

ecm_add_test(${duchainbench_SRCS}
    TEST_NAME duchainbench)

add_definitions(-DDUCHAIN_PY_DATA_DIR="${CMAKE_CURRENT_SOURCE_DIR}")

target_link_libraries(pyduchaintest
    kdev4pythonduchain
    kdev4pythonparser
    ${kdev4pythonparser_LIBRARIES}
    Qt5::Test
    ${KDEVPLATFORM_TESTS_LIBRARIES}
)

target_link_libraries(duchainbench
    kdev4pythonduchain
    kdev4pythonparser
    ${kdev4pythonparser_LIBRARIES}
    Qt5::Test
    ${KDEVPLATFORM_TESTS_LIBRARIES}
)
