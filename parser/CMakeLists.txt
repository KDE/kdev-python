add_subdirectory(tests)

include_directories(${CMAKE_CURRENT_BINARY_DIR})

get_parser_srcs(parser_SRCS)

kde4_add_executable( python-parser main.cpp
    ${parser_SRCS} ${parser_STAT_SRCS}
)
target_link_libraries(python-parser ${QT_QTCORE_LIBRARY})
install(TARGETS python-parser DESTINATION ${BIN_INSTALL_DIR})

