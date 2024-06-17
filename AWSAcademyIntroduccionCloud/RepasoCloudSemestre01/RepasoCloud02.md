<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Temas: VPC, Route53, CloudFront</h1>
</p>

## Código
### Ejercicio 8: Simulación de un CDN con control de caché avanzado
Implementar una CDN que almacene en caché contenido y soporte políticas de caché avanzadas como expiración basada en tiempo y tamaño máximo de caché.

#### Define la clase CDN:
- Crea una clase CDN para gestionar el contenido en caché.
- Implementa métodos para agregar contenido a la caché, recuperar contenido, y manejar la expiración de caché.

#### Políticas de caché:
- Implementa una política de caché basada en tiempo para expirar contenido después de un tiempo determinado.
- Implementa una política de tamaño máximo de caché y manejar la eliminación de contenido cuando se exceda el tamaño.

#### Simular solicitudes de contenido:
- Implementa un método para simular solicitudes de contenido que respete las políticas de caché.

```
import time
class CDN:
    def __init__(self, max_cache_size, cache_expiration):
        self.cache = {}
        self.max_cache_size = max_cache_size
        self.cache_expiration = cache_expiration

    def get_content(self, url):
        if url in self.cache:
            content, timestamp = self.cache[url]
            if time.time() - timestamp < self.cache_expiration:
                print("Content served from cache")
                return content
            else:
                print("Cache expired, fetching new content")
                self.cache.pop(url)
        content = self.fetch_from_origin(url)
        self.add_to_cache(url, content)
        return content

    def fetch_from_origin(self, url):
        print("Fetching content from origin server...")
        time.sleep(2) # Simular tiempo de respuesta del servidor de origen
        return f"Content of {url}"
 
    def add_to_cache(self, url, content):
        if len(self.cache) >= self.max_cache_size:
            self.evict_cache()
        self.cache[url] = (content, time.time())
    
    def evict_cache(self):
        # Evict the oldest cache entry
        oldest_url = min(self.cache, key=lambda k: self.cache[k][1])
        print(f"Evicting cache for {oldest_url}")
        self.cache.pop(oldest_url)
    
    def __str__(self):
        return str(self.cache)

# Simulación de la CDN
def main():
    cdn = CDN(max_cache_size=3, cache_expiration=10)
    while True:
        command = input("Enter command (get, exit): ")
        if command == 'get':
            url = input("Enter URL to fetch: ")
            content = cdn.get_content(url)
            print(content)
        elif command == 'exit':
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
```
