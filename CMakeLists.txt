cmake_minimum_required(VERSION 2.8)
project(romkan)

find_package(Java COMPONENTS Runtime Development)
include(UseJava)

find_package (Python3 COMPONENTS Interpreter)

add_custom_command(OUTPUT ${PROJECT_BUILD_DIR}/RomkanData.java.gen
  COMMAND ${Python3_EXECUTABLE} ${PROJECT_SOURCE_DIR}/jromkan-generate.py -c RomkanData -e utf-8
  -p org.happypeng.sumatora.jromkan
  DEPENDS ${PROJECT_SOURCE_DIR}/jromkan-generate.py)

get_filename_component(JDK_BIN_DIR ${JAVA_COMPILE} PATH)

find_program(NATIVE2ASCII NAMES native2ascii PATHS ${JDK_BIN_DIR})

if(NATIVE2ASCII)
  message(STATUS "Using native2ascii: ${NATIVE2ASCII}")
else()
  message(FATAL_ERROR "native2ascii not found")
endif()

add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/org/happypeng/sumatora/jromkan/RomkanData.java
  COMMAND ${NATIVE2ASCII} -encoding utf-8 RomkanData.java.gen ${PROJECT_SOURCE_DIR}/org/happypeng/sumatora/jromkan/RomkanData.java
  DEPENDS ${PROJECT_BUILD_DIR}/RomkanData.java.gen)

add_jar(romkan ${PROJECT_SOURCE_DIR}/org/happypeng/sumatora/jromkan/RomkanData.java romkancli.java ENTRY_POINT romkancli)
