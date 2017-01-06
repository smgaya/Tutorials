cmake_minimum_required(VERSION 3.6)
project(C)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES MemoryManagement.cpp CommandLineArguments.cpp)
add_executable(C ${SOURCE_FILES})