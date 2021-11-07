#!/usr/bin/env/python3

from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup


# Información básica
def Basic_Info(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    title_name = soup.title.string
    title_parent = soup.title.parent.name

    print('\n [!] Basic information:')
    print('\n\t [+] Title name: ', title_name)
    print('\n\t [+] Title parent: ', title_parent)


# Función que define el estado de la página
def url_Status(url):
    r = requests.get(url)
    if r.status_code == 200:
        return 1
    else:
        return 0


# Función que busca links
def Find_Links(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    title_name = soup.title.string
    fo = open(f"{title_name}.txt", "a")
    for link in (soup.find_all('a')):
        if (link.get('href')) is not None:
            enlace = link.get('href')
            fo.write(f"\n [+] {enlace} \n")
            print('\t [+] ', link.get('href'))
    fo.close()

# Función que llama para hacer webscrapping
def WebScrapping(ip):
    try:
        pStatus = url_Status(ip)
        if pStatus == 1:
            cont = False
        else:
            input("\n[¡!] The link does not respond. Please press enter.")
    except:
        input('\n [¡!] Something else went wrong.')

    Basic_Info(ip)
    print("\n [!] All links on the page: \n")
    Find_Links(ip)
    