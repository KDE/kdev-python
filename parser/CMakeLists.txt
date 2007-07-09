add_subdirectory(tests)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
include_directories(${QT_INCLUDES})
include_directories(${KDE4_INCLUDE_DIR})

set(parser_STAT_SRCS
    decoder.cpp
    python_io.cpp
    pythondriver.cpp
    )

kde4_add_executable( python-parser main.cpp ${lexer_SRCS} ${parser_STAT_SRCS} ${parser_SRCS} )
target_link_libraries(python-parser ${QT_QTCORE_LIBRARY})
install(TARGETS python-parser DESTINATION ${BIN_INSTALL_DIR})

