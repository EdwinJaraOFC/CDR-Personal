import time

class CDN:
    """
    Implementación de una CDN básica con Python
    Podemos simular una CDN que almacena en caché el contenido y responde a las solicitudes.
    """
    def __init__(self):
        self.cache = {}

    def get_content(self, url):
        if url in self.cache:
            print("Content served from cache")
            return self.cache[url]
        else:
            content = self.fetch_from_origin(url)
            self.cache[url] = content
            return content
    
    def fetch_from_origin(self, url):
        print("Fetching content from origin server...")
        time.sleep(2) # Simular tiempo de respuesta del servidor de origen
        return f"Content of {url}"

# Crear una instancia de CDN
cdn = CDN()
# Solicitar contenido
print(cdn.get_content("https://example.com/image.png"))