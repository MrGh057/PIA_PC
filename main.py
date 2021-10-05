#!/bin/python3 Python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-wS","--webScraping", help="Iniciar webscraping.", action="store_true")
parser.add_argument("-pS","--portScan", help="Escaneo de puertos.", action="store_true")
parser.add_argument("-c","--cifrado", help="Cifrado de archivo.", action="store_true")
parser.add_argument("-oM", "--obtMetadatos", help="Obtención de meta datos", action="store_true")
parser.add_argument("-a", "--all", help="Ejecución de todas las funciones", action="store_true")
parser = parser.parse_args()

if parser.webScraping:
    print("[+] Se escogió webscraping\n")
    # Aquí va el script de webscraping.
elif parser.portScan:
    print("[+] Se escogió escaneo de puertos\n")
    # Aquí va el script de escaneo de puertos.
elif parser.cifrado:
    print("[+] Se escogió cifrado de archivos.\n")
    # Aquí va el script de cifrado de archivos.
elif parser.obtMetadatos:
    print("[+] Se escogío obtencion de metadatos\n")
