<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 7: Seguridad I</h1>
</p>

## Finalidad del módulo
Obtendremos información general sobre la seguridad en la nube en relación con AWS Identity and Access Management (IAM). Esto incluye información sobre las prácticas recomendadas, los roles, los usuarios, las políticas y los grupos de seguridad.

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| AWS Identity and Acces Management (IAM)  | <p align="justify">Implica aplicar controles para los usuarios que necesitan acceder a recursos informáticos.</p>  |
|  Rol | <p align="justify">Una identidad de IAM que puede crear en su cuenta y que tiene permisos específicos.</p>  |
| Usuario  |  <p align="justify">Una entidad que se crea en AWS para representar a la persona o aplicación que la utiliza y que interactúa con AWS. Un usuario de AWS está compuesto por un nombre y credenciales.</p> |
| Grupo de seguridad  | <p align="justify">Actúa como firewall virtual de la instancia para controlar el tráfico entrante y saliente.</p> |
| Política  | <p align="justify">Objeto de AWS que, cuando se asocia a una identidad o un recurso, define sus permisos. AWS evalúa estas políticas cuando una entidad principal (usuario o rol) realiza una solicitud.</p> |
| Amazon Inspector  | <p align="justify">Ayuda a los clientes a identificar llas vulnerabilidades de seguridad y las desviaciones de las prácticas recomendadas de seguridad en las aplicaciones, antes de que se implementen y mientras se ejecutan en un entorno de producción.</p>  |
| Grupo  | <p align="justify">Un grupo de IAM es un conjunto de usuarios de IAM. Los grupos le permiten especificar permisos a varios usuarios, lo que puede facilitar la administración de permisos de dichos usuarios.</p>  |
| Usuario Raíz  | <p align="justify">Cuando crea una cuenta de AWS por primera vez, comienza con una identidad de inicio de sesión único que tiene acceso total a todos los servicios y recursos de AWS en la cuenta.</p>  |
| Credencial  | <p align="justify">Las credenciales de seguridad de AWS verifican quién es usted y si tiene permiso para acceder a los recursos que solicita.</p>  |
| Habilitación de Multi-Factor Authentication (MFA)  | <p align="justify">Este enfoque de autenticación requiere que se autentifiquen dos o más datos independientes.</p>  |
| Notación de objetos JavaScript (JSON)  | <p align="justify">Sintaxis para almacenar e intercambiar datos.</p>  |
| Multi-Factor Authentication (MFA)  |  <p align="justify">Sistema de seguridad que requiere más de un método de autenticación de categorías independientes de credenciales para verificar la identidad del usuario para un inicio de sesión u otra transacción.</p> |

## Antecedentes
IAM aplica controles a los usuarios que necesitan acceder a los recursos informáticos. Una sola cuenta de AWS puede tener servicios administrados por decenas de personas diferentes que pueden estar en distintos departamentos u oficinas, tener diferentes responsabilidades o niveles de antigüedad, e incluso estar en distintos países. Para mantener un entorno seguro en la nube con todas estas variables en cuestión, es esencial seguir las prácticas recomendadas de IAM.

### Prácticas recomendadas de IAM

**1. Bloquee las claves de acceso de usuario raíz de la cuenta de AWS:** <br>
La clave de acceso del usuario raíz de su cuenta de AWS le da acceso completo a todos sus recursos en todos los servicios de AWS, incluso a su información de facturación. No puede reducir los permisos asociados a la clave de acceso de usuario raíz de su cuenta de AWS. Por lo tanto, proteja su clave de acceso de usuario raíz como lo haría con los números de su tarjeta de crédito o cualquier otra información secreta confidencial.

**2. Cree usuarios individuales de IAM:** <br>
Al crear usuarios IAM individuales para las personas que acceden a su cuenta, puede dar a cada usuario de IAM un conjunto exclusivo de credenciales de seguridad. También puede conceder permisos diferentes a cada usuario de IAM. Si es necesario, puede cambiar o revocar los permisos de un usuario de IAM en cualquier momento.

