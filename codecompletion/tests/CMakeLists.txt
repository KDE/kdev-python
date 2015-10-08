set(pycompletiontest_SRCS 
    pycompletiontest.cpp
    ../codecompletiondebug.cpp)

ecm_add_test(${pycompletiontest_SRCS}
    TEST_NAME pycompletiontest
    LINK_LIBRARIES
        kdevpythonduchain
        kdevpythoncompletion
        kdevpythonparser
        ${kdevpythonparser_LIBRARIES}
        Qt5::Test
        KDev::Tests
)
