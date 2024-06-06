<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Tema: IAM</h1>
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
