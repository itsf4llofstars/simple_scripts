#!/usr/bin/bash
# shellcheck disable=SC2059

clear

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
  printf "%s\n" "    Prints numbers 0-255 in the color that each 256 number"
  printf "%s\n" "    represents."
  printf "\n%s\n" "    ~ $ ./colors.sh [options]"
  printf "\n%s\n" "    OPTIONS"
  printf "%s\n" "        -h, --help Print this help and exit."
  printf "%s\n" "        -n Print numbers and colors in a single column"
  exit
fi

if [ "$1" == "-n" ]; then
  for i in {0..255}; do
    printf "\x1b[38;5;${i}m${i}\n"
  done
else
  for i in {0..255}; do
    printf "\x1b[38;5;${i}m${i} "
  done
fi
echo
