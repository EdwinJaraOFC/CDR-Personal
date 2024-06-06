<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Temas: IAM, S3</h1>
</p>

# Temas: IAM, S3
## La Cuenta Root y la implementación de MFA
Discute la importancia de la cuenta root en AWS y las mejores prácticas para asegurarla, incluyendo la implementación de MFA (Multi-Factor Authentication).

### Cuenta root en AWS
Cuenta principal que se crea al registrarse por primera vez en AWS.

#### Usuario raíz
Es la persona que creó la cuenta en AWS. Para crear la cuenta usamos un correo electrónico y una contraseña.

#### Importancia de la cuenta root
- Acceso completo a todos los servicios y recursos de AWS.
- Desde la cuenta root podemos crear usuarios adicionales (usuarios IAM).

#### MFA (Multi-Factor Authentication)
- Seguridad
- Más de un método de autenticación

#### Implementación en código
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
