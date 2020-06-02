"""
Author: Julian Guillermo Zapata Rugeles
Correo: Juliang.zapata@udea.edu.co
Descargar videos de youtube por palabras claves
https://www.facebook.com/julianguillermo.zapatarugeles.1

2020
GPL

"""
bienvenida="""
*******************************************
          FAST YOUTUBE DOWNLOADER
                   FYD

*Instrucciones:
   -Ingresa el nombre de la cancion o video
   -Selecciona el formato
   -Listo !

******************************************* """
salida="""
*******************************************
                HASTA LUEGO
*******************************************
"""

import urllib.request
from bs4 import BeautifulSoup
import os

def ObtenerEnlaces(busqueda):
    consulta = urllib.parse.quote(busqueda)
    url = "https://www.youtube.com/results?search_query=" + consulta
    respuestaYoutube = urllib.request.urlopen(url) # re envia la peticiòn
    html = respuestaYoutube.read() # se lee el contenido
    soup = BeautifulSoup(html, 'html.parser')

    todosEnlaces=[]

    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        enlace_individual=str('https://www.youtube.com' + vid['href'])
        todosEnlaces.append(enlace_individual)
    if len(todosEnlaces)==0:
        print("verifica tu conexión a internet :( ")
        exit()
    return todosEnlaces[0]

def Descargar(enlace):
    options=[1,2]
    continuar=False
    while continuar==False:
        print("********** Que desea decargar ? ***********\n1) vídeo\n2) canción\n")
        try:
            election=int(input())
            if election in options:
                continuar=True
        except Exception as e:
            print("Alerta:  elección inválida")
            os.system("clear") #aquì se borra la consola cls para windows !
    if election==2:
        comando="youtube-dl -f m4a "+str(enlace)
        os.system(comando)
    else:
        comando="youtube-dl -f mp4 "+str(enlace)
        os.system(comando)

####################### INICIO DEL PROGRAMA #########################
print(bienvenida)
busqueda=str(input("Buscar : "))
print("\n buscando...\n")
enlace=ObtenerEnlaces(busqueda)
Descargar(enlace)
print(salida)
