# PIA - Programaci贸n para Ciber Seguridad.

Este proyecto es una recopilaci贸n de diversas herramientas de ciberseguridad unidas en una sola que se puedem mandar llamar desde un main. Entre esas tareas se encuentra:
* WebScraping.
* Investigacion con shodan.
* Escaneo de puertos con nmap.
* Extracci贸n de metadata.
* Cifrado.
* Env铆o de correos.

## Comenzando 馃殌
_Este script funciona mediante argumentos, solo ciertos script requieren de la interacci贸n del usuario, a continuacion se muestra c贸mo lo puedes obtener._

### Pre-requisitos 馃搵
_Sistema operativo Linux para el escaneo de puertos con nmap mediante bash._

Si no tienes nmap, as铆 se instala en Linux:

```
$ sudo apt-get install nmap
```
_Para la investigaci贸n mediante shodan es necesario tenerlo instalado en las librer铆as de python._

Se utiliza el siguiente comando para Linux y Windows.
```
pip install shodan
```


### Instalacion 馃敡
_Para una instalaci贸n en Linux solamente se debe clonar el repositorio de la siguiente manera._
```
$ git clone https://github.com/MrGh057/PIA_PC
```

_Para Windows_
```
* Click en la secci贸n Code (bot贸n verde).
* Download ZIP.
```
## Ejecuci贸n de la herramienta 鈿欙笍
_Herramienta de webscraping._
```
$ python main.py -wS -s http://www.paginaobjetivo.com/
```

_Herramienta con Shodan._
```
$ python main.py -Sh -ob objetivo
```

_Herramienta PortScaner._
```
$ python main.py -pS -i 127.0.0.1
```

_Herramienta de cifrado._
```
$ python main.py -c -Co correo -Cl Clave
```

_Herramienta metadatos_
```
$ python main.py -oM -r C:/users/Panchito/Desktop/imagenes/
```
_Env铆o de correos_
```
$ python main.py -e
```


## Construido con 馃洜锔?
_Se utilizaron las siguientes documentaciones_
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
* [Shodan](https://shodan.readthedocs.io/en/latest/)
* [Nmap](https://nmap.org/book/port-scanning-options.html)
* [smptlib](https://docs.python.org/3/library/smtplib.html)
* [ssl](https://docs.python.org/3/library/ssl.html)
* [subprocess](https://docs.python.org/3/library/subprocess.html)

## Autores 鉁掞笍
* **Jos茅 Gerardo ME** - [MrGh057](https://github.com/MrGh057)
* **Jelmy Gerardo LG** - [JelmyLG](https://github.com/JelmyLG)
* **Diego Ibarra** - [DikerZarc40](https://github.com/DikerZarc40)
* **Diego Alexander** - [LicPlatano](https://github.com/LicPlatano)
* **Erick Cruz** - [VirtualCryst](https://github.com/VirtualCryst)
