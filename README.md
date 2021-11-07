# PIA - Programación para Ciber Seguridad.

Este proyecto es una recopilación de diversas herramientas de ciberseguridad unidas en una sola que se puedem mandar llamar desde un main. Entre esas tareas se encuentra:
* WebScraping.
* Investigacion con shodan.
* Escaneo de puertos con nmap.
* Extracción de metadata.
* Cifrado.
* Envío de correos.

## Comenzando 🚀
_Este script funciona mediante argumentos, solo ciertos script requieren de la interacción del usuario, a continuacion se muestra cómo lo puedes obtener._

### Pre-requisitos 📋
_Sistema operativo Linux para el escaneo de puertos con nmap mediante bash._

Si no tienes nmap, así se instala en Linux:

```
$ sudo apt-get install nmap
```
_Para la investigación mediante shodan es necesario tenerlo instalado en las librerías de python._

Se utiliza el siguiente comando para Linux y Windows.
```
pip install shodan
```


### Instalacion 🔧
_Para una instalación en Linux solamente se debe clonar el repositorio de la siguiente manera._
```
$ git clone https://github.com/MrGh057/PIA_PC
```

_Para Windows_
```
* Click en la sección Code (botón verde).
* Download ZIP.
```
## Ejecución de la herramienta ⚙️
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
$ python main.py -c
```

_Herramienta metadatos_
```
$ python main.py -oM
```


## Construido con 🛠️
_Se utilizaron las siguientes documentaciones_
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
* [Shodan](https://shodan.readthedocs.io/en/latest/)
* [Nmap](https://nmap.org/book/port-scanning-options.html)
* [smptlib](https://docs.python.org/3/library/smtplib.html)
* [ssl](https://docs.python.org/3/library/ssl.html)
* [subprocess](https://docs.python.org/3/library/subprocess.html)

## Autores ✒️
* **José Gerardo ME** - [MrGh057](https://github.com/MrGh057)
* **Jelmy Gerardo LG** - [JelmyLG](https://github.com/JelmyLG)
* **Diego Ibarra** - [DikerZarc40](https://github.com/DikerZarc40)
