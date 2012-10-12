automoc4(pyduchaintest waitforupdate.cpp)
kde4_add_unit_test(pyduchaintest pyduchaintest.cpp waitforupdate.cpp)

target_link_libraries(pyduchaintest
    kdev4pythonduchain
    kdev4pythonparser
    ${QT_QTTEST_LIBRARY}
    ${KDEVPLATFORM_TESTS_LIBRARIES}
)
