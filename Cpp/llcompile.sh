#!/bin/bash
currentDirectory=$(pwd)
cmakeListsPath="${currentDirectory}/CMakeLists.txt"

if [ ! -f "$cmakeListsPath" ]; then
  echo "No CMakeLists.txt in current directory, please check."
  exit 1
fi

echo "Start generating and compiling..."

buildFolderPath="./build"

if [ ! -d "$buildFolderPath" ]; then
  mkdir -p "$buildFolderPath"
  echo "build folder created."
fi

cmake -G "Unix Makefiles" -DCMAKE_SYSTEM_PROCESSOR=x86_64 -S . -B ./build/

if [ $? -eq 0 ]; then
  cmake --build ./build/ --config DEBUG
fi
