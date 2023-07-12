#!/usr/bin/env bash

# Remaps the Caps Lock key to Escape, Control, or back to Caps Lock
#    depending on the user sent command line argument.
#
# remap [options]
#
# Options:
#    -e : Remaps Caps Lock to Escape key
#    -c : Remaps Caps Lock to Caps Lock key
#    -t : Remaps Caps Lock to Control key
#

if [ "$1" == "-e" ]; then
    dconf write /org/gnome/desktop/input-sources/xkb-options "['caps:escape']"
    printf "Caps Lock to Escape\n"
elif [ "$1" == "-c" ]; then
    dconf write /org/gnome/desktop/input-sources/xkb-options "['caps:caps']"
    printf "Caps Lock to Caps Lock\n"
elif [ "$1" == "-t" ]; then
    dconf write /org/gnome/desktop/input-sources/xkb-options "['caps:ctrl_modifier']"
    printf "Caps Lock to Control\n"
else
    printf "Command line arg -e (to esc), -c (to caps-lock), -t (to control) needed.\n"
fi

# cat remap.sh | head -n 12
