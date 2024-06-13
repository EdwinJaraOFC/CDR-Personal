<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Temas: IAM, S3</h1>
</p>

## La Cuenta Root y la implementación de MFA
Discute la importancia de la cuenta root en AWS y las mejores prácticas para asegurarla, incluyendo la implementación de MFA (Multi-Factor Authentication).

### Cuenta root en AWS
Cuenta principal que se crea al registrarse por primera vez en AWS.

### Usuario raíz
Es la persona que creó la cuenta en AWS. Para crear la cuenta usamos un correo electrónico y una contraseña.

### Importancia de la cuenta root
- Acceso completo a todos los servicios y recursos de AWS.
- Desde la cuenta root podemos crear usuarios adicionales (usuarios IAM).

### MFA (Multi-Factor Authentication)
- Seguridad
- Más de un método de autenticación

### Implementación en código
```
class IAMService:
    def __init__(self):
        self.users = {} 
        self.groups = {}
        self.policies = {}
        self.roles = {}

    def create_user(self, iam_service, user_name):
        iam_service.users[user_name] = {'policies': [], 'mfa_enabled': False}
        print(f"User '{user_name}' created.")

    def enable_mfa_for_user(self, iam_service, user_name):
        if user_name in iam_service.users:
            iam_service.users[user_name]['mfa_enabled'] = True
            print(f"MFA enabled for user '{user_name}'.")
        else:
            print("Usuario no encontrado")

    def deactivate_mfa_for_user(self, iam_service, user_name):
        if user_name in iam_service.users:
            iam_service.users[user_name]['mfa_enabled'] = False
            print(f"MFA deactivated for user '{user_name}'.")
        else:
            print("Usuario no encontrado")

    def mostrar(self, iam_service):
        for user in iam_service.users:
            print(f"User {user} , {iam_service.users[user]}" )
            

iam_service = IAMService()
iam_service.create_user(iam_service, "alice")
iam_service.create_user(iam_service, "massiel")
iam_service.enable_mfa_for_user(iam_service, "alice")
iam_service.mostrar(iam_service)

iam_service.deactivate_mfa_for_user(iam_service, "alice")
iam_service.mostrar(iam_service)
```

## Laboratorio de AWS Lab Learner
### Ejercicio 3: Definición y asignación de políticas IAM
Crea una política personalizada que otorgue permisos específicos a un bucket de S3. Asigna esta política a un usuario o grupo y verifica que los permisos funcionen correctamente.

1. Ejemplo
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b7ad5965-c5aa-4948-b2da-51c03b4cd5e3" width="1000">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/8b5c018f-1fb8-4039-bd43-db785e2ad840" width="1000">
</p>

2. Crear política
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ab69ace3-fa19-4693-9bee-f616486b4a3d" width="800">
</p>

3. Acciones
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f49f3df9-f587-4d23-84fe-b8bd910eca76" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a976be39-3f26-4d45-a815-bc71bd75ecb5" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/cfd7dfd2-8207-4ea4-b27e-9fb251ee348f" width="800">
</p>

## Configuración de MFA (Multi-Factor Authentication)
Describe el proceso de configuración de MFA para una cuenta root y un usuario IAM. ¿Por qué es importante habilitar MFA?

### MFA (Multi-Factor Authentication)
Mecanismo que solicita verificar tu identidad utilizando más de un conjunto de credenciales. MFA usa dos verificaciones secretas separadas para verificar tu identidad: algo que sabe y algo que tiene.

