<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Temas: IAM, S3</h1>
</p>

## 1. La Cuenta Root y la implementación de MFA
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

## 2. Laboratorio de AWS Lab Learner
### Ejercicio 3: Definición y asignación de políticas IAM
Crea una política personalizada que otorgue permisos específicos a un bucket de S3. Asigna esta política a un usuario o grupo y verifica que los permisos funcionen correctamente.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b7ad5965-c5aa-4948-b2da-51c03b4cd5e3" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/8b5c018f-1fb8-4039-bd43-db785e2ad840" width="800">
</p>

## 3. Configuración de MFA (Multi-Factor Authentication)
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

def generarCodigoVerificacion(length=6):
  codigo = ""
  for _ in range(length):
    codigo += str(random.randint(0, 9))
  return codigo

def enviarCodigoVerificacion(userName, code):
  print(f"Enviando código de verificación a {userName}: {code}")

def configuracionMFA(userName):
  if not userName:
    print("El nombre de usuario no es válido.")
    return
    
  code = generarCodigoVerificacion()
  enviarCodigoVerificacion(userName, code)
  print(f"MFA configurada para el usuario '{userName}'.")
  print("El código de verificación caducará en 5 minutos.")

configuracionMFA("Edwin Jara")
```

## 4. Laboratorio de AWS Lab Learner
### Ejercicio 2: Configuración de MFA para usuarios IAM
Configura MFA para un usuario IAM y documenta el proceso, incluyendo cómo verificar el estado de MFA y cómo manejar la autenticación de doble factor.

1. Inicie sesión en la AWS Management Console y abra la consola de IAM.
2. En el panel de navegación, seleccione Users (Usuarios).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/1816a8c2-e839-4d62-b110-f07a43d5d275" width="800">
</p>

3. En la lista Users (Usuarios), elija el nombre de usuario de IAM.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b5b4ef4c-696b-427d-b9a4-3e34f5469844" width="800">
</p>

4. Elija la pestaña Security credentials (Credenciales de seguridad). En Multi-factor authentication (MFA), seleccione Assign MFA device (Asignar dispositivo MFA).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/63136d97-a158-4b19-b393-c620914d1a6a" width="800">
</p>

5. En el asistente, escriba un Nombre de dispositivo, elija Aplicación del autenticador y luego, Siguiente.
- IAM generará y mostrará la información de configuración del dispositivo MFA virtual, incluido un gráfico de código QR.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a28b206f-c53a-4c01-ae85-8195a27d72c5" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/625b263b-00e6-46bf-aca2-b32e97218d34" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/20ac3094-a59a-4fed-b9b6-78345008bef1" width="800">
</p>
- Authenticator app
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a28b206f-c53a-4c01-ae85-8195a27d72c5" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/625b263b-00e6-46bf-aca2-b32e97218d34" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/20ac3094-a59a-4fed-b9b6-78345008bef1" width="800">
</p>
- Security Key
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a28b206f-c53a-4c01-ae85-8195a27d72c5" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/625b263b-00e6-46bf-aca2-b32e97218d34" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/20ac3094-a59a-4fed-b9b6-78345008bef1" width="800">
</p>
- Hardware TOTP token
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a28b206f-c53a-4c01-ae85-8195a27d72c5" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/625b263b-00e6-46bf-aca2-b32e97218d34" width="800">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/20ac3094-a59a-4fed-b9b6-78345008bef1" width="800">
</p>

6. Abra su aplicación de MFA virtual.
- Si la aplicación de MFA virtual admite varios dispositivos o cuentas de MFA, elija la opción para crear un nuevo dispositivo o cuenta de MFA virtual.
7. Verifique si la aplicación MFA admite códigos QR y, a continuación, lleve a cabo alguna de las siguientes operaciones:
- Escanear el código QR desde el asistente.
- Introducir manualmente la clave secreta desde el asistente.
8. Cuando haya terminado, el dispositivo MFA virtual comenzará a generar contraseñas de uso único.
9. En la página Configurar el dispositivo, en el cuadro Código MFA 1, escriba la contraseña de uso único que aparece actualmente en el dispositivo MFA virtual. Espere hasta 30 segundos y escriba la otra contraseña de uso único en el cuadro MFA code 2 (Código MFA 2). Elija Add MFA (Agregar MFA).
<strong>Ahora el dispositivo MFA virtual ya está listo para utilizarlo con AWS.</strong>
