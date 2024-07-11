import os

class BlockStorage:
    """
    Almacenamiento en bloque (Block Storage).

    Simula un almacenamiento en bloque con archivos binarios en Python.
    """
    def __init__(self, size):
        """
        Inicializa el almacenamiento en bloque con un tamaño específico.
        """
        self.storage = bytearray(size)
    
    def write(self, data, offset):
        """
        Escribe datos en el almacenamiento en bloque a partir de una posición específica.
        """
        try:
            self.storage[offset:offset+len(data)] = data
        except IndexError:
            raise IndexError("Offset fuera de límites del almacenamiento.")

    def read(self, offset, size):
        """
        Lee datos del almacenamiento en bloque a partir de una posición específica.
        """
        return bytes(self.storage[offset:offset+size])

    def delete(self, offset, size):
        """
        Borra datos del almacenamiento en bloque desde una posición específica.
        """
        self.storage[offset:offset+size] = bytearray(size)


class FileStorage:
    """
    Almacenamiento de Archivos (File Storage).

    Simula un sistema de archivos básico con directorios y archivos.
    """
    def __init__(self, root_dir):
        """
        Inicializa el sistema de almacenamiento de archivos con un directorio raíz.
        """
        self.root_dir = root_dir
        os.makedirs(root_dir, exist_ok=True)
    
    def write(self, path, data):
        """
        Escribe datos en un archivo dentro del sistema de almacenamiento.
        """
        with open(os.path.join(self.root_dir, path), 'w') as f:
            f.write(data)
    
    def read(self, path):
        """
        Lee datos de un archivo dentro del sistema de almacenamiento.
        """
        with open(os.path.join(self.root_dir, path), 'r') as f:
            return f.read()

    def list_files(self):
        """
        Lista todos los archivos almacenados en el sistema de archivos.
        """
        files = []
        for root, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                files.append(os.path.relpath(os.path.join(root, filename), self.root_dir))
        return files


class ObjectStorage:
    """
    Almacenamiento de Objetos (Object Storage).

    Simula el almacenamiento de objetos usando un diccionario.
    """
    def __init__(self):
        """
        Inicializa el almacenamiento de objetos.
        """
        self.storage = {}

    def put_object(self, key, data):
        """
        Almacena un objeto en el almacenamiento usando una clave única.
        """
        self.storage[key] = {'data': data, 'versions': {}}
    
    def get_object(self, key):
        """
        Recupera un objeto del almacenamiento usando su clave.
        """
        return self.storage.get(key, None)

    def put_object_version(self, key, data, version):
        """
        Almacena una versión específica de un objeto en el almacenamiento.
        """
        if key in self.storage:
            self.storage[key]['versions'][version] = data
        else:
            raise KeyError(f"Object with key '{key}' not found in storage.")

# Ejemplos de uso

# BlockStorage
print("BlockStorage:")
block_storage = BlockStorage(1024)
block_storage.write(b"Hello", 0)
print(block_storage.read(0, 5))  # Output: b'Hello'
block_storage.delete(0, 5)
print(block_storage.read(0, 5))  # Output: b'\x00\x00\x00\x00\x00'
print("")

# FileStorage
print("FileStorage:")
file_storage = FileStorage('/tmp/filestorage')
file_storage.write("example.txt", "Hello, File Storage!")
print(file_storage.read("example.txt"))  # Output: 'Hello, File Storage!'
print(file_storage.list_files())  # Output: ['example.txt']
print("")

# ObjectStorage
print("ObjectStorage:")
object_storage = ObjectStorage()
object_storage.put_object('file1.txt', 'Hello, Object Storage!')
print(object_storage.get_object('file1.txt'))  # Output: 'Hello, Object Storage!'
object_storage.put_object_version('file1.txt', 'Updated data', 'v2')
print(object_storage.get_object('file1.txt'))  # Output: {'data': 'Hello, Object Storage!', 'versions': {'v2': 'Updated data'}}