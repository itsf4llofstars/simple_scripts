#!/usr/bin/bash
# mod.sh
# Script used to quickly change a files permissions
# to executable

if [ "$1" == "-h"] || [ "$1" == "--help" ]
then
    printf "\t%s\n\n" "Changes a files permission to executable"
    printf "\t%s\n\n" "\$ ./mod.sh file"
fi

PERS=755
FILE="$1"

chmod "$PERS" "$FILE"

exit
