#!/usr/bin/bash

set -e

TARFILE="$HOME"/archives/daily_backup.tar
NVIMCONF=""
KITTYCONF="$HOME"/.config/kitty/kitty.conf

if [ -f "$HOME"/.config/nvim/init.vim ]; then
  NVIMCONF="$HOME"/.config/nvim/init.vim
elif [ -f "$HOME"/.config/nvim/init.lua ]; then
  NVIMCONF="$HOME"/.config/nvim/init.lua
fi

LOGDIR="$HOME"/logfiles/mint.log
LOGDATE=$(date +'%FT%T')

if [ -f "$TARFILE" ]; then
  rm "$TARFILE"
fi

DOTFILES=(.bashrc .bash_aliases .gitconfig .tmux.conf .nanorc)

tar --create --absolute-names --file="$TARFILE" "$NVIMCONF"
tar --append --absolute-names --file="$TARFILE" "$KITTYCONF"

for dotfile in "${DOTFILES[@]}"; do
  tar --append --absolute-names --file="$TARFILE" "$HOME"/"$dotfile"
done

printf "%s\n" "[$LOGDATE] $0" >> "$LOGDIR" 2>&1

exit 0
