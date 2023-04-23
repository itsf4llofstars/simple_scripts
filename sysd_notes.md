# Systemd Time

## Create a Script

Create a bash script to be run by the systemd timer

> script.sh

## Create Systemd Service

Create a systemd service to run the script.<br>
At the command prompt:

```bash
~ $ cd /etc/systemd/system
$ sudo vim [service_name].service
```

The mininum required lines are:

```bash
[Service]
ExecStart=/home/$USER/[path_to_script]/[script].sh
```

## Using the Service

### Reload the Daemon

Initially we need to reload the daemon

```bash
$ sudo systemctl daemon reload
```

### Start/Stop the Service

We need to now start the service

```bash
$ sudo systemctl start [service_name].service
```

We can now check to see if our [script].sh is/has/will run.

To stop the service:

```bash
$ sudo systemctl stop [service_name].service
```

NOTE: If we change the [script].sh file we do not need to reload the daemon.

## Checking Logs

We can check to logs to view any problems, or to ensure we are running the script.

```bash
$ tail -f /var/log/syslog

$ sudo journalctl -u [service_name] -f
```

NOTE: We did not put the .service suffix on the service_name

Use Ctrl-c to exit the log views.

## Updating the Service

We can update the service with:

```bash
$ sudo systemctl edit [service_name] --full
```

NOTE: No .service at the end

### Add Desciption to Service

```bash
[Unit]
Description=Describe the systemd service and or script.sh file we are running

[Service]
ExecStart=/home/$USER/[path_to_script]/[script].sh
User=$USER
```

### Add To Run When GUI Desktop Starts

```bash
[Unit]
Description=Describe the systemd service and or script.sh file we are running

[Service]
ExecStart=/home/$USER/[path_to_script]/[script].sh
User=$USER

[Install]
WantedBy=graphical.target
```

### Add To Run When NON-GUI Desktop Starts

```bash
[Unit]
Description=Describe the systemd service and or script.sh file we are running

[Service]
ExecStart=/home/$USER/[path_to_script]/[script].sh
User=$USER

[Install]
WantedBy=multiuser.target
```

NOTE: Since we used:

> $ sudo systemctl edit [service_name] --full

We do not need to reload the daemon

## Check Status

To check the status:

```bash
$ systemctl satus [service_name].service
```

## END VIDEO 57
