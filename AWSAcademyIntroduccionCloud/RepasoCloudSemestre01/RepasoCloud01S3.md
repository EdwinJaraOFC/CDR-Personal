<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Tema: S3</h1>
</p>

Alojamiento de sitios web estáticos
Pregunta: Describe cómo se puede utilizar Amazon S3 para alojar sitios web estáticos. ¿Cuáles son los pasos necesarios para configurar un bucket de S3 para alojamiento web?

Amazon S3 puede alojar diferentes tipos de objetos, entre ellos los sitios web estáticos, S3 a través de múltiples instancias o buckets puede almacenar múltiples páginas web mediante indicadores únicos. Para configurar un bucket de S3 para alojar un sitio web debemos seguir los siguientes pasos:


Ejercicio 1: Creación y gestión de un bucket de Amazon S3
Objetivo: Crear un bucket de Amazon S3 y gestionar objetos dentro de él. Instrucciones:
Inicia sesión en AWS Management Console.

Navega a Amazon S3.

Crea un nuevo bucket con un nombre único.

Sube varios archivos al bucket.

Organiza los archivos en carpetas dentro del bucket.

Configura permisos para que algunos archivos sean públicos y otros privados.

Elimina uno de los archivos del bucket.


Preguntas:
¿Qué configuraciones adicionales puedes aplicar al bucket?
Podemos habilitar el alojamiento de sitios web estáticos.
Podemos editar la política del bucket para agregar ciertos permisos que necesitemos.
Activar el control de versiones de buckets.
¿Cómo se gestionan los permisos para los archivos en el bucket?
Mediante las políticas que se le asignan al bucket.
Mediante roles y políticas de IAM.
Mediante ACL (Access Control List)

Código
Introducción a Amazon S3
Buckets y Objetos
Simula la creación y gestión de buckets y objetos.

class S3Bucket:
def __init__(self):
self.buckets = {}

def create_bucket(self, name):
self.buckets[name] = {}

def put_object(self, bucket, key, data):
if bucket in self.buckets:
self.buckets[bucket][key] = data

def get_object(self, bucket, key):
return self.buckets.get(bucket, {}).get(key, None)

# Ejemplo de uso
s3 = S3Bucket()
s3.create_bucket('mybucket')
s3.put_object('mybucket', 'file1.txt', 'Hello, S3 Bucket!')
print(s3.get_object('mybucket', 'file1.txt'))
# Output: 'Hello, S3 Bucket!'

Gestión de objetos en un Bucket
Permisos de acceso
Simula el manejo de permisos mediante un diccionario de permisos.

class S3BucketWithPermissions(S3Bucket):
def __init__(self):
super().__init__()
self.permissions = {}

def set_permission(self, bucket, key, permission):
if bucket not in self.permissions:
self.permissions[bucket] = {}
self.permissions[bucket][key] = permission

def check_permission(self, bucket, key, action):
return self.permissions.get(bucket, {}).get(key) == action

# Ejemplo de uso
s3p = S3BucketWithPermissions()
s3p.create_bucket('mybucket')
s3p.put_object('mybucket', 'file1.txt', 'Hello, S3 with Permissions!') 
s3p.set_permission('mybucket', 'file1.txt', 'read') 
print(s3p.check_permission('mybucket', 'file1.txt', 'read')) # Output: True




Versionado
Pregunta: Explica el concepto de versionado en Amazon S3 y cómo se configura. ¿Cuáles son las ventajas de habilitar el versionado en un bucket?
El versionado ocurre a nivel de bucket y aplica a todos los objetos almacenados en él.
Se puede configurar al crear el bucket


Lab Learner
Ejercicio 2: Configuración de versionado en un Bucket de Amazon S3
Objetivo: Configurar el versionado en un bucket de Amazon S3 y observar cómo se manejan las versiones de los objetos.
Instrucciones:
Utiliza el bucket creado en el ejercicio anterior.
Habilita el versionado para el bucket.
Sube un archivo con el mismo nombre varias veces y observa cómo se gestionan las versiones
Elimina una versión específica del archivo.
Restaura una versión anterior del archivo.


Preguntas:
¿Qué ventajas tiene habilitar el versionado en un bucket?
Evitar sobreescribir archivos
Nos permite recuperar versiones anteriores

¿Cómo puedes recuperar una versión eliminada accidentalmente?
Borrandolo de la carpeta de borrados

4.1. Implementación de Versionado
Simula el versionado de objetos con una lista.