**3. Utilice grupos de usuarios para asignar permisos a los usuarios de IAM:** <br>
Cree grupos que se relacionen con las funciones del trabajo (administradores, desarrolladores, contadores, etc.). A continuación, defina los permisos pertinentes para cada grupo. Por último, asigne usuarios de IAM a esos grupos. Todos los usuarios de un grupo de IAM heredan los permisos asignados al grupo.

**4. Conceda menos privilegios:** <br>
Cuando cree políticas de IAM, siga los consejos de seguridad estándar de conceder menos privilegios o conceder solo los permisos necesarios para realizar una tarea. Determine qué deben hacer los usuarios (y roles) y, a continuación, cree políticas que les permitan realizar solo esas tareas.

**5. Comience a utilizar los permisos con las políticas administradas de AWS:** <br>
Si desea comenzar rápidamente, puede utilizar las políticas administradas de AWS para otorgar a sus empleados los permisos que necesitan para comenzar. Estas políticas ya están disponibles en su cuenta, y AWS se encarga de mantenerlas y actualizarlas.Las políticas administradas de AWS le facilitarán la tarea de asignar de los permisos adecuados a los usuarios, grupos de usuarios y roles en lugar de tener que escribir las políticas usted mismo.

**6. Valide sus políticas:** <br>
Es una práctica recomendada que valide las políticas que crea. Puede realizar la validación de políticas cuando crea y edita políticas JSON. IAM identifica cualquier error de sintaxis JSON, mientras que IAM Access Analyzer proporciona más de 100 comprobaciones de políticas y recomendaciones procesables para ayudarlo a crear políticas seguras y funcionales.

**7. Utilice políticas administradas por el cliente en lugar de políticas en línea:** <br>
Una ventaja clave del uso de estas políticas es que puede ver todas las políticas administradas en un solo lugar. Las políticas integradas son aquellas que solo existen en una identidad de IAM (usuario, grupo de usuarios o rol).

**8. Utilice los niveles de acceso para revisar los permisos de IAM:** <br>
Para mejorar la seguridad de su cuenta de AWS, debe revisar y supervisar periódicamente cada una de sus políticas de IAM. Asegúrese de que sus políticas otorguen la menor cantidad de privilegios necesarios para llevar a cabo solo las acciones necesarias.

**9. Configure una política de contraseñas seguras para los usuarios:** <br>
Puede utilizar la política de contraseñas para definir requisitos de contraseña, como la longitud mínima, si requiere caracteres no alfabéticos, con qué frecuencia debe cambiarla, etc.

**10. Habilite la MFA:** <br>
Solicite la autenticación multifactor (MFA) para todos los usuarios de su cuenta. Con la MFA, los usuarios tendrán un dispositivo que generará una respuesta a un desafío de autenticación. Se requieren tanto las credenciales del usuario como la respuesta generada por el dispositivo para completar el proceso de inicio de sesión. Si la contraseña o las claves de acceso de un usuario se ven comprometidas, los recursos de la cuenta seguirán estando seguros gracias al requisito de autenticación adicional.

**11. Utilice roles para aplicaciones que se ejecutan en instancias de Amazon EC2:** <br>
Las aplicaciones que se ejecutan en una instancia EC2 necesitan credenciales para acceder a otros servicios de AWS. Para proporcionar credenciales a la aplicación de forma segura, utilice roles de IAM. Un rol es una entidad que tiene su propio conjunto de permisos, pero no es un usuario ni un grupo de usuarios.

**12. Utilice roles para delegar permisos:** <br>
No comparta credenciales de seguridad entre cuentas con el fin de permitir que los usuarios de otra cuenta de AWS accedan a los recursos de su cuenta de AWS. En su lugar, use roles de IAM. Puede definir un rol que especifique qué permisos tienen los usuarios de IAM en la otra cuenta. También puede designar qué cuentas de AWS cuentan con los usuarios de IAM que pueden asumir el rol.

