
include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${QT_QTCORE_INCLUDE_DIR}
    ${QT_QTTEST_INCLUDE_DIR}
    ${QT_INCLUDE_DIR}
    ${KDE4_INCLUDE_DIR}
    )

get_parser_srcs(parser_SRCS)

set(parsetest_SRCS parsetest.cpp
    ${parser_SRCS} ${parser_STAT_SRCS} )

kde4_add_unit_test(python-parsetest ${parsetest_SRCS})
target_link_libraries(python-parsetest
    ${QT_QTTEST_LIBRARY}
    ${QT_QTCORE_LIBRARY}
)

if(KDE4_BUILD_TESTS)
add_custom_target( run_py_test 
	COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/test_runner.py -p ${CMAKE_BINARY_DIR}/parser/python-parser -s ${CMAKE_CURRENT_SOURCE_DIR}
	DEPENDS python-parser
	WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)
endif(KDE4_BUILD_TESTS)

