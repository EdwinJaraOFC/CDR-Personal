class OSIModel:
    def __init__(self, data):
        if not data:
            raise ValueError("Los datos no pueden estar vacíos.")
        self.data = data

    def application_layer(self):
        print("Capa de Aplicación: Procesando datos", self.data)
        self.data = "procesado_aplicación(" + self.data + ")"
        self.presentation_layer()

    def presentation_layer(self):
        print("Capa de Presentación: Formateando datos", self.data)
        self.data = "procesado_presentación(" + self.data + ")"
        self.session_layer()

    def session_layer(self):
        print("Capa de Sesión: Gestionando sesión para datos", self.data)
        self.data = "procesado_sesión(" + self.data + ")"
        self.transport_layer()

    def transport_layer(self):
        print("Capa de Transporte: Segmentando datos", self.data)
        self.data = "procesado_transporte(" + self.data + ")"
        self.network_layer()

    def network_layer(self):
        print("Capa de Red: Enrutando datos", self.data)
        self.data = "procesado_red(" + self.data + ")"
        self.data_link_layer()

    def data_link_layer(self):
        print("Capa de Enlace de Datos: Enmarcando datos", self.data)
        self.data = "procesado_enlace(" + self.data + ")"
        self.physical_layer()

    def physical_layer(self):
        print("Capa Física: Transmitiendo datos", self.data)
        self.data = "procesado_físico(" + self.data + ")"
        print("Datos finales transmitidos:", self.data)

    def process_data(self):
        self.application_layer()

# Ejemplo de uso
osi_model = OSIModel(data="Hola Mundo")
osi_model.process_data()
