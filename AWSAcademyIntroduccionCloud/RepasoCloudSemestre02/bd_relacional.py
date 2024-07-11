class BDRelacional:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablas = {}

    def crear_tabla(self, nombre_tabla, columnas):
        if nombre_tabla not in self.tablas:
            self.tablas[nombre_tabla] = {
                'columnas': columnas,
                'filas': []
            }
            print(f"Tabla '{nombre_tabla}' creada con columnas: {columnas}")
        else:
            print(f"La tabla '{nombre_tabla}' ya existe")

    def insertar_registro(self, nombre_tabla, registro):
        if nombre_tabla in self.tablas:
            self.tablas[nombre_tabla]['filas'].append(registro)
            print(f"Registro insertado en la tabla '{nombre_tabla}': {registro}")
        else:
            print(f"La tabla '{nombre_tabla}' no existe")

    def listar_registros(self, nombre_tabla):
        if nombre_tabla in self.tablas:
            registros = self.tablas[nombre_tabla]['filas']
            print(f"Registros en la tabla '{nombre_tabla}':")
            for registro in registros:
                print(registro)
        else:
            print(f"La tabla '{nombre_tabla}' no existe")

    def eliminar_tabla(self, nombre_tabla):
        if nombre_tabla in self.tablas:
            del self.tablas[nombre_tabla]
            print(f"Tabla '{nombre_tabla}' eliminada correctamente")
        else:
            print(f"La tabla '{nombre_tabla}' no existe")


# Ejemplo de uso:
bd = BDRelacional("MiBaseDeDatos")

# Crear tabla
bd.crear_tabla("Usuarios", ["id", "nombre", "edad"])

# Insertar registros
bd.insertar_registro("Usuarios", {"id": 1, "nombre": "Alice", "edad": 30})
bd.insertar_registro("Usuarios", {"id": 2, "nombre": "Bob", "edad": 28})

# Listar registros
bd.listar_registros("Usuarios")

# Eliminar tabla
bd.eliminar_tabla("Usuarios")

# Intentar listar registros de una tabla eliminada
bd.listar_registros("Usuarios")