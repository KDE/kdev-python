add_executable(pycompletiontest pycompletiontest.cpp)
add_test(pycompletiontest pycompletiontest)
ecm_mark_as_test(pycompletiontest)

target_link_libraries(pycompletiontest
    kdev4pythonduchain
    kdev4pythoncompletion
    kdev4pythonparser
    ${kdev4pythonparser_LIBRARIES}
    Qt5::Test
    ${KDEVPLATFORM_TESTS_LIBRARIES}
)
