<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Tema: S3</h1>
</p>

## Alojamiento de Sitios Web Estáticos
Describe cómo se puede utilizar Amazon S3 para alojar sitios web estáticos. ¿Cuáles son los pasos necesarios para configurar un bucket de S3 para alojamiento web?

## Sitios Web Estáticos y Arquitectura Jamstack en AWS
### Sitios Web Estáticos en AWS con Amazon S3
S3 está diseñado principalmente para almacenar y servir contenido estático, como archivos HTML, CSS, JavaScript, imágenes y videos.

### Ventajas de usar Amazon S3
- **Escalabilidad:** S3 maneja automáticamente el aumento de tráfico sin necesidad de intervención manual.
- **Costo-efectividad:** Solo pagas por el almacenamiento y la transferencia de datos que realmente utilizas.
- **Alta Disponibilidad y Durabilidad:** Los datos en S3 son altamente disponibles y duraderos.

### ¿Por qué Amazon S3 no aloja sitios web dinámicos?
S3 no es adecuado para alojar sitios web dinámicos por sí solo debido a las siguientes razones:

| Característica | Sitio Web Estático | Sitio Web Dinámico |
| :------------: | :------------: | :------------: |
| Generación de contenido | <p align="justify">Los archivos (HTML, CSS, JavaScript, imágenes) se sirven tal cual están almacenados en el servidor.</p> | <p align="justify">El contenido se genera dinámicamente en el servidor utilizando lenguajes de programación y bases de datos.</p> |
| Interacción con bases de datos | <p align="justify">No hay interacción con bases de datos ni procesamiento en el servidor.</p> | <p align="justify">Interactúa con bases de datos y realiza procesamiento en el servidor.</p> |
| Personalización de contenido | <p align="justify">El contenido es igual para todos los usuarios.</p> | <p align="justify">El contenido se personaliza según el usuario o la solicitud.</p> |
| Actualización de contenido | <p align="justify">Los cambios en el contenido requieren actualizar manualmente los archivos.</p> | <p align="justify">El contenido se actualiza automáticamente mediante la lógica del servidor.</p> |
| Rendimiento y seguridad | <p align="justify">Generalmente más rápidos y seguros, pero con funcionalidad limitada.</p> | <p align="justify">Más funcionales y dinámicos, pero requieren más recursos del servidor.</p> |

### ¿Qué es Jamstack?
Jamstack es un modelo de desarrollo web que se enfoca en la velocidad, el rendimiento y la escalabilidad usando tecnologías modernas. Se basa en tres pilares fundamentales: JavaScript, API y Markup pre compilado.
- JavaScript delega la arquitectura al cliente, utilizando frameworks de desarrollo como React o Angular.
- Las API reemplazan la base de datos desde el servidor, utilizando servicios web accedidos vía HTTPS con JavaScript.
- El Markup pre compilado promueve la precompilación de vistas, templates y marcado, evitando la generación dinámica tradicional.

### Diferencias entre Jamstack y otras arquitecturas web
- En arquitecturas tradicionales, las solicitudes se procesan y se renderizan plantillas y contenido en HTML en cada petición.
- En Jamstack, el código fuente y el contenido se alojan en un repositorio como ficheros editables.
- Cada vez que se modifica el código o contenido, se ejecuta un proceso de pre renderización de todo el sitio web.
- El HTML pre generado se publica en la CDN de la aplicación, disponible para el navegador.

<div align="center"; style="display: flex; justify-content: space-between;">
 <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/2be8ebca-1b33-45c2-9fee-381f6ff79585" width="438px"/>
 <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/70f127ea-009f-4d3f-bc9a-795ba1d171d4" width="562px"/>
</div>

### Alojar sitios web dinámicos con AWS: Arquitectura Jamstack
- Para alojar sitios web dinámicos en AWS, se utiliza la arquitectura "Jamstack" (JavaScript, APIs y Markup).
- En Jamstack, S3 se utiliza para almacenar y servir los archivos estáticos (HTML, CSS, JavaScript, imágenes).
- Los componentes dinámicos se manejan mediante:
 - AWS Lambda para ejecución de código sin servidor (lógica de back-end y funciones serverless).
 - Amazon API Gateway para crear y gestionar APIs que interactúan con Lambda y otros servicios.
 - Amazon RDS o DynamoDB para bases de datos.
