#automoc4(pyduchaintest waitforupdate.cpp)
#add_executable(pyduchaintest pyduchaintest.cpp)
#add_test(pyduchaintest pyduchaintest)
#ecm_mark_as_test(pyduchaintest)
ecm_add_test(pyduchaintest.cpp)

#add_executable(duchainbench duchainbench.cpp)
#add_test(duchainbench duchainbench)
#ecm_mark_as_test(duchainbench)
ecm_add_test(duchainbench.cpp)

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
