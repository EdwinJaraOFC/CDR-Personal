import logging
import heapq  # Para usar una cola de prioridad
import random
import time

# Configurar el logging globalmente
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class NotificationSystem:
    def __init__(self):
        self.topics = {}  # Diccionario para almacenar los temas y sus suscripciones
        self.retry_limit = 3  # Límite máximo de reintentos

    def create_topic(self, name):
        self.topics[name] = []  # Inicializa el tema con una lista vacía de suscripciones
        logging.info(f"Tema creado: {name}")  # Registro de creación de tema en el log
        return name

    def subscribe(self, topic, endpoint):
        if topic in self.topics:
            self.topics[topic].append(endpoint)
            logging.info(f"Suscripción añadida: {endpoint.name} al tema {topic}")  # Registro de suscripción del endpoint en el log
        else:
            raise Exception("El tema no existe")

    def unsubscribe(self, topic, endpoint):
        if topic in self.topics:
            self.topics[topic].remove(endpoint)
            print("")
            logging.info(f"Suscripción eliminada: {endpoint.name} del tema {topic}")  # Registro de desuscripción del endpoint en el log
        else:
            raise Exception("El tema no existe")

    def publish(self, topic, message, priority=0):
        if topic in self.topics:
            for endpoint in self.topics[topic]:
                heapq.heappush(endpoint.message_queue, (priority, message))
                logging.info(f"Mensaje publicado en tema {topic}: {message} con prioridad {priority}")  # Registro de publicación del mensaje con prioridad en el log
                time.sleep(1)
                self.send_notifications(endpoint)  # Intentar enviar las notificaciones
        else:
            raise Exception("El tema no existe")

    def send_notifications(self, endpoint):
        while endpoint.message_queue:
            priority, message = heapq.heappop(endpoint.message_queue)
            success = self.attempt_send(endpoint, message)
            if not success:
                self.retry(endpoint, message, priority)

    def attempt_send(self, endpoint, message):
        if endpoint.notify(message):
            logging.info(f"Notificación enviada con éxito a {endpoint.name}: {message}")  # Registro de éxito en envío de notificación en el log
            print("")
            time.sleep(1)
            return True
        else:
            logging.info(f"Fallo al enviar notificación a {endpoint.name}: {message}")  # Registro de fallo en envío de notificación en el log
            time.sleep(1)
            return False

    def retry(self, endpoint, message, priority):
        attempts = 1
        while attempts <= self.retry_limit:
            logging.info(f"Reintentando ({attempts}/{self.retry_limit}) para {endpoint.name}")  # Registro de intento de reenvío en el log
            time.sleep(1)
            if self.attempt_send(endpoint, message):
                return
            attempts += 1
        logging.info(f"Notificación fallida después de {self.retry_limit} intentos para {endpoint.name}")  # Registro de fallo tras reintentos en el log
        print("")

class Endpoint:
    def __init__(self, name):
        self.name = name
        self.message_queue = []  # Cola de prioridad para los mensajes

    def notify(self, message):
        if random.random() > 0.3:  # Simular fallos aleatorios con una probabilidad del 30%
            return False
        return True

# Ejemplo de uso
sns = NotificationSystem()
email_endpoint = Endpoint("cayetano@upch.pe")
sms_endpoint = Endpoint("+51905116858")

# Crear tema y suscribir endpoints
sns.create_topic("alertas")
sns.subscribe("alertas", email_endpoint)
sns.subscribe("alertas", sms_endpoint)
print("")

# Publicar mensajes con diferentes prioridades
sns.publish("alertas", "Mensaje de alta prioridad", priority=1)
time.sleep(2)

sns.publish("alertas", "Mensaje de baja prioridad", priority=3)
time.sleep(2)

sns.publish("alertas", "Mensaje de prioridad media", priority=2)
time.sleep(2)

# Publicar más mensajes para ver reintentos y logs
sns.publish("alertas", "Otro mensaje de alta prioridad", priority=1)
time.sleep(2)

sns.publish("alertas", "Otro mensaje de baja prioridad", priority=3)
time.sleep(2)

# Desuscribir un endpoint y publicar un mensaje
sns.unsubscribe("alertas", email_endpoint)
sns.publish("alertas", "Mensaje después de desuscribir email", priority=1)
time.sleep(2)
