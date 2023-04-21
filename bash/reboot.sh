#!/usr/bin/bash

# A script that can be set to run as a cron using crontab
# This scripts requires that the user has the directory structure
# /home/$USER/logfiles/logfile.log
# Where $USER is is the users Linux username.
# This can expanded by either using the tilda:
#
# ~/logfiles
#
# or $HOME
#
# "$HOME"
#
# As seen in the script

# Running with crontab, add:
#
# @reboot "$HOME"/[script_dir]/reboot.sh
#
# To your crontab. [script_dir] is the path to the reboot.sh script
# See bash_readme.md file


# Append the date and time to the mint.log file in the logfiles directory
printf "%s\n" "[$(date +'%FT%H:%M')] $0" >> "$HOME"/logfiles/mint.log 2>&1

