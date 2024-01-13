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
        Qt${QT_MAJOR_VERSION}::Test
        KF${KF_MAJOR_VERSION}::Service
        KDev::Tests
)
