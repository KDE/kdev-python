
include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${QT_QTCORE_INCLUDE_DIR}
    ${QT_QTTEST_INCLUDE_DIR}
    ${QT_INCLUDE_DIR}
    ${KDE4_INCLUDE_DIR}
    )


set(parsetest_SRCS parsetest.cpp )

kde4_add_unit_test(python-parsetest ${parsetest_SRCS})
target_link_libraries(python-parsetest
    ${QT_QTTEST_LIBRARY}
    ${QT_QTCORE_LIBRARY}
    kdev4pythonparser
)

set(lexertest_SRCS lexertest.cpp )

kde4_add_unit_test(python-lexertest ${lexertest_SRCS})
target_link_libraries(python-lexertest
    ${QT_QTTEST_LIBRARY}
    ${QT_QTCORE_LIBRARY}
    kdev4pythonparser
)


if(KDE4_BUILD_TESTS)
add_custom_target( run_py_test
	COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/test_runner.py -p ${CMAKE_BINARY_DIR}/parser/python-parser -s ${CMAKE_CURRENT_SOURCE_DIR}
	DEPENDS python-parser
	WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)
endif(KDE4_BUILD_TESTS)

