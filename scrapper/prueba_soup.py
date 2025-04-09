'''
Prueba de BeautifulSoup 
'''
from bs4 import BeautifulSoup

html = "<html><body><h1>Titulo</h1><p>Texto</p></body></html>"
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())  # Imprime el HTML formateado
print(soup.h1.text)  # Imprime el texto dentro de la etiqueta <h1>
soup.p.string = "Hola mundo!"  # Cambia el texto dentro de la etiqueta <p>
soup.h1.string = "Hola mundo de BeautifulSoup"
nueva_etiqueta = soup.new_tag("p")
nueva_etiqueta.string = "Soy una nueva etiqueta"
soup.body.append(nueva_etiqueta)  # Añade la nueva etiqueta al body
nueva_liga = soup.new_tag("a", href="https://www.google.com")
nueva_liga.string = "Google"
soup.body.append(nueva_liga)  
print(soup.prettify())  # Imprime el HTML formateado
print("..........................")
print(soup.find("h1"))  # Encuentra la primera etiqueta <h1>
print(soup.find_all("p"))  # Encuentra todas las etiquetas <p>
parrafos = soup.find_all("p")
lista_parrafos = []
for p in parrafos:
    lista_parrafos.append(p.string) 
print(lista_parrafos)  # Imprime la lista de textos de los párrafos