include_directories(
    ${CMAKE_CURRENT_BINRAY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

set(completion_SRCS
    pythoncodecompletioncontext.cpp
    pythoncodecompletionmodel.cpp
    pythoncodecompletionworker.cpp
)

kde4_add_library(kdev4pythoncompletion SHARED ${completion_SRCS})

target_link_libraries(kdev4pythoncompletion
    ${KDE4_KDECORE_LIBS}
    ${KDEVPLATFORM_LANGUAGE_LIBRARIES}
)

install(TARGETS ${kdev4pythoncompletion} DESTINATION ${INSTALL_TARGETS_DEFAULT_ARGS})
