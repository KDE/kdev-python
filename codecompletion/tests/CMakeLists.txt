set(pycompletiontest_SRCS 
    pycompletiontest.cpp
    ../codecompletiondebug.cpp)

ecm_add_test(${pycompletiontest_SRCS}
    TEST_NAME pycompletiontest
    LINK_LIBRARIES
        kdev4pythonduchain
        kdev4pythoncompletion
        kdev4pythonparser
        ${kdev4pythonparser_LIBRARIES}
        Qt5::Test
        KDev::Tests
        KF5::KDELibs4Support
)
