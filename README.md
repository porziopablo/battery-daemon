# battery-daemon
TP1, Software Libre, FI-UNMdP, 2021: Programar un daemon en Linux que detecte si la batería está cargada completamente y el sistema enchufado, y lo registre en un archivo en `/var/log`. 

Instalación
1 - Clonar repo

`$ git clone https://github.com/porziopablo/battery-daemon.git`

2 - Crear directorio para logs:

`$ sudo mkdir /var/log/battery-daemon`

3 - Transferir propiedad al usuario que ejecutará el daemon:

`$ sudo chown usuario /var/log/battery-daemon`

Ejecución:

1 - Correr: 

`$ python3 battery-daemon.py start`

2 - Detener: 

`$ python3 battery-daemon.py stop`


3 - Reiniciar:

`$ python3 battery-daemon.py restart`

