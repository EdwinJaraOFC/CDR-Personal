import logging
import time

class CustomAutoScalingGroup:
    def __init__(self, template, min_size, max_size):
        self.template = template  # Plantilla de servidor utilizada para crear nuevos servidores
        self.min_size = min_size  # Tamaño mínimo del grupo de servidores
        self.max_size = max_size  # Tamaño máximo del grupo de servidores
        self.servers = [self.template.create_server() for _ in range(min_size)]  # Lista de servidores iniciales
        self.memory_threshold = 70  # Límite de uso de memoria para escalar
        self.logger = logging.getLogger('custom_autoscaling_group')  # Logger para el grupo de autoescalado

        self.logger.info(f"Grupo de Autoescalado personalizado inicializado con {min_size} servidores.")

    def set_memory_scaling_policy(self, memory_threshold):
        self.memory_threshold = memory_threshold  # Establece el límite de uso de memoria para escalar
        self.logger.info(f"Política de escalado basada en memoria establecida en {memory_threshold}%")

    def scale_out(self):
        if len(self.servers) < self.max_size:  # Verifica si el número de servidores es menor que el máximo
            self.servers.append(self.template.create_server())  # Añade un nuevo servidor a la lista
            self.logger.info("Escalado hacia afuera: Se añadió un servidor")

    def scale_in(self):
        if len(self.servers) > self.min_size:  # Verifica si el número de servidores es mayor que el mínimo
            self.servers.pop()  # Elimina un servidor de la lista
            self.logger.info("Escalado hacia adentro: Se eliminó un servidor")

    def adjust_capacity(self, memory_usages):
        avg_memory_usage = sum(memory_usages) / len(memory_usages)  # Calcula el uso promedio de memoria
        self.logger.info(f"Ajustando capacidad: el uso promedio de memoria es {avg_memory_usage}%")

        if avg_memory_usage > self.memory_threshold:  # Si el uso promedio de memoria supera el límite
            self.scale_out()  # Escala hacia afuera
        elif avg_memory_usage < self.memory_threshold and len(self.servers) > self.min_size:  # Si el uso promedio de memoria es menor que el límite
            self.scale_in()  # Escala hacia adentro

    def print_servers_info(self):
        for i, server in enumerate(self.servers):
            self.logger.info(f"Información del Servidor {i + 1}: {server.info}")

    def show_servers_content(self):
        for i, server in enumerate(self.servers):
            self.logger.info(f"Contenido del Servidor {i + 1}: {server.get_content()}")

class ServerTemplate:
    def create_server(self):
        server = Server()  # Crea una nueva instancia de Server
        server.add_info("AWS", "Auto-escalado habilitado")  # Añade información al servidor
        server.add_content("Datos importantes", "Elasticidad y Autoescalado")  # Añade contenido al servidor
        return server

class Server:
    def __init__(self):
        self.info = {}  # Diccionario para almacenar información del servidor
        self.content = {}  # Diccionario para almacenar contenido del servidor

    def add_info(self, key, value):
        self.info[key] = value  # Añade un par clave-valor a la información del servidor

    def add_content(self, key, value):
        self.content[key] = value  # Añade un par clave-valor al contenido del servidor

    def get_content(self):
        return self.content  # Retorna el contenido del servidor

# Configurar el logging globalmente
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

# Ejemplo de uso
template = ServerTemplate()  # Crea una plantilla de servidor
custom_asg = CustomAutoScalingGroup(template=template, min_size=2, max_size=5)  # Crea un grupo de autoescalado personalizado

# Establecer la política de escalado basada en memoria
custom_asg.set_memory_scaling_policy(memory_threshold=70)

# Simular métricas de uso de memoria
memory_usages = [80, 85, 70]

custom_asg.adjust_capacity(memory_usages)  # Ajusta la capacidad del grupo basado en los usos de memoria proporcionados
custom_asg.print_servers_info()  # Imprime la información de todos los servidores
custom_asg.show_servers_content()  # Muestra el contenido de todos los servidores
