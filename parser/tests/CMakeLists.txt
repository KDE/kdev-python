set(pyasttest_SRCS pyasttest.cpp ../parserdebug.cpp)

include_directories(${CMAKE_BINARY_DIR}/duchain)
ecm_add_test(${pyasttest_SRCS}
    TEST_NAME pyasttest
    LINK_LIBRARIES kdevpythonparser Qt5::Test KDev::Tests)

set(pycythontest_SRCS pycythontest.cpp ../parserdebug.cpp)
ecm_add_test(${pycythontest_SRCS}
    TEST_NAME pycythontest
    LINK_LIBRARIES kdevpythonparser Qt5::Test KDev::Tests)
