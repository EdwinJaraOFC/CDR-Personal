<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Actividad 11: Conceptos de introducción a las redes</h1>
</p>

## Problema 2: Optimización de protocolos y caché
<p align="justify">
  
**Escenario:** Una empresa de streaming de video experimenta interrupciones frecuentes en la entrega de contenido a los clientes. La infraestructura actual utiliza multicast para distribuir contenido, pero aún enfrenta problemas de latencia y pérdida de paquetes. 
</p>

### 1. Explica cómo mejorarías el rendimiento utilizando técnicas de caché de red. ¿Dónde colocarías estos cachés y por qué?
<p align="justify">
Para acceder al cache desde un ordenador primero busca en el caché local en lugar de volver a preguntar al servidor,el caché permite  almacenar los datos previamente cargados para un acceso más rápido, pues cuando no se encuentra el caché local este envía una consulta al solucionador DNS para comprobar su caché y en caso que este no encuentre una ip que coincida con el host este envía una consulta a su servidor de DNS preferido y en caso de no recibir respuesta por un tiempo determinado este consultara a un servidor dns alternativo.<br><br>
Una manera de mejorar el rendimiento sería usar la delegación de esta manera se podría regular el tráfico entrante a los servidores DNS. Estos servidores caché se colocarán en diferentes áreas por ejemplo distritos que luego pasan la información a un servidor de ciudad para luego a la del país de esta manera disminuye el tráfico en los servidores.
</p>
<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/b837e371-bde3-4a07-83b2-0eabe4048399">
</p>

#### Implementación de caché de red con Python
<p align="justify">
Usaremos Python para simular un sencillo sistema de caché que pueda almacenar y recuperar videos solicitados frecuentemente para reducir la latencia y la carga en el servidor principal. Para la elección del servidor del que descargar los datos, llamamos a la función Anycast que será definida y explicada a profundidad más adelante, pero de momento nos servirá para poder representar la descarga de archivos desde el servidor más cercano.
</p>

```
class VideoCache:
  def __init__(self):
    self.cache = {"perrito":"video de un perrito corriendo"}
  def get_video(self, video_id):
    if video_id in self.cache: # verificación de si el video se encuentra en el caché
      print(f"Video {video_id} retrieved from cache")
      print(self.cache) # imprimimos el diccionario de nuestro caché para confimara que se encuentre la información del video dentro
      return self.cache[video_id]
    else:
      print(f"Video {video_id} not in cache, downloading...") # se simula la descarga del video una vez no encontrado en nuestro caché
      video_data = self.download_video(video_id)
      self.cache[video_id] = video_data
      grafo = {
    '192.168.1.1': {'or': 11},
    '192.168.2.1': {'or': 3},
    '192.168.3.1': {'or': 7},
    'or':   {'192.168.1.1':11,'192.168.2.1':3,'192.168.3.1':7}
    }
      anycast = AnycastService()
      s, distancia, previos = anycast.dijkstra(grafo,"or")
      print(f"Se ha recibido el mensaje de {s[1]}")


      return video_data

  def download_video(self, video_id):

    return f"Video data for {video_id}"

# Ejemplo de uso
#con el caché vacío
cache = VideoCache()
video = cache.get_video("video1234")
print(video)

video = cache.get_video("video1234") # en esta línea, volvemos a solicitar el video, pero
#esta vez, ya se encuentra guardado en el caché, por lo que se obtiene directamente de ahí

```
### 2. ¿Cómo afecta el protocolo de transporte al rendimiento del streaming de video? Considera TCP vs UDP y justifica tu elección.
<p align="justify">
Afecta en las velocidades de carga y tiempo de respuesta, porque un servicio de streaming con protocolos lentos, pero seguros, puede presentar interrupciones en la reproducción del video. Se usa UDP principalmente, porque presenta una mayor velocidad de envío, puesto que, comparado al TCP, no se almacenan tantas variables como con el segundo tipo de conexión mencionado (el número de FLAG, números de secuencia, etc.) y no establece tantas conexiones. 
</p>
<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/8ee58a94-f39e-4337-8a82-e4b039f21670">
</p>

#### Selección del protocolo de transporte
<p align="justify">
Exploraremos cómo usar UDP en lugar de TCP para mejorar la eficiencia de la transmisión de video, debido a la menor sobrecarga de UDP.<br><br>
Discusión:<br>
  
● Explica las ventajas de usar UDP sobre TCP para streaming de video, considerando las características de ambos protocolos.<br>
- La principal ventaja del UDP sobre el TCP es su menor latencia a comparacion del TCP ya que este ultimo trasfiere mayor cantidad de datos y es mas segura mientras que el UDP podra ser mas rapido pero no garantiza la llegada de la informacion. Todo esto se debe a que TCP antes de enviar los datos establece y verifica la conexion mientras que el UDP no lo hace , esto puede llevar a que los datos no terminen llegando al destino.

● Analiza los posibles problemas de confiabilidad y orden de llegada de los paquetes y cómo mitigarlos.

- Con ya se menciono antes, el UDP a pesar de ser mas rapido y presentar menor latencia puede presentar problemas de confiabilidad ya que no asegura que los datos lleguen , pero en el contexto de una compañia de streming este puede tolerar cierta pedida de informacion como flujo de audio y videos .Por otro lado el TCP al establecer una coneccion antes de enviar la infomacion este presenta un mayor latencia pero al mismo tiempo se asegura que la informacion llegue a su destino  aumetando su confiabilidad.Una manea de mitigar los problemas de confiabilidad de UPD seria implementar estrategias como FEC (Forward Error Correction) implica enviar información redundante junto con los datos originales, lo que permite al receptor reconstruir los datos perdidos sin necesidad de solicitar la retransmisión de los paquetes.

