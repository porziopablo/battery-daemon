# battery-daemon
> TP1 - Software Libre - 2021 - FI-UNMdP

Daemon for Linux that detects if the battery is completely charged and the computer is plugged-in, and then registers it in a file in `/var/log`. Made with `Python 3`.

## Authors 
  - Mariquena Gros
  - Pablo Porzio


## Installation

1 - Clone repo:

```
git clone https://github.com/porziopablo/battery-daemon.git
```

2 - Create logs directory:

```
sudo mkdir /var/log/battery-daemon
```

3 - Transfer ownership to the `user` that will run the daemon:

```
sudo chown usuario /var/log/battery-daemon
```

## Execution

1 - Start: 

```
python3 battery-daemon.py start
```

2 - Stop: 

```
python3 battery-daemon.py stop
```


3 - Restart:

```
python3 battery-daemon.py restart
```

## Sources

- [Daemon template](https://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/)
- [Dbus library for Python](https://dbus.freedesktop.org/doc/dbus-python/tutorial.html)
- [UPower service](https://upower.freedesktop.org/docs/Device.html)
- [Upower source code](https://gist.github.com/kjmkznr/1343846)
- [Logging library for Python](https://docs.python.org/3/howto/logging.html)
