#!/bin/python3 Python3

import subprocess
import argparse
import WebScraping
import Investigacion
import CifradoPIA
import MandarCorreo
import Metadata

parser = argparse.ArgumentParser()

# Argumentos para WebScrapping
parser.add_argument("-wS","--webScraping", help="Iniciar webscraping.", action="store_true")
parser.add_argument("-s", "--Sitio", help="Sitio para hacer webscraping.", )

# Argumentos para shodan
parser.add_argument("-Sh", "--Shodan", help="Herramienta para investigar mediante shodan.", action="store_true")
parser.add_argument("-ob", "--Objetivo", help="Se declara el objetivo de Shodan")

# Argumentos PortScaner
parser.add_argument("-pS","--portScan", help="Escaneo de puertos.", action="store_true")
parser.add_argument("-i", "--ip", help="IP objetivo a escanear.")

# Argumentos para cifrado
parser.add_argument("-c","--cifrado", help="Cifrado de archivo.", action="store_true")
parser.add_argument("-Co", "--correo", help="Correo para cifrar.")
parser.add_argument("-Cl", "--clave", help="Palabra clave.")

# Argumentos para Metadatos
parser.add_argument("-oM", "--obtMetadatos", help="Obtención de meta datos", action="store_true")
parser.add_argument("-r", "--ruta", help="La ruta absoluta de donde se obtendra la metadata")

#Argumentos para Envio de correos
parser.add_argument("-e", "--enviar_correo", help="Envio de correos", action="store_true")

parser.add_argument("-a", "--all", help="Ejecución de todas las funciones", action="store_true")

parser = parser.parse_args()


# opcionales de los argumentos
if parser.webScraping:
    print("[+] Se escogió webscraping\n")
    sitio = parser.Sitio
    print(f"{sitio}")

    try:
        # Manda a llamar el módulo WebScraping 
        WebScraping.WebScrapping(sitio)
    except:
        print("Something else wen wrong")

# Aqui es el uso de Shodan
elif parser.Shodan:
    print("[+] Se escogió Investigacion con Shodan")
    print("""[!] Esta herramienta requiere un API Key, favor de ingresarla.
        [!] Si no cuentas con una, registrate aqui: https://account.shodan.io/register""")
    key = input("\n[->] API Key: ")

    try:
        Investigacion.Investigacion(parser.Objetivo, key)
    except:
        print("\n\t [¡!] Algo salió mal")

# Uso de PortScaner
elif parser.portScan:
    print("[+] Se escogió escaneo de puertos\n")
    
    # Aquí va el script de escaneo de puertos.
    process = subprocess.Popen(["./PortScan.sh", f"{parser.ip}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("[+] Completado")
    print(process.stdout.read())

# Cifrado de 
elif parser.cifrado:
    print("[+] Se escogió cifrado de archivos.\n")
    # Aquí va el script de cifrado de archivos.
    CifradoPIA.CifradoF(parser.correo, parser.clave)
 
#Obtener metadatos
elif parser.obtMetadatos:
    print("[+] Se escogío obtencion de metadatos\n")
    try:
        
    
#Mandar correos
elif parser.enviar_correo:
    print("[+] Se escogió Envio de correos.\n")
    #Aquí va el script de Envio de correos.
    MandarCorreo.Envio_Correo()
    
