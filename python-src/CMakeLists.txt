# determine the PYTHON version from Include/patchlevel.h

file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/_usedpythonversion.cpp 
"#include <patchlevel.h>\n"
"#include <stdio.h>\n"
"int main() { printf(\"%i.%i.%i\", PY_MAJOR_VERSION, PY_MINOR_VERSION, PY_MICRO_VERSION); return 0; }")

set(CMAKE_REQUIRED_INCLUDES )
try_run(_VERSION_RUN_RESULT
        _VERSION_COMPILE_RESULT
        ${CMAKE_CURRENT_BINARY_DIR}
        ${CMAKE_CURRENT_BINARY_DIR}/_usedpythonversion.cpp
        COMPILE_DEFINITIONS -IC:/kde/git/kdev-python/python-src/Include
        RUN_OUTPUT_VARIABLE run_output
        COMPILE_OUTPUT_VARIABLE compile_output
)
string(REGEX REPLACE "([0-9])\\.([0-9])\\.([0-9])" "\\1" PYTHON_MAJOR_VERSION ${run_output})
string(REGEX REPLACE "([0-9])\\.([0-9])\\.([0-9])" "\\2" PYTHON_MINOR_VERSION ${run_output})
string(REGEX REPLACE "([0-9])\\.([0-9])\\.([0-9])" "\\3" PYTHON_MICRO_VERSION ${run_output})

if(NOT WIN32)

    add_custom_target(
        python_target
        COMMAND /bin/bash ${CMAKE_CURRENT_SOURCE_DIR}/configure --enable-shared --without-pymalloc WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        COMMAND /usr/bin/env make -C ${CMAKE_CURRENT_SOURCE_DIR}
    )
    add_library(python-kdevelop SHARED IMPORTED)
    set_target_properties(python-kdevelop PROPERTIES
        IMPORTED_LOCATION "${CMAKE_CURRENT_SOURCE_DIR}/libpython${PYTHON_MAJOR_VERSION}.${PYTHON_MINOR_VERSION}-kdevelop.so.1.0"
        IMPORTED_SONAME "libpython${PYTHON_MAJOR_VERSION}.${PYTHON_MINOR_VERSION}-kdevelop.so"
    )
    add_dependencies(python-kdevelop python_target)

    install(FILES libpython${PYTHON_MAJOR_VERSION}.${PYTHON_MINOR_VERSION}-kdevelop.so DESTINATION ${LIB_INSTALL_DIR})
    install(FILES libpython${PYTHON_MAJOR_VERSION}.${PYTHON_MINOR_VERSION}-kdevelop.so.1.0 DESTINATION ${LIB_INSTALL_DIR})

