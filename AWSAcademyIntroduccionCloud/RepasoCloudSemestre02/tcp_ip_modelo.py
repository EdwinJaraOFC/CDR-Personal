class TCPIPModel:
    def __init__(self, data):
        if not data:
            raise ValueError("Los datos no pueden estar vacíos.")
        self.data = data

    def application_layer(self):
        print("Capa de Aplicación: Procesando datos", self.data)
        self.data = "procesado_aplicación(" + self.data + ")"
        self.transport_layer()

    def transport_layer(self):
        print("Capa de Transporte: Segmentando datos", self.data)
        self.data = "procesado_transporte(" + self.data + ")"
        self.internet_layer()

    def internet_layer(self):
        print("Capa de Internet: Enrutando datos", self.data)
        self.data = "procesado_internet(" + self.data + ")"
        self.network_interface_layer()

    def network_interface_layer(self):
        print("Capa de Interfaz de Red: Transmitiendo datos", self.data)
        self.data = "procesado_interfaz(" + self.data + ")"
        print("Datos finales transmitidos:", self.data)

    def process_data(self):
        self.application_layer()

# Ejemplo de uso
tcp_ip_model = TCPIPModel(data="Hola Mundo")
tcp_ip_model.process_data()