</p>

### 3. Propone una solución usando Anycast para optimizar la entrega de contenido. ¿Cómo funcionaría en este contexto?
<p align="justify">
Para optimizar la entrega de contenido, implementaremos Anycast. Configuraremos servidores Anycast en ubicaciones estratégicas para abordar los problemas de latencia y pérdida de datos. Cuando los usuarios soliciten contenido, sus solicitudes serán dirigidas automáticamente al servidor Anycast más cercano y eficiente en la red, garantizando una entrega optimizada del contenido.<br><br>
Ventajas de Anycast sobre Multicast en este caso:<br>
  
● **Reducción de la latencia:** Anycast dirige las solicitudes de los usuarios al servidor más cercano geográficamente, lo que reduce significativamente la latencia en comparación con la difusión de datos a través de multicast a través de la red.<br>
● **Mayor control y escalabilidad:** Anycast permite una mayor flexibilidad y control al dirigir las solicitudes de los usuarios a servidores específicos, lo que facilita la escalabilidad y la gestión de la red en comparación con multicast, que puede ser más difícil de controlar en entornos grandes y complejos.<br>
● **Menor impacto en la red:** Anycast solo envía datos al servidor más cercano, lo que reduce la carga en la red en comparación con multicast, que puede generar tráfico adicional al enviar datos a múltiples destinos simultáneamente.
</p>
<p align="center">
    <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/29ab9300-048e-4da4-8737-82f4388e03d0">
</p>

#### Implementación de anycast con Python
<p align="justify">
Simularemos el uso de anycast para dirigir las solicitudes de los usuarios al servidor de caché más cercano utilizando Python. Este ejemplo es conceptual, ya que la implementación real de anycast se manejaría a un nivel más bajo en la red. En este caso, se elige el servidor de manera aleatoria con la función random.choice.
</p>

```
import random
class AnycastService:
  def __init__(self):
    self.servers = ['192.168.1.1', '192.168.2.1', '192.168.3.1']
  def get_nearest_server(self, user_ip):
    # Simula la selección del servidor más cercano (simplificado)
    return random.choice(self.servers)
# Ejemplo de uso
anycast = AnycastService()
nearest_server = anycast.get_nearest_server("192.168.1.100")
print(f"Nearest server for user is {nearest_server}")
```
<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/7fb0aa24-a215-4f50-8b96-4e488ccc0a57">
</p>

#### Implementación de anycast con Python, ahora asignando distancias del servidor principal a los demás servidores de manera aleatoria y mostrando un grafo
```
import random
import networkx as nx
import matplotlib.pyplot as plt

class AnycastService:
  def __init__(self):
    self.servers = ['192.168.1.1', '192.168.2.1', '192.168.3.1']
    # Inicializamos la matriz de distancias desde "192.168.1.100" a los servidores
    self.distances = {}
    self.distances["192.168.1.100"] = {}
    for server in self.servers:
      distance = random.randint(1, 10)
      self.distances["192.168.1.100"][server] = distance

  def getNearestServer(self, userIP):
    minDistance = float('inf')
    nearestServer = None

    # Iteramos sobre los servidores para encontrar el más cercano
    for server in self.servers:
      distance = self.distances[userIP].get(server, float('inf'))
      if distance < minDistance:
        minDistance = distance
        nearestServer = server
    return nearestServer

  def drawNetwork(self):
    G = nx.DiGraph()

    # Agregamos nodos
    G.add_nodes_from(self.servers)
    G.add_node("192.168.1.100")

    # Agregamos distancias
    for server, distance in self.distances["192.168.1.100"].items():
      G.add_edge("192.168.1.100", server, weight=distance)

    # Dibujamos el grafo
    pos = nx.spring_layout(G) # Podemos usar diferentes grafos: circular_layout, random_layout, shell_layout
    nx.draw(G, pos, with_labels=True, node_size=3500, node_color="skyblue", font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Anycast Network")
    plt.show()

anycast = AnycastService()
nearestServer = anycast.getNearestServer("192.168.1.100")
print(f"Nearest server for user is {nearestServer}")
anycast.drawNetwork()
```
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/03cb8c8b-01af-4255-8d54-b4a40e30dbc7" width="333px">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/92b25778-eb10-4ade-b931-46bc64e22899" width="333px">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/c11e3098-957d-49bc-8159-ff02dba00282" width="333px">
</div>

### 4. Desarrolla un modelo simplificado para calcular el efecto de la caché en la reducción de latencia. 
<p align="justify">
Mientras más caché se almacene en el dispositivo, más información para el acceso rápido tendrá el usuario, para así evitar requests constantes al servidor. Sin embargo, también tomará espacio significativo en el almacenamiento del usuario o en la capacidad del proxy intermediario para retener esta información en pro de una conexión más rápida con los datos almacenados de las páginas web usadas con frecuencia.<br><br>
Un posible modelo útil para el cálculo del efecto que tiene el caché en la reducción de latencia, sería, una vez implementado, sería la comparación directa entre el tiempo en envío y recepción de paquetes con y sin la aplicación de las técnicas de memoria caché.
</p>
<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/551f20ea-e0c7-4fbc-9912-55862ff5ffd6">
</p>