else(NOT WIN32)
    include_directories(Python Modules/zlib Include PC)
    add_executable(make_versioninfo PC/make_versioninfo.c)
    add_custom_command(OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/pythonnt_rc.h COMMAND ${CMAKE_CURRENT_BINARY_DIR}/make_versioninfo.exe > ${CMAKE_CURRENT_BINARY_DIR}/pythonnt_rc.h)

    set(PYTHON_SRCS
        Python/traceback.c
        Python/thread.c
        Python/sysmodule.c
        Python/symtable.c
        Python/structmember.c
        Python/pythonrun.c
        Python/Python-ast.c
        Python/dtoa.c
        Python/pystrtod.c
        Python/pystrcmp.c
        Python/pystate.c
        Python/pytime.c
        Python/pymath.c
        Python/pyfpe.c
        Python/pyctype.c
        Python/pyarena.c
        Python/peephole.c
        Python/mystrtoul.c
        Python/mysnprintf.c
        Python/modsupport.c
        Python/marshal.c
        Python/importdl.c
        Python/import.c
        Python/graminit.c
        Python/getversion.c
        Python/getplatform.c
        Python/getopt.c
        Python/getcopyright.c
        Python/getcompiler.c
        Python/getargs.c
        Python/future.c
        Python/frozen.c
        Python/formatter_unicode.c
        Python/fileutils.c
        Python/errors.c
        Python/dynload_win.c
        Python/dynamic_annotations.c
        Python/compile.c
        Python/codecs.c
        Python/ceval.c
        Python/bltinmodule.c
        Python/ast.c
        Python/asdl.c
        Python/_warnings.c
        PC/msvcrtmodule.c
        PC/import_nt.c
        PC/getpathp.c
        PC/dl_nt.c
        PC/config.c
        PC/winreg.c
        PC/_subprocess.c
        Parser/tokenizer.c
        Parser/parsetok.c
        Parser/parser.c
        Parser/node.c
        Parser/myreadline.c
        Parser/metagrammar.c
        Parser/listnode.c
        Parser/grammar1.c
        Parser/grammar.c
        Parser/firstsets.c
        Parser/bitset.c
        Parser/acceler.c
        Objects/weakrefobject.c
        Objects/unicodeobject.c
        Objects/unicodectype.c
        Objects/typeobject.c
        Objects/tupleobject.c
        Objects/structseq.c
        Objects/sliceobject.c
        Objects/setobject.c
        Objects/rangeobject.c
        Objects/obmalloc.c
        Objects/object.c
        Objects/moduleobject.c
        Objects/methodobject.c
        Objects/memoryobject.c
        Objects/longobject.c
        Objects/listobject.c
        Objects/iterobject.c
        Objects/genobject.c
        Objects/funcobject.c
        Objects/frameobject.c
        Objects/floatobject.c
        Objects/fileobject.c
        Objects/exceptions.c
        Objects/enumobject.c
        Objects/dictobject.c
        Objects/descrobject.c
        Objects/complexobject.c
        Objects/codeobject.c
        Objects/classobject.c
        Objects/cellobject.c
        Objects/capsule.c
        Objects/bytesobject.c
        Objects/bytearrayobject.c
        Objects/bytes_methods.c
        Objects/boolobject.c
        Objects/abstract.c
        Modules/cjkcodecs/multibytecodec.c
        Modules/cjkcodecs/_codecs_tw.c
        Modules/cjkcodecs/_codecs_kr.c
        Modules/cjkcodecs/_codecs_jp.c
        Modules/cjkcodecs/_codecs_iso2022.c
        Modules/cjkcodecs/_codecs_hk.c
        Modules/cjkcodecs/_codecs_cn.c
        Modules/zlib/zutil.c
        Modules/zlib/uncompr.c
        Modules/zlib/trees.c
        Modules/zlib/inftrees.c
        Modules/zlib/inflate.c
        Modules/zlib/inffast.c
        Modules/zlib/infback.c
        Modules/zlib/deflate.c
        Modules/zlib/crc32.c
        Modules/zlib/compress.c
        Modules/zlib/adler32.c
        Modules/_io/_iomodule.c
        Modules/_io/textio.c
        Modules/_io/iobase.c
        Modules/_io/bufferedio.c
        Modules/_io/stringio.c
        Modules/_io/bytesio.c
        Modules/_io/fileio.c
        Modules/zlibmodule.c
        Modules/zipimport.c
        Modules/xxsubtype.c
        Modules/timemodule.c
        Modules/_threadmodule.c
        Modules/symtablemodule.c
        Modules/signalmodule.c
        Modules/sha512module.c
        Modules/sha256module.c
        Modules/sha1module.c
        Modules/rotatingtree.c
        Modules/posixmodule.c
        Modules/parsermodule.c
        Modules/operator.c
        Modules/mmapmodule.c
        Modules/md5module.c
        Modules/mathmodule.c
        Modules/main.c
        Modules/itertoolsmodule.c
        Modules/gcmodule.c
        Modules/errnomodule.c
        Modules/_datetimemodule.c
        Modules/cmathmodule.c
        Modules/binascii.c
        Modules/audioop.c
        Modules/atexitmodule.c
        Modules/arraymodule.c
        Modules/_weakref.c
        Modules/_time.c
        Modules/_struct.c
        Modules/_sre.c
        Modules/_randommodule.c
        Modules/_pickle.c
        Modules/_math.c
        Modules/_lsprof.c
        Modules/_localemodule.c
        Modules/_json.c
        Modules/_heapqmodule.c
        Modules/_functoolsmodule.c
        Modules/_csv.c
        Modules/_collectionsmodule.c
        Modules/_codecsmodule.c
        Modules/_bisectmodule.c
        ${CMAKE_CURRENT_BINARY_DIR}/pythonnt_rc.h
        PC/python_nt.rc
    )

    # that file is normally compiled by make_buildinfo so that it can be configured at buildtime
    # (God bless cmake ;-))
    list(APPEND PYTHON_SRCS
        Modules/getbuildinfo.c
    )

    add_definitions(-D_USRDLL -DPy_BUILD_CORE -DPy_ENABLE_SHARED)
    add_library(python-kdevelop SHARED ${PYTHON_SRCS})
    target_link_libraries(python-kdevelop kernel32 user32 gdi32 winspool comdlg32 advapi32 shell32 ole32 oleaut32 uuid odbc32 odbccp32)
    set_target_properties(python-kdevelop PROPERTIES OUTPUT_NAME python${PYTHON_MAJOR_VERSION}.${PYTHON_MINOR_VERSION}-kdevelop)
    install(TARGETS python-kdevelop RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)
endif(NOT WIN32)