**13. No comparta claves de acceso:** <br>
Las claves de acceso proporcionan acceso mediante programación a AWS. No comparta estas credenciales de seguridad entre los usuarios de su cuenta de AWS. En el caso de las aplicaciones que necesitan acceso a AWS, configure el programa para recuperar credenciales de seguridad temporales mediante un rol de IAM.

**14. Cambie las credenciales regularmente:** <br>
Cambie sus propias contraseñas y claves de acceso con frecuencia y asegúrese de que todos los usuarios de IAM de su cuenta también lo hagan. De esta forma, si una contraseña o clave de acceso se ve comprometida sin su conocimiento, podrá limitar el tiempo de uso de las credenciales para acceder a sus recursos.

**15. Elimine credenciales innecesarias:** <br>
Elimine las credenciales de usuario de IAM (contraseñas y claves de acceso) que no sean necesarias.

**16. Utilice las condiciones de la política para obtener mayor seguridad:** <br>
Defina las condiciones en las que las políticas de IAM permiten el acceso a un recurso.

**17. Supervise la actividad de su cuenta de AWS:** <br>
Puede utilizar las funciones de registro de AWS para determinar las acciones que realizaron los usuarios en su cuenta y los recursos que se utilizaron. Los archivos de registro muestran la hora y la fecha de las acciones, la IP de origen de una acción, qué acciones fallaron debido a permisos inadecuados y más.

### Identidades de AWS

Cuando se piensa en IAM en AWS, hay roles, identidades y grupos, y todos ellos se rigen por políticas.

En el nivel más alto se encuentra el usuario raíz. El usuario raíz tiene acceso a todos los aspectos de AWS y actúa como administrador universal. Nunca se deben dar a conocer las credenciales del usuario raíz y tampoco se recomienda que el creador de la cuenta realice tareas cotidianas como usuario raíz. En su lugar, se debe utilizar la cuenta del usuario raíz para crear una cuenta de administrador. Solo se deben realizar pocas tareas como usuario raíz, como cambiar el plan de AWS Support o cerrar una cuenta.

Los roles de IAM son similares a los usuarios, ya que son identidades de AWS con políticas de permisos para determinar qué puede o no puede hacer la identidad en AWS. Sin embargo, un rol no tiene asociadas credenciales, como una contraseña o claves de acceso. En vez de estar asociado únicamente a una persona, el rol está pensado para asignarse a cualquiera que lo necesite. Un usuario de IAM puede asumir un rol y adquirir temporalmente diferentes permisos para una tarea específica. Los roles son útiles en los casos en que una aplicación móvil accede a sus datos de AWS. No es deseable que todas las personas que utilicen esa aplicación tengan credenciales para su cuenta de AWS, aunque sí necesitan algún tipo de acceso a los datos cuando la utilizan. Si se asigna un rol cuando el usuario inicia sesión, se le otorga un acceso temporal con algunos permisos, pero sin credenciales permanentes.

Anteriormente, se mencionó las políticas en relación con los permisos que se pueden asignar a un grupo. Cuando una política se adjunta a un usuario,rol o grupo, se definen sus permisos. Las políticas se almacenan en AWS como documentos JSON. Es una práctica recomendada asignar políticas a los grupos y luego asignar cada usuario y rol a un grupo al crearlos. De esta forma, puede eliminar o cambiar rápidamente los permisos sin tener que modificar cada usuario o rol individual.

## Laboratorio: Introducción a IAM
### Objetivo
Diferenciar entre un rol, un usuario y una política en la seguridad en la nube.

### Tarea 1: Analizar los usuarios y grupos
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d569d0e7-bccc-407a-a9b3-0a12b1e8abeb)
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/29fec384-b5a3-477c-b645-7e70b616c2b0)

### Tarea 2: Agregar usuarios a los grupos
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ac808453-664c-4920-878a-6a6316750b42)

### Tarea 3: Iniciar sesión y probar los usuarios
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/420ae6a2-d8cd-4f27-87c9-af63fe8d4a86)

