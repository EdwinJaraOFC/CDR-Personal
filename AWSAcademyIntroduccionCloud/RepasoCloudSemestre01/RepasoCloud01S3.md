<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Tema: S3</h1>
</p>

## Alojamiento de sitios web estáticos
Describe cómo se puede utilizar Amazon S3 para alojar sitios web estáticos. ¿Cuáles son los pasos necesarios para configurar un bucket de S3 para alojamiento web?

| Característica | Sitio Web Estático | Sitio Web Dinámico |
| :------------: | :------------: | :------------: |
| Generación de contenido | Los archivos (HTML, CSS, JavaScript, imágenes) se sirven tal cual están almacenados en el servidor. | El contenido se genera dinámicamente en el servidor utilizando lenguajes de programación y bases de datos. |
| Interacción con bases de datos | No hay interacción con bases de datos ni procesamiento en el servidor. | Interactúa con bases de datos y realiza procesamiento en el servidor. |
| Personalización de contenido | El contenido es igual para todos los usuarios. | El contenido se personaliza según el usuario o la solicitud. |
| Actualización de contenido | Los cambios en el contenido requieren actualizar manualmente los archivos. | El contenido se actualiza automáticamente mediante la lógica del servidor. |
| Ejemplos | Sitios web simples, portafolios, blogs estáticos. | Sitios de comercio electrónico, aplicaciones web, redes sociales. |
| Rendimiento y seguridad | Generalmente más rápidos y seguros, pero con funcionalidad limitada. | Más funcionales y dinámicos, pero requieren más recursos del servidor. |
| Casos de uso | Adecuados para sitios con contenido estático o que no requiere actualizaciones frecuentes. | Adecuados para sitios con contenido dinámico y personalizado. |

Amazon S3 es una solución sencilla y económica para alojar sitios web estáticos en AWS, gracias a su capacidad de almacenamiento escalable y a la facilidad para configurar el alojamiento web y la distribución de contenido.

## Laboratorio de AWS Lab Learner
### Ejercicio 1: Creación y gestión de un bucket de Amazon S3
Crea un bucket de Amazon S3 y gestionar objetos dentro de él.
#### Instrucciones:
1. Inicia sesión en AWS Management Console.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ac7a12d9-fc81-4a19-9084-97ba4b3518a3" width="900">
</p>

2. Navega a Amazon S3.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/1125b5f0-9d55-47d9-91c4-82e8d3278eb4" width="900">
</p>

3. Crea un nuevo bucket con un nombre único.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7074df92-1305-47d2-ac88-6f96c14fe48c" width="900">
</p>

4. Sube varios archivos al bucket.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/6bb0e62b-de96-49a8-b173-2576e103d43b" width="900">
</p>

5. Organiza los archivos en carpetas dentro del bucket.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ec4ec1bc-c673-4bf2-99f5-8be8cef2eead" width="900">
</p>

6. Configura permisos para que algunos archivos sean públicos y otros privados.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/521fa02f-eca8-4619-aa28-8bd6b0bfa5a8" width="800">
</p>

7. Elimina uno de los archivos del bucket.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/44e18d89-41fe-4bae-a753-562c8cb16bb7" width="800">
</p>

#### Preguntas:
¿Qué configuraciones adicionales puedes aplicar al bucket?
- **Registro de acceso:** Registrar todas las solicitudes al bucket para análisis y auditoría.
- **Políticas de ciclo de vida:** Reglas para administrar el ciclo de vida de los objetos (moverlos a almacenamiento más económico, eliminarlos, etc.).
- **Replicación de objetos:** Replicar objetos en otros buckets, incluso en diferentes regiones para backup y recuperación.
- **Control de versiones:** Mantener múltiples versiones de un objeto en el mismo bucket.

¿Cómo se gestionan los permisos para los archivos en el bucket?
- Políticas de bucket
- Listas de Control de Acceso (ACL)

## Código
### Introducción a Amazon S3
#### Buckets y Objetos
Simula la creación y gestión de buckets y objetos.
```
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
```
### Gestión de objetos en un Bucket
#### Permisos de acceso
Simula el manejo de permisos mediante un diccionario de permisos.
```
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
```


## Versionado
Explica el concepto de versionado en Amazon S3 y cómo se configura. ¿Cuáles son las ventajas de habilitar el versionado en un bucket?
El versionado ocurre a nivel de bucket y aplica a todos los objetos almacenados en él.
Se puede configurar al crear el bucket


## Laboratorio de AWS Lab Learner
### Ejercicio 2: Configuración de versionado en un Bucket de Amazon S3
Configura el versionado en un bucket de Amazon S3 y observar cómo se manejan las versiones de los objetos.

#### Instrucciones:
1. Utiliza el bucket creado en el ejercicio anterior.
2. Habilita el versionado para el bucket.
3. Sube un archivo con el mismo nombre varias veces y observa cómo se gestionan las versiones
4. Elimina una versión específica del archivo.
5. Restaura una versión anterior del archivo.

#### Preguntas:
¿Qué ventajas tiene habilitar el versionado en un bucket?
- Evitar sobreescribir archivos
- Nos permite recuperar versiones anteriores

¿Cómo puedes recuperar una versión eliminada accidentalmente?
- Borrandolo de la carpeta de borrados

## Código
### 4.1. Implementación de Versionado
Simula el versionado de objetos con una lista.

