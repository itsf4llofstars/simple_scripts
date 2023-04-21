#!/usr/bin/bash
# shellcheck disable=SC2059

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

