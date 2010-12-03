kde4_add_unit_test(pyduchaintest pyduchaintest.cpp )
target_link_libraries(pyduchaintest kdev4pythonduchain ${QT_QTTEST_LIBRARY} ${KDEVPLATFORM_TESTS_LIBRARIES})
