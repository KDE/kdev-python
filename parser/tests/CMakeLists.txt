
include_directories(${CMAKE_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_BINARY_DIR})

set(parsetest_SRCS parsetest.cpp)
qt4_automoc(${parsetest_SRCS})
add_executable(python-parsetest ${parsetest_SRCS})
target_link_libraries(python-parsetest
    ${QT_QTTEST_LIBRARY}
    ${QT_QTCORE_LIBRARY}
    kdevpythonparser
)

