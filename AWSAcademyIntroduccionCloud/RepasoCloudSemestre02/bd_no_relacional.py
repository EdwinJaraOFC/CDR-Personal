class BDNoRelacional:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}

    def insertar_documento(self, clave, documento):
        if clave not in self.documentos:
            self.documentos[clave] = documento
            print(f"Documento insertado con clave '{clave}': {documento}")
        else:
            print(f"La clave '{clave}' ya existe")

    def obtener_documento(self, clave):
        if clave in self.documentos:
            documento = self.documentos[clave]
            print(f"Documento encontrado con clave '{clave}': {documento}")
            return documento
        else:
            print(f"No se encontró documento con clave '{clave}'")

    def eliminar_documento(self, clave):
        if clave in self.documentos:
            del self.documentos[clave]
            print(f"Documento con clave '{clave}' eliminado correctamente")
        else:
            print(f"No se encontró documento con clave '{clave}'")

    def listar_documentos(self):
        print(f"Documentos en la base de datos '{self.nombre}':")
        for clave, documento in self.documentos.items():
            print(f"Clave: {clave}, Documento: {documento}")


# Ejemplo de uso:
bd = BDNoRelacional("MiBaseDeDatosNoRelacional")

# Insertar documentos
bd.insertar_documento("1", {"nombre": "Alice", "edad": 30, "ciudad": "New York"})
bd.insertar_documento("2", {"nombre": "Bob", "edad": 28, "ciudad": "Los Angeles"})

# Listar documentos
bd.listar_documentos()

# Obtener documento por clave
bd.obtener_documento("1")

# Eliminar documento por clave
bd.eliminar_documento("2")

# Intentar obtener un documento eliminado
bd.obtener_documento("2")
