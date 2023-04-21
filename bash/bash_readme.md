# Bash Scripts

Notes on the Bash scripts included in this repository

## Scripts

- colors.sh
- daily_backup.sh
- weekly_backup.sh
- mod.sh
- reboot.sh

### reboot.sh

The reboot.sh script is written to be run as a crontab and run at every boot or
reboot of the computer. The term: "$HOME" is a bash expansion of the home/user
directory, ie.

"$HOME" expands to /home/itsf4llofstars

This script requires a logfiles directory as well as a mint.log file, these can be
change to fit your needs.

#### Running reboot.sh

To use this as a crontab you will need crontab installed. Installation is beyond the
scope of this repository, but it can be checked with:

```bash
~ $ crontab -l
```

This should print a list of the currently used crontabs.

Adding reboot.sh to the crontab is done by:

```bash
~ $ crontab -e
```

> At the end of the crontab add<br>
> @reboot "$HOME"/simple_scripts/bash/reboot.sh \>/dev/null 2>&1

You can change the path to reboot.sh as needed.

It is advisable to have a crontab.log file in your logfiles directory. In which
case:

> @reboot "$HOME"/simple_scritps/bash/reboot.sh >> "$HOME"/logfiles/crontab.log 2>&1

Can be added, this will append any error occuring with crontab to be logged to the
crontab.log file.

See this: [crontab example](https://www.youtube.com/watch?v=IrynEnD5tdM&list=PLy7Kah3WzqrHPrgkBgwzXyfDDCvthdUfl&index=53&t=153s) for an excellent tutorial on crontabs, this is video 1 of 2 videos.
