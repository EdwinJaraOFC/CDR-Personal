<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Temas: VPC, Route53, CloudFront</h1>
</p>

## Ejercicio 8: Simulación de un CDN con control de caché avanzado
Implementar una CDN que almacene en caché contenido y soporte políticas de caché avanzadas como expiración basada en tiempo y tamaño máximo de caché.

### Define la clase CDN:
- Crea una clase CDN para gestionar el contenido en caché.
- Implementa métodos para agregar contenido a la caché, recuperar contenido, y manejar la expiración de caché.

### Políticas de caché:
- Implementa una política de caché basada en tiempo para expirar contenido después de un tiempo determinado.
- Implementa una política de tamaño máximo de caché y manejar la eliminación de contenido cuando se exceda el tamaño.

### Simular solicitudes de contenido:
- Implementa un método para simular solicitudes de contenido que respete las políticas de caché.

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| Red de entrega de contenido (CDN)  | <p align="justify">Red de servicios distribuidos que proporciona páginas web y otro contenido web de forma segura en función de la ubicación geográfica del usuario.</p>  |
| Memoria Caché  | <p align="justify">Forma de almacenamiento temporal de alta velocidad que guarda copias de datos o contenidos para que futuras solicitudes de esos datos se puedan satisfacer más rápidamente.</p>  |
| Control de Caché Avanzado  | <p align="justify">Técnicas y políticas empleadas para gestionar el almacenamiento y la expiración de datos en la caché de manera eficiente. Esto incluye determinar qué datos deben almacenarse, durante cuánto tiempo, y cuándo deben eliminarse.</p>  |
| Técnicas de control de caché  | <p align="justify">LRU (Least Recently Used), FIFO (First In, First Out), LFU (Least Frequently Used).</p>  |
| Políticas de caché  | <p align="justify">Definen las reglas y estrategias para gestionar cómo se almacena y se elimina el contenido en la caché.</p>  |

## Código

```
import os
import random
import webbrowser
import time
from datetime import datetime

class CDN:
    def __init__(self, max_cache_size, cache_expiration):
        self.cache = {}  # Diccionario para almacenar el contenido en caché
        self.max_cache_size = max_cache_size  # Tamaño máximo de la caché
        self.cache_expiration = cache_expiration  # Tiempo de expiración de la caché
        self.access_times = {}  # Diccionario para almacenar el tiempo de acceso
        self.url_to_html = {}  # Diccionario para almacenar la correspondencia URL - archivo HTML

    def read_and_open_html(self, url):
        folder = os.getcwd()  # Obtiene el directorio actual de trabajo
        ruta = os.path.join(folder, "folder")

        if url in self.url_to_html:
            html_file = self.url_to_html[url]
        else:
            files = os.listdir(ruta)  # Lista los archivos en la carpeta 'folder'
            if not files:
                print("No hay archivos HTML en la carpeta 'folder'.")
                return

            html_file = random.choice(files)  # Selecciona un archivo HTML aleatorio
            self.url_to_html[url] = html_file  # Almacena la correspondencia URL - archivo HTML

        full_path = os.path.join(ruta, html_file)
        print(f"Abriendo archivo HTML: {html_file}")
        self.open_html_file(full_path)

    def open_html_file(self, full_path):
        try:
            webbrowser.open('file://' + os.path.realpath(full_path))  # Abre el archivo HTML en el navegador
        except Exception as e:
            print(f"Error al abrir archivo HTML: {e}")

    def get_content(self, url):
        if url in self.cache:
            content, timestamp = self.cache[url]  # Obtiene el contenido y el timestamp de la URL de la caché
            if time.time() - timestamp < self.cache_expiration:
                print("Contenido servido de la caché.")
                self.access_times[url] = datetime.fromtimestamp(timestamp)  # Convierte a datetime
                return content  # Devuelve el contenido de la caché si no ha expirado
            else:
                print("Caché expirado, obteniendo nuevo caché.")
                self.cache.pop(url)  # Elimina el contenido expirado de la caché
                self.access_times.pop(url, None)  # Elimina el tiempo de acceso también
        self.read_and_open_html(url)  # Abre el archivo HTML correspondiente a la URL
        content = self.fetch_from_origin(url)  # Obtiene el contenido del servidor de origen
        self.add_to_cache(url, content)  # Añade el contenido a la caché
        return content

    def fetch_from_origin(self, url):
        print("Obteniendo contenido del servidor original...")
        time.sleep(2)  # Simula el tiempo de respuesta del servidor de origen
        return f"Contenido de {url}"  # Devuelve el contenido simulado del servidor de origen

    def add_to_cache(self, url, content):
        if len(self.cache) >= self.max_cache_size:
            self.evict_cache()  # Evita la entrada más antigua si la caché está llena
        timestamp = time.time()
        self.cache[url] = (content, timestamp)  # Añade el contenido a la caché con el timestamp actual
        self.access_times[url] = datetime.fromtimestamp(timestamp)  # Almacena el tiempo de acceso como datetime

    def evict_cache(self):
        # Desalojar la entrada de caché utilizada menos recientemente
        lru_url = min(self.access_times, key=self.access_times.get)
        print(f"Desalojando caché de {lru_url}")
        self.cache.pop(lru_url)  # Elimina la entrada menos recientemente usada de la caché
        self.access_times.pop(lru_url)

    def __str__(self):
        formatted_cache = {}
        for url, (content, timestamp) in self.cache.items():
            formatted_cache[url] = (content, datetime.fromtimestamp(timestamp).strftime('%H:%M:%S'))
        return str(formatted_cache)  # Devuelve una representación en cadena de la caché con tiempos formateados


def main():
    cdn = CDN(max_cache_size=4, cache_expiration=20)  # Crea una instancia de la clase CDN con tamaño máximo de caché y expiración
    while True:
        command = input("Ingrese un comando (get, exit): ")
        if command == 'get':
            url = input("Ingrese URL a buscar: ")
            content = cdn.get_content(url)  # Obtiene el contenido de la URL solicitada
            print(content)
            print(cdn)
        elif command == 'exit':
            print(cdn)
            break  # Sale del bucle si el comando es 'exit'
        else:
            print("Comando inválido")  # Informa si el comando es inválido


if __name__ == "__main__":
    main()  # Ejecuta la función main si el script se ejecuta directamente
```
