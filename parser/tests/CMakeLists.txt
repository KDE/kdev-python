set(pyasttest_SRCS pyasttest.cpp ../parserdebug.cpp)

include_directories(${CMAKE_BINARY_DIR}/duchain)
ecm_add_test(${pyasttest_SRCS}
    TEST_NAME pyasttest
    LINK_LIBRARIES kdevpythonparser Qt6::Test KDev::Tests)

