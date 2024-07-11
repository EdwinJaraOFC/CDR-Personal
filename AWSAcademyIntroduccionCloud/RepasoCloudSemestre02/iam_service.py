import random

class IAMService:
    """
    Servicio de gestión de identidades y accesos (IAM).
    """
    def __init__(self):
        # Inicialización de los diccionarios para usuarios, grupos, políticas y roles.
        self.users = {}
        self.groups = {}
        self.policies = {}
        self.roles = {}

    def list_users(self):
        """
        Lista todos los usuarios.
        """
        return list(self.users.keys())

    def list_groups(self):
        """
        Lista todos los grupos.
        """
        return list(self.groups.keys())

    def generate_credential_report(self):
        """
        Genera un informe de credenciales de los usuarios.

        El informe incluye políticas asignadas y si MFA está activado para cada usuario.
        """
        report = {}
        for user in self.users:
            report[user] = {
                "Politicas": self.users[user].get('Politicas', []),
                "MFA-Activado": self.users[user].get('MFA-Activado', False),
                "Roles": self.users[user].get('Roles', [])
            }
        print("Credencial reportada:", report)


class IAMConsole:
    """
    Consola para interactuar con el servicio IAM.
    """
    def create_user(self, iam_service, user_name):
        """
        Crea un nuevo usuario.
        """
        try:
            # Verifica si el usuario ya existe en el servicio IAM
            if user_name in iam_service.users:
                raise ValueError(f"El usuario '{user_name}' ya existe.")
            # Crea el usuario en el servicio IAM
            iam_service.users[user_name] = {'Politicas': [], 'Roles': [], 'MFA-Activado': False}
            print(f"Usuario '{user_name}' creado.")
        except ValueError as e:
            print(f"Error: {e}")

    def create_group(self, iam_service, group_name):
        """
        Crea un nuevo grupo.
        """
        try:
            # Verifica si el grupo ya existe en el servicio IAM
            if group_name in iam_service.groups:
                raise ValueError(f"El grupo '{group_name}' ya existe.")
            # Crea el grupo en el servicio IAM
            iam_service.groups[group_name] = {'Politicas': [], 'Roles': [], 'Usuarios': []}
            print(f"Grupo '{group_name}' creado.")
        except ValueError as e:
            print(f"Error: {e}")

    def create_policy(self, iam_service, policy_name, permissions):
        """
        Crea una nueva política.
        """
        try:
            # Verifica si la política ya existe en el servicio IAM
            if policy_name in iam_service.policies:
                raise ValueError(f"La política '{policy_name}' ya existe.")
            # Crea la política en el servicio IAM
            iam_service.policies[policy_name] = {"Nombre": policy_name, "Permisos": permissions}
            print(f"Política '{policy_name}' creada.")
        except ValueError as e:
            print(f"Error: {e}")

    def create_role(self, iam_service, role_name):
        """
        Crea un nuevo rol.
        """
        try:
            # Verifica si el rol ya existe en el servicio IAM
            if role_name in iam_service.roles:
                raise ValueError(f"El rol '{role_name}' ya existe.")
            # Crea el rol en el servicio IAM
            iam_service.roles[role_name] = {'Politicas': [], 'Usuarios': []}
            print(f"Rol '{role_name}' creado.")
        except ValueError as e:
            print(f"Error: {e}")

    def add_user_to_group(self, iam_service, user_name, group_name):
        """
        Añade un usuario a un grupo.
        """
        try:
            # Verifica si el usuario existe en el servicio IAM
            if user_name not in iam_service.users:
                raise ValueError(f"El usuario '{user_name}' no existe.")
            # Verifica si el grupo existe en el servicio IAM
            if group_name not in iam_service.groups:
                raise ValueError(f"El grupo '{group_name}' no existe.")
            
            # Añade el usuario al grupo
            iam_service.groups[group_name]['Usuarios'].append(user_name)
            print(f"Usuario '{user_name}' añadido al grupo '{group_name}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def assign_policy_to_user(self, iam_service, user_name, policy_name):
        """
        Asigna una política a un usuario.
        """
        try:
            # Verifica si el usuario existe en el servicio IAM
            if user_name not in iam_service.users:
                raise ValueError(f"El usuario '{user_name}' no existe.")
            # Verifica si la política existe en el servicio IAM
            if policy_name not in iam_service.policies:
                raise ValueError(f"La política '{policy_name}' no existe.")
            
            # Asigna la política al usuario
            iam_service.users[user_name]['Politicas'].append(iam_service.policies[policy_name])
            print(f"Política '{policy_name}' asignada al usuario '{user_name}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def assign_policy_to_group(self, iam_service, group_name, policy_name):
        """
        Asigna una política a un grupo.
        """
        try:
            # Verifica si el grupo existe en el servicio IAM
            if group_name not in iam_service.groups:
                raise ValueError(f"El grupo '{group_name}' no existe.")
            # Verifica si la política existe en el servicio IAM
            if policy_name not in iam_service.policies:
                raise ValueError(f"La política '{policy_name}' no existe.")
            
            # Asigna la política al grupo
            iam_service.groups[group_name]['Politicas'].append(iam_service.policies[policy_name])
            print(f"Política '{policy_name}' asignada al grupo '{group_name}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def assign_json_policy_to_user(self, iam_service, user_name, policy_json):
        """
        Asigna una política JSON a un usuario.
        """
        try:
            # Verifica si el usuario existe en el servicio IAM
            if user_name not in iam_service.users:
                raise ValueError(f"El usuario '{user_name}' no existe.")
            
            # Asigna la política JSON al usuario
            iam_service.users[user_name]['Politicas'].append(policy_json)
            print(f"Política JSON asignada al usuario '{user_name}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def assign_role_to_user(self, iam_service, user_name, role_name):
        """
        Asigna un rol a un usuario.
        """
        try:
            # Verifica si el usuario existe en el servicio IAM
            if user_name not in iam_service.users:
                raise ValueError(f"El usuario '{user_name}' no existe.")
            # Verifica si el rol existe en el servicio IAM
            if role_name not in iam_service.roles:
                raise ValueError(f"El rol '{role_name}' no existe.")
            
            # Asigna el rol al usuario
            iam_service.users[user_name]['Roles'].append(role_name)
            print(f"Rol '{role_name}' asignado al usuario '{user_name}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def assign_role_to_group(self, iam_service, group_name, role_name):
        """
        Asigna un rol a un grupo.
        """
        try:
            # Verifica si el grupo existe en el servicio IAM
            if group_name not in iam_service.groups:
                raise ValueError(f"El grupo '{group_name}' no existe.")
            # Verifica si el rol existe en el servicio IAM
            if role_name not in iam_service.roles:
                raise ValueError(f"El rol '{role_name}' no existe.")
            
            # Asigna el rol al grupo
            iam_service.groups[group_name]['Roles'].append(role_name)
            print(f"Rol '{role_name}' asignado al grupo '{group_name}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def set_password_policy(self, min_length, require_symbols, require_numbers):
        """
        Establece la política de contraseñas.
        """
        policy = {
            "min_length": min_length,
            "require_symbols": require_symbols,
            "require_numbers": require_numbers
        }
        print("Política de contraseñas establecida", policy)

def setup_mfa(user_name):
    """
    Configura la autenticación multifactor (MFA) para un usuario.
    """
    code = ""
    for _ in range(6):
        code += str(random.randint(0, 9))
    print(f"MFA configurado para el usuario '{user_name}'. Código de verificación: {code}")

def enable_mfa_for_user(iam_service, user_name):
    """
    Activa la MFA para un usuario.
    """
    try:
        # Verifica si el usuario existe en el servicio IAM
        if user_name not in iam_service.users:
            raise ValueError(f"El usuario '{user_name}' no existe.")
        
        # Activa MFA para el usuario
        iam_service.users[user_name]['MFA-Activado'] = True
        print(f"MFA activado para el usuario '{user_name}'.")
    except ValueError as e:
        print(f"Error: {e}")

import uuid
def generate_temporary_credentials():
    """
    Genera credenciales temporales (clave de acceso, clave secreta y token de sesión).
    """
    access_key = str(uuid.uuid4())
    secret_key = str(uuid.uuid4())
    session_token = str(uuid.uuid4())
    print(f"Credenciales temporales generadas:\nClave de Acceso: {access_key}\nClave Secreta: {secret_key}\nToken de Sesión: {session_token}")

# Generar credenciales temporales
generate_temporary_credentials()
print("")

# Crear instancia de IAMService y IAMConsole
iam_service = IAMService()
iam_console = IAMConsole()

# Crear usuario y grupo
iam_console.create_user(iam_service, "Edwin")
iam_console.create_group(iam_service, "Grupo-Admin")

# Crear políticas
iam_console.create_policy(iam_service, "Politica-Admin", ["s3:ListBucket", "ec2:StartInstances"])
iam_console.create_policy(iam_service, "Politica-Grupo-Admin", ["s3:*", "ec2:*"])
iam_console.create_policy(iam_service, "Politica-ReadOnly", ["s3:GetObject"])
iam_console.create_policy(iam_service, "Politica-Write", ["s3:PutObject"])
print("")

# Añadir usuario al grupo
iam_console.add_user_to_group(iam_service, "Edwin", "Grupo-Admin")

# Asignar políticas a usuario y grupo
iam_console.assign_policy_to_user(iam_service, "Edwin", "Politica-Admin")
iam_console.assign_policy_to_group(iam_service, "Grupo-Admin", "Politica-Grupo-Admin")
iam_console.assign_policy_to_user(iam_service, "Edwin", "Politica-ReadOnly")
iam_console.assign_policy_to_group(iam_service, "Grupo-Admin", "Politica-Write")
print("")

# Asignar política JSON a usuario
example_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example_bucket"
        }
    ]
}
iam_console.assign_json_policy_to_user(iam_service, "Edwin", example_policy)
print("")

# Asignar roles a usuario y grupo
iam_console.assign_role_to_user(iam_service, "Edwin", "Role-Admin")
iam_console.assign_role_to_group(iam_service, "Grupo-Admin", "Role-ReadOnly")
print("")

# Establecer política de contraseñas
iam_console.set_password_policy(8, True, True)
print("")

# Activar MFA para el usuario
enable_mfa_for_user(iam_service, "Edwin")

# Configurar MFA para el usuario
setup_mfa("Edwin")
print("")

# Generar informe de credenciales
iam_service.generate_credential_report()