| Configuración MFA para cuenta root  | Configuración MFA para usuario IAM  |
| :------------: | :------------: |
| <p align="justify">1. Inicie sesión en la AWS Management Console.</p>  | <p align="justify">1. Inicie sesión en la AWS Management Console y abra la consola de IAM</p>  |
| <p align="justify">2. En la parte derecha de la barra de navegación, elija su nombre de cuenta y seleccione Security Credentials (Credenciales de seguridad).</p>  | <p align="justify">2. En el panel de navegación, seleccione Users (Usuarios), elija el nombre de usuario de IAM y seleccione Security Credentials (Credenciales de seguridad).</p>  |
| <p align="justify">3. En la sección Multi-Factor Authentication (MFA), elija Assign MFA device (Asignar dispositivo MFA).</p>  | <p align="justify">3. En la sección Multi-Factor Authentication (MFA), elija Assign MFA device (Asignar dispositivo MFA).</p>  |
| <p align="justify">4. En el asistente, escriba un Nombre de dispositivo, elija Aplicación del autenticador y luego, Siguiente.<br>- IAM generará y mostrará la información de configuración del dispositivo MFA virtual, incluido un gráfico de código QR.</p>  | <p align="justify">4. En el asistente, escriba un Nombre de dispositivo, elija Aplicación del autenticador y luego, Siguiente.<br>- IAM generará y mostrará la información de configuración del dispositivo MFA virtual, incluido un gráfico de código QR.</p>  |
| <p align="justify">5. Abra la aplicación de MFA virtual en el dispositivo.<br>- Si la aplicación de MFA virtual admite varios dispositivos o cuentas de MFA, elija la opción para crear un nuevo dispositivo o cuenta de MFA virtual.</p>  | <p align="justify">5. Abra la aplicación de MFA virtual en el dispositivo.<br>- Si la aplicación de MFA virtual admite varios dispositivos o cuentas de MFA, elija la opción para crear un nuevo dispositivo o cuenta de MFA virtual.</p>  |
| <p align="justify">6. Verifique si la aplicación MFA admite códigos QR y, a continuación, lleve a cabo alguna de las siguientes operaciones:<br>- Escanear el código QR desde el asistente.<br>- Introducir manualmente la clave secreta desde el asistente.</p>  | <p align="justify">6. Verifique si la aplicación MFA admite códigos QR y, a continuación, lleve a cabo alguna de las siguientes operaciones:<br>- Escanear el código QR desde el asistente.<br>- Introducir manualmente la clave secreta desde el asistente.</p>  |
| <p align="justify">7. Cuando haya terminado, el dispositivo MFA virtual comenzará a generar contraseñas de uso único.</p>  | <p align="justify">7. Cuando haya terminado, el dispositivo MFA virtual comenzará a generar contraseñas de uso único.</p>  |
| <p align="justify">8. En el asistente, en el cuadro Código MFA 1, escriba la contraseña de uso único que aparece actualmente en el dispositivo MFA virtual. Espere hasta 30 segundos y escriba la otra contraseña de uso único en el cuadro MFA code 2 (Código MFA 2). Elija Add MFA (Agregar MFA).</p>  | <p align="justify">8. En el asistente, en el cuadro Código MFA 1, escriba la contraseña de uso único que aparece actualmente en el dispositivo MFA virtual. Espere hasta 30 segundos y escriba la otra contraseña de uso único en el cuadro MFA code 2 (Código MFA 2). Elija Add MFA (Agregar MFA).</p>  |
| <strong>El dispositivo MFA virtual ya está listo para utilizarlo con AWS.</strong>  | <strong>El dispositivo MFA virtual ya está listo para utilizarlo con AWS.</strong>  |

### ¿Por qué es importante habilitar MFA?
El proceso de configuración de la Autenticación Multifactor (MFA) para una cuenta root de AWS y un usuario del IAM (AWS Identity and Access Management) es importante para agregar una capa adicional de seguridad y proteger los recursos de AWS de accesos no autorizados.

