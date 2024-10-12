import requests
from bs4 import BeautifulSoup
import re
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# URL de la página que deseas scrapear
url = "https://www.amazon.com/s?k=dog+food&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9DNA5TKUEJWY&sprefix=dog+foo%2Caps%2C197&ref=nb_sb_noss_2"

# Configurar el User-Agent para hacer que parezca que el request proviene de un navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

# Hacer la solicitud HTTP
response = requests.get(url, headers=headers)

variable_enlaces_buscar=  []

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Extraer el contenido HTML de la página
    html_content = response.text

    # Usar regex para encontrar los enlaces y textos deseados
    # El patrón busca enlaces <a> con clase específica y extrae el href y el texto dentro del enlace
    pattern = r'<a.*?class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal".*?href="(.*?)".*?>(.*?)</a>'
    pattern2 = r'href=["\']([^"\']*page=(\d+)[^"\']*)["\']'

    
    # Buscar todas las coincidencias con el patrón
    enlaces = re.findall(pattern, html_content)
    pagina_siguiente = re.findall(pattern2, html_content)
    print(pagina_siguiente)
    
    for href in pagina_siguiente:
        enlace_completo = "https://www.amazon.com" + href[0]  # Crear el enlace completo # Agregar a la lista
        print(f"Enlace a la siguiente página: {enlace_completo}")
        variable_enlaces_buscar.append(enlace_completo)
    # Imprimir los resultados encontrados
    for href_enlace, texto_enlace in enlaces:
        # Limpiar el texto del enlace
        texto_enlace = re.sub(r'<.*?>', '', texto_enlace).strip()
        enlace_completo = f"https://www.amazon.com{href_enlace}"  # Crear el enlace completo
        # Imprimir el texto y el enlace completo
        print(enlace_completo)
else:
    print(f"Error al acceder a la página, código de estado: {response.status_code}")
    
    