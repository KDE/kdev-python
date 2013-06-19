automoc4(pyduchaintest waitforupdate.cpp)
kde4_add_unit_test(pyduchaintest pyduchaintest.cpp)

target_link_libraries(pyduchaintest
    kdev4pythonduchain
    kdev4pythonparser
    ${kdev4pythonparser_LIBRARIES}
    ${QT_QTTEST_LIBRARY}
    ${KDEVPLATFORM_TESTS_LIBRARIES}
)
