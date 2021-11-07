#!/usr/bin/env/python3

from shodan import Shodan 

def Investigacion(objetivo,key):
	conexion = Shodan(key)

	try:
		# Aquin inciamos la consulta
		consult = conexion.search(f"{objetivo}")
		print(f"[¡!] Resultados totales: {consult['total']}")
		fo = open(f"{objetivo}.txt", "a")
		# ciclo para recorrer los resultados
		for host in consult['matches']:
			
			ip = host['ip_str']
			port = host['port']
			org = host['org']

			# Escritura en el archivo .txt
			fo.write(f"[+] IP: {ip}\n")
			fo.write(f"[+] Puerto {port}\n")
			fo.write(f"[+] org\n")

			print(f"\n [+] IP: {ip}")
			print(f"[+] Puerto: {port}")
			print(f"[+] Organización: {org}")
			try:
				asn = host['asn']
				fo.write(f"[*] ASN: {asn}\n")
				print(f"[+] ASN: {asn}")
			except:
				fo.write(f"[+] ASN: Not Found.\n")
				print(f"[+] ASN: Not Found.")
				pass

			for i in host['location']:
				fo.write(f"[+] {i} : {str(host['location'][i])}\n")
				print(f"[+] {i} : {str(host['location'][i])}")
		fo.close()
	except:
		print("[¡!] Algo salió mal.\n")
		print("[!] Shodan restringe el numero de consultas a las cuentas gratuitas")
