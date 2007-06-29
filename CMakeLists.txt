
#To properly find kdevelop-pg add -DKDEVPG_DATA_DIR=<kdevpg-install-path>/share to the
#cmake run if you installed it in a different directory than this plugin
#TODO: a cmake run is needed after changing one of the CMakeLists.txt, make will
#complain about the FindKDevelop-PG.cmake file not findable.
if( KDEVPG_DATA_DIR )
    set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${KDEVPG_DATA_DIR}/cmake/modules )
else( KDEVPG_DATA_DIR )
    set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_INSTALL_PREFIX}/share/cmake/modules )
endif( KDEVPG_DATA_DIR )
if( FLEX_DATA_DIR )
    set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${FLEX_DATA_DIR}/cmake/modules )
endif( FLEX_DATA_DIR )


add_subdirectory(parser)