### Implementación en código
```
import random

class IAMService:
    def __init__(self):  # Inicializa las estructuras de datos
        self.users = {}
        self.groups = {}
        self.roles = {}
        self.policies = {}

    def create_user(self, user_name):  # Crea un nuevo usuario
        self.users[user_name] = {'groups': [], 'roles': [], 'mfa_enabled': False, 'policies': []}
        print(f"Usuario '{user_name}' creado.")

    def create_group(self, group_name):  # Crea un nuevo grupo
        self.groups[group_name] = set()
        print(f"Grupo '{group_name}' creado.")

    def create_role(self, role_name):  # Crea un nuevo rol
        self.roles[role_name] = set()
        print(f"Rol '{role_name}' creado.")

    def create_policy(self, policy_name):  # Crea una nueva política
        self.policies[policy_name] = []
        print(f"Política '{policy_name}' creada.")

    def add_user_to_group(self, user_name, group_name):  # Agrega un usuario a un grupo
        if user_name in self.users and group_name in self.groups:
            self.users[user_name]['groups'].append(group_name)
            self.groups[group_name].add(user_name)
            print(f"Usuario '{user_name}' agregado al grupo '{group_name}'.")
        else:
            print("Usuario o grupo no encontrado")

    def add_user_to_role(self, user_name, role_name):  # Agrega un usuario a un rol
        if user_name in self.users and role_name in self.roles:
            self.users[user_name]['roles'].append(role_name)
            self.roles[role_name].add(user_name)
            print(f"Usuario '{user_name}' agregado al rol '{role_name}'.")
        else:
            print("Usuario o rol no encontrado")

    def attach_policy_to_user(self, user_name, policy_name):  # Asigna una política a un usuario
        if user_name in self.users and policy_name in self.policies:
            self.users[user_name]['policies'].append(policy_name)
            print(f"Política '{policy_name}' asignada al usuario '{user_name}'.")
        else:
            print("Usuario o política no encontrada")

    def enable_mfa(self, user_name):  # Habilita MFA para un usuario
        if user_name in self.users:
            self.send_verification_code(user_name)
            self.users[user_name]['mfa_enabled'] = True
            print(f"MFA configurada para el usuario '{user_name}'.")
        else:
            print("Usuario no encontrado")

    def disable_mfa(self, user_name):  # Deshabilita MFA para un usuario
        if user_name in self.users:
            self.users[user_name]['mfa_enabled'] = False
            print(f"MFA desactivada para el usuario '{user_name}'.")
        else:
            print("Usuario no encontrado")

    def generate_verification_code(self, length=6):  # Genera un código de verificación
        code = ""
        for _ in range(length):
            code += str(random.randint(0, 9))
        return code

    def send_verification_code(self, user_name):  # Envía códigos de verificación
        code1 = self.generate_verification_code()
        code2 = self.generate_verification_code()
        print(f"Enviando códigos de verificación a {user_name}: {code1}, {code2}")
        print("Los códigos de verificación caducarán en 1 minuto.")

    def show_info(self, user_name):  # Muestra información de usuarios, grupos, roles y políticas
        if user_name in self.users:
            self.print_users_info()
            self.print_groups_info()
            self.print_roles_info()
            self.print_policies_info()
        else:
            print("Usuario no encontrado")

    def print_users_info(self):  # Imprime información de usuarios
        print("Información de usuarios:")
        print("self.users =", self.users)

    def print_groups_info(self):  # Imprime información de grupos
        print("\nInformación de grupos:")
        print("self.groups =", {group: list(self.groups[group]) for group in self.groups})

    def print_roles_info(self):  # Imprime información de roles
        print("\nInformación de roles:")
        print("self.roles =", {role: list(self.roles[role]) for role in self.roles})

    def print_policies_info(self):  # Imprime información de políticas
        print("\nInformación de políticas:")
        print("self.policies =", self.policies)

iam_service = IAMService()
iam_service.create_user("Massiel")
iam_service.create_user("Edwin")
print("\n")

iam_service.create_group("admins")
iam_service.create_role("developer")
iam_service.create_policy("admin_policy")
iam_service.create_policy("developer_policy")
print("\n")

iam_service.add_user_to_group("Massiel", "admins")
iam_service.add_user_to_role("Massiel", "developer")
iam_service.attach_policy_to_user("Massiel", "admin_policy")
iam_service.attach_policy_to_user("Massiel", "developer_policy")
iam_service.enable_mfa("Massiel")
print("\n")

iam_service.show_info("Massiel")
print("\n")

iam_service.add_user_to_group("Edwin", "admins")
iam_service.add_user_to_role("Edwin", "developer")
iam_service.attach_policy_to_user("Edwin", "admin_policy")
iam_service.attach_policy_to_user("Edwin", "developer_policy")
iam_service.enable_mfa("Edwin")
print("\n")

iam_service.show_info("Edwin")
print("\n")

iam_service.disable_mfa("Massiel")
iam_service.disable_mfa("Edwin")
print("\n")

iam_service.show_info("Edwin")
```

## Laboratorio de AWS Lab Learner
### Ejercicio 2: Configuración de MFA para usuarios IAM
Configura MFA para un usuario IAM y documenta el proceso, incluyendo cómo verificar el estado de MFA y cómo manejar la autenticación de doble factor.

1. Inicie sesión en la AWS Management Console y abra la consola de IAM.
2. En el panel de navegación, seleccione Users (Usuarios).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/1816a8c2-e839-4d62-b110-f07a43d5d275" width="900">
</p>

3. En la lista Users (Usuarios), elija el nombre de usuario de IAM.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b5b4ef4c-696b-427d-b9a4-3e34f5469844" width="900">
</p>

4. Elija la pestaña Security credentials (Credenciales de seguridad). En Multi-factor authentication (MFA), seleccione Assign MFA device (Asignar dispositivo MFA).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/63136d97-a158-4b19-b393-c620914d1a6a" width="900">
</p>

5. En el asistente, escriba un Nombre de dispositivo, elija Aplicación del autenticador y luego, Siguiente.
- IAM generará y mostrará la información de configuración del dispositivo MFA virtual, incluido un gráfico de código QR.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a28b206f-c53a-4c01-ae85-8195a27d72c5" width="700">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/625b263b-00e6-46bf-aca2-b32e97218d34" width="700">
</p>

