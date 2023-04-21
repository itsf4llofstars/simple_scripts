#!/bin/sh
# Anacron weekly backup mint distro

set -e

HOMEDIR=/home/"$USER"
TARDIRPNY=/media/"$USER"/PNY32G/mint
TARDIRSCN=/media/"$USER"/SCANDSK/mint
tarfile=

if [ -d "$TARDIRPNY" ]; then
  tarfile="$TARDIRPNY"/weekly_backup.tar
elif [  -d "$TARDIRSCN" ]; then
  tarfile="$TARDIRSCN"/weekly_backup.tar
else
  exit 1
fi

# directories: bashscripts .config cron ed logfiles notes Pictures projects
#              python safehouse src

rm "$tarfile".gz

tar --create --absolute-names --file="$tarfile" "$HOMEDIR"/bashscripts
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/.config
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/cron
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/ed
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/logfiles
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/notes
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/Pictures
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/projects
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/python
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/safehouse
tar --append --absolute-names --file="$tarfile" "$HOMEDIR"/src

gzip "$tarfile"

printf "%s\n" "[$(date +'%Y-%m-%dT%H%M')] $0" \
  >> "$HOMEDIR"/logfiles/mint.log 2>&1

exit 0
