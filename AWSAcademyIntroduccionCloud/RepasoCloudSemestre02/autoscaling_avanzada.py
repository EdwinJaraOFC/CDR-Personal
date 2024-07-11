import logging
import time

class Server:
    def __init__(self, nombre="my_template", description="Plantilla", ami="Linux", tipo_instancia="t2.micro", grupo_seguridad="EC2GroupSecurity"):
        self.nombre = nombre
        self.description = description
        self.ami = ami
        self.tipo_instancia = tipo_instancia
        self.grupo_seguridad = grupo_seguridad

    def __str__(self):
        return f"Server(nombre={self.nombre}, AMI={self.ami}, tipo_instancia={self.tipo_instancia}, grupo_seguridad={self.grupo_seguridad})"

class ServerTemplate:
    def create_server(self, name="my_template", description="Plantilla", ami="Linux"):
        return Server(nombre=name, description=description, ami=ami)

    def elegir_ami(self):
        opciones = {1: "Linux", 2: "macOS", 3: "Ubuntu", 4: "Windows", 5: "Red Hat", 6: "Debian"}
        print("Opciones: ", opciones)
        elegido = int(input("Elige una opción: "))
        if elegido in opciones:
            return opciones[elegido]
        else:
            print("Opción inválida, se seleccionará Linux por default.")
            return "Linux"

class CustomAutoScalingGroup:
    def __init__(self, template, min_size, max_size):
        self.template = template
        self.min_size = min_size
        self.max_size = max_size
        self.servers = self.configurar_plantilla_lanzamiento()
        self.memory_threshold = 70
        self.logger = logging.getLogger('custom_autoscaling_group')

        self.logger.info(f"Grupo de Autoescalado personalizado inicializado con {min_size} servidores.")

    def configurar_plantilla_lanzamiento(self):
        print("1: Configurar manualmente, 2: Configuración por default")
        op = int(input("Elegir una opción: "))

        if op == 1:
            name = input("Ingresar el nombre: ")
            description = input("Ingresar la descripción: ")
            ami = self.template.elegir_ami()
            return [self.template.create_server(name, description, ami) for _ in range(self.min_size)]
        elif op == 2:
            return [self.template.create_server() for _ in range(self.min_size)]
        else:
            print("Opción inválida, se utilizará la configuración por default.")
            return [self.template.create_server() for _ in range(self.min_size)]

    def set_memory_scaling_policy(self, memory_threshold):
        self.memory_threshold = memory_threshold
        self.logger.info(f"Política de escalado basada en memoria establecida en {memory_threshold}%")

    def scale_out(self):
        if len(self.servers) < self.max_size:
            self.servers.append(self.template.create_server())
            self.logger.info("Escalado hacia afuera: Se añadió un servidor")

    def scale_in(self):
        if len(self.servers) > self.min_size:
            self.servers.pop()
            self.logger.info("Escalado hacia adentro: Se eliminó un servidor")

    def adjust_capacity(self, memory_usages):
        avg_memory_usage = sum(memory_usages) / len(memory_usages)
        self.logger.info(f"Ajustando capacidad: el uso promedio de memoria es {avg_memory_usage}%")

        if avg_memory_usage > self.memory_threshold:
            self.scale_out()
        elif avg_memory_usage < self.memory_threshold and len(self.servers) > self.min_size:
            self.scale_in()

    def print_servers_info(self):
        for i, server in enumerate(self.servers):
            self.logger.info(f"Información del Servidor {i + 1}: {server}")

    def show_servers_content(self):
        for i, server in enumerate(self.servers):
            self.logger.info(f"Contenido del Servidor {i + 1}: {server}")

# Configuración global del logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

# Ejemplo de uso
template = ServerTemplate()
custom_asg = CustomAutoScalingGroup(template=template, min_size=2, max_size=5)

custom_asg.set_memory_scaling_policy(memory_threshold=75)

memory_usages = [80, 85, 70]
custom_asg.adjust_capacity(memory_usages)

custom_asg.print_servers_info()
custom_asg.show_servers_content()

custom_asg.adjust_capacity([15, 20])