- Amazon CloudFront actúa como una capa de entrega y aceleración:
 - Optimiza la entrega de archivos estáticos alojados en S3.
 - Acelera las API y funciones serverless (Lambda y API Gateway) mediante caché inteligente.
 - Proporciona seguridad adicional contra ataques DDoS y tráfico malicioso (integración con AWS WAF).
 - Ofrece optimización de contenido (compresión, minimización, optimización de imágenes).

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

## Versionado
Explica el concepto de versionado en Amazon S3 y cómo se configura. ¿Cuáles son las ventajas de habilitar el versionado en un bucket?
- El versionado ocurre a nivel de bucket y aplica a todos los objetos almacenados en él.
- Se puede configurar al crear el bucket
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/8e04d289-ce3d-440d-9cff-35bed4d05b11)

## Laboratorio de AWS Lab Learner
### Ejercicio 2: Configuración de versionado en un Bucket de Amazon S3
Configura el versionado en un bucket de Amazon S3 y observar cómo se manejan las versiones de los objetos.

#### Instrucciones:
1. Utiliza el bucket creado en el ejercicio anterior. <br> Servicios > S3 > Crear bucket <br> Nombre:  Único, solo minúscula, empezar por letra o número, 3-63 caracteres, no se puede modificar el nombre, descriptivo
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ff4cc7e0-3854-4326-acd2-8f9ecf000a62" width="900">
</p>

2. Habilita el versionado para el bucket.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/922778ad-b7d3-42e5-8879-f7dc69bcdce5" width="900">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/8b4760e0-f51e-41f8-bc55-e4a33b1e8f3c" width="900">
</p>

3. Sube un archivo con el mismo nombre varias veces y observa cómo se gestionan las versiones
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/13b391d1-0354-429d-b0c9-30d704dd781c" width="900">
</p>

4. Elimina una versión específica del archivo.<br>
Con versionado habilitado
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/9fcafcac-c61b-428d-851e-6521e2815480" width="900">
</p>

Con versionado deshabilitado
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f2440259-9cc7-4f22-ab8d-4678b31bfe69" width="900">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a28b5ce4-70f4-45e8-98e5-b188b355dd63" width="900">
</p>

5. Restaura una versión anterior del archivo.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/78fa34c4-3eaa-470f-aa68-56bcd6bd2a84" width="900">
</p>

Archivo recuperado
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/985118b7-bc79-43eb-bf8c-694ad64731d0" width="900">
</p>

#### Preguntas:
¿Qué ventajas tiene habilitar el versionado en un bucket?
- Evitar sobreescribir archivos
- Nos permite recuperar versiones anteriores

¿Cómo puedes recuperar una versión eliminada accidentalmente?
- Borrandolo de la carpeta de borrados

## Código
### 4.1. Implementación de Versionado
Simula el versionado de objetos con una lista.
```
class S3Bucket:
    def __init__(self):
        self.buckets = {}

    #Método para crear bucket
    def create_bucket(self, name):
        self.buckets[name] = {}

    #Cargar un objeto al bucket
    def put_object(self, bucket, key, data):
        if bucket in self.buckets:
            self.buckets[bucket][key] = data

    #Metodo  para mostrar el objeto
    def get_object(self, bucket, key):
        return self.buckets.get(bucket, {}).get(key, None)
    
class S3BucketWithVersioning(S3Bucket):
    def __init__(self):
        super().__init__()
        self.versions = {}

    #Método para crear versiones del objeto
    def put_object(self, bucket, key, data):
        if bucket not in self.versions:
            self.versions[bucket] = {}
        if key not in self.versions[bucket]:
            self.versions[bucket][key] = []

        self.versions[bucket][key].append(data)

    #Método para mostrar versiones del objeto
    def get_object(self, bucket, key, version=None):
        if version is None:
            return self.versions.get(bucket, {}).get(key, [])[-1]
        return self.versions.get(bucket, {}).get(key, [])[version]

# Ejemplo de uso
s3=S3Bucket()
s3.create_bucket('mybucket')
s3.put_object('mybucket', 'file1.txt', 'Hello, S3 Bucket!')
print(s3.get_object('mybucket', 'file1.txt')) # Output: 'Hello, S3 Bucket!'


s3v = S3BucketWithVersioning()
s3v.create_bucket('mybucket')
s3v.put_object('mybucket', 'file1.txt', 'Version 1')
s3v.put_object('mybucket', 'file1.txt', 'Version 2')
print(s3v.get_object('mybucket', 'file1.txt')) # Output: 'Version 2'
print(s3v.get_object('mybucket', 'file1.txt', 0)) # Output: 'Version 1'
```
