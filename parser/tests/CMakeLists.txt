#add_executable(pyasttest pyasttest.cpp)
#add_test(pyasttest pyasttest)
#ecm_mark_as_test(pyasttest)
ecm_add_test(pyasttest.cpp
    LINK_LIBRARIES kdev4pythonparser Qt5::Test ${KDEVPLATFORM_TESTS_LIBRARIES})

#add_executable(pycythontest pycythontest.cpp)
#add_test(pycythontest pycythontest)
#ecm_mark_as_test(pycythontest)
ecm_add_test(pycythontest.cpp
    LINK_LIBRARIES kdev4pythonparser Qt5::Test ${KDEVPLATFORM_TESTS_LIBRARIES})
