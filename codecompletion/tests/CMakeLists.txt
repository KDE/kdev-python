kde4_add_unit_test(pycompletiontest pycompletiontest.cpp)

target_link_libraries(pycompletiontest
    kdev4pythonduchain
    kdev4pythoncompletion
    kdev4pythonparser
    ${kdev4pythonparser_LIBRARIES}
    ${QT_QTTEST_LIBRARY}
    ${KDEVPLATFORM_TESTS_LIBRARIES}
)