- Authenticator app
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/20ac3094-a59a-4fed-b9b6-78345008bef1" width="700">
</p>

- Security Key
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7b05fa17-b7af-4498-8d0d-61723e302489" width="700">
</p>

- Hardware TOTP token
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/57a906ef-4989-4b8a-ae9d-37e160b6a927" width="700">
</p>

6. Abra su aplicación de MFA virtual.
- Si la aplicación de MFA virtual admite varios dispositivos o cuentas de MFA, elija la opción para crear un nuevo dispositivo o cuenta de MFA virtual.
7. Verifique si la aplicación MFA admite códigos QR y, a continuación, lleve a cabo alguna de las siguientes operaciones:
- Escanear el código QR desde el asistente.
- Introducir manualmente la clave secreta desde el asistente.
8. Cuando haya terminado, el dispositivo MFA virtual comenzará a generar contraseñas de uso único.
9. En la página Configurar el dispositivo, en el cuadro Código MFA 1, escriba la contraseña de uso único que aparece actualmente en el dispositivo MFA virtual. Espere hasta 30 segundos y escriba la otra contraseña de uso único en el cuadro MFA code 2 (Código MFA 2). Elija Add MFA (Agregar MFA).

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/6ed3a63e-f988-4383-9652-0f4059bfe8f6" width="700">
</p>
<p align= "center">https://www.youtube.com/watch?v=7Gy1Ps_vC80&t=287s</p>
<strong>Ahora el dispositivo MFA virtual ya está listo para utilizarlo con AWS.</strong>


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
- En Jamstack, usamos JavaScript para manejar la lógica de la aplicación, las interacciones del usuario y la actualización del contenido sin necesidad de recargar la página completa.
- Las API permiten que tu sitio web obtenga datos y funcionalidades de otros lugares en internet. En lugar de tener toda la información y lógica en tu propio servidor, con Jamstack, tu sitio web se conecta a diferentes servicios externos usando JavaScript.
- En Jamstack, este HTML se genera previamente (pre compilado) y se sirve como archivos estáticos. Esto significa que el servidor no tiene que generar el HTML cada vez que alguien visita la página, lo que hace que el sitio sea mucho más rápido.

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
Para alojar sitios web dinámicos en AWS, podemos utilizar la arquitectura "Jamstack" (JavaScript, APIs y Markup). En Jamstack, S3 se utiliza para almacenar y servir los archivos estáticos (HTML, CSS, JavaScript, imágenes).
Los componentes dinámicos se manejan mediante:
 - AWS Lambda para ejecución de código sin servidor (lógica de back-end y funciones serverless).
 - Amazon API Gateway para crear y gestionar APIs que interactúan con Lambda y otros servicios.
 - Amazon RDS o DynamoDB para bases de datos.

Amazon CloudFront actúa como una capa de entrega y aceleración:
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
        self.buckets = {} # Diccionario para almacenar los buckets
        
    def create_bucket(self, name): # Crea un nuevo bucket vacío con el nombre especificado
        self.buckets[name] = {}

    def put_object(self, bucket, key, data): # Agrega un nuevo objeto al bucket
        if bucket in self.buckets:
            self.buckets[bucket][key] = data

    def get_object(self, bucket, key): # Obtiene el contenido de un objeto en un bucket específico
        if bucket in self.buckets:
            if key in self.buckets[bucket]:
                return self.buckets[bucket][key]
        return None

    def list_objects(self, bucket): # Lista todos los objetos en un bucket específico
        if bucket in self.buckets:
            return list(self.buckets[bucket].keys())
        return []

    def delete_object(self, bucket, key): # Elimina un objeto específico de un bucket
        if bucket in self.buckets:
            if key in self.buckets[bucket]:
                del self.buckets[bucket][key]

# Ejemplo de uso
s3 = S3Bucket()
s3.create_bucket('website')
s3.put_object('website', 'index.html', '<!DOCTYPE html><html><body><h1>Mi Sitio Web</h1></body></html>')
s3.put_object('website', 'styles.css', 'body { background-color: green; }')
s3.put_object('website', 'script.js', 'console.log("Hola desde JavaScript");')

print(s3.get_object('website', 'index.html'))
# Output: '<!DOCTYPE html><html><body><h1>Mi Sitio Web</h1></body></html>'

print(s3.list_objects('website'))
# Output: ['index.html', 'styles.css', 'script.js']

s3.delete_object('website', 'script.js')
print(s3.list_objects('website'))
# Output: ['index.html', 'styles.css']
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
