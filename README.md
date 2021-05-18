# battery-daemon
> TP1 - Software Libre - 2021 - FI-UNMdP

Daemon para Linux que detecta si la batería está cargada completamente y el sistema enchufado, y lo registra en un archivo en `/var/log`. Realizado en `Python 3`.

## Alumnos 
  - Mariquena Gros
  - Pablo Porzio


## Instalación

1 - Clonar repo:

```
$ git clone https://github.com/porziopablo/battery-daemon.git
```

2 - Crear directorio para logs:

```
$ sudo mkdir /var/log/battery-daemon
```

3 - Transferir propiedad al `usuario` que ejecutará el daemon:

```
$ sudo chown usuario /var/log/battery-daemon
```

## Ejecución

1 - Correr: 

```
$ python3 battery-daemon.py start
```

2 - Detener: 

```
$ python3 battery-daemon.py stop
```


3 - Reiniciar:

```
$ python3 battery-daemon.py restart
```

## Fuentes

- [Esqueleto de daemon](https://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/)
- [Librería dbus para Python](https://dbus.freedesktop.org/doc/dbus-python/tutorial.html)
- [Servicio UPower](https://upower.freedesktop.org/docs/Device.html)
- [Código base para UPower](https://gist.github.com/kjmkznr/1343846)
- [Librería logging para Python](https://docs.python.org/3/howto/logging.html)
