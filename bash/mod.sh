#!/usr/bin/bash
# mod.sh
# Script used to quickly change a files permissions
# to executable

if [ "$1" == "-h" ] || [ "$1" == "--help" ]
then
    clear
    echo
    printf "\t%s\n\n" "Changes a files permission to executable"
    printf "\t%s\n" "\$ ./mod.sh [OPTIONS]"
    printf "\t%s\n\n" "\$ ./mod.sh file"
    printf "\t%s\n" "OPITIONS"
    printf "\t\t%s\n" "-h, --help Print this help and exit."
    echo
    exit 0
fi

PERS=755
FILE="$1"

chmod "$PERS" "$FILE"

exit
