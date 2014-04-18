kde4_add_unit_test(pyasttest pyasttest.cpp)
target_link_libraries(pyasttest kdev4pythonparser ${QT_QTTEST_LIBRARY} ${KDEVPLATFORM_TESTS_LIBRARIES})

kde4_add_unit_test(pycythontest pycythontest.cpp)
target_link_libraries(pycythontest kdev4pythonparser ${QT_QTTEST_LIBRARY} ${KDEVPLATFORM_TESTS_LIBRARIES})