<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 14: Facturación y soporte</h1>
</p>

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| Calculadora de costo mensual de AWS  |  <p align="justify">Proporciona una factura mensual estimada basada en los requisitos informáticos y de almacenamiento del usuario.</p> |
| Plan AWS Support  |  <p align="justify">Los planes de soporte están diseñados para brindarle la combinación adecuada de herramientas y acceso a la experiencia para que pueda tener éxito en AWS optimizando el rendimiento, administrando el riesgo y manteniendo los costos bajo control.</p> |
| AWS Organizations  |  <p align="justify">Lo ayuda a administrar la facturación de forma centralizada; controlar el acceso, la conformidad y la seguridad, y compartir recursos entre sus cuentas de AWS.</p> |
| Facturación unificada  | <p align="justify">Puede unificar la facturación y los pagos de varias cuentas de AWS. Cada organización de Organizations tiene una cuenta de administración (pagador) que paga los cargos de todas las cuentas miembro.</p>  |
| Gerente técnico de cuenta (TAM)  | <p align="justify">Este asistente y asesor en la nube dedicado para cuentas de AWS de nivel empresarial responde a preguntas de soporte, monitorea su cuenta en la nube y ofrece recomendaciones para la optimización.</p>  |

## Antecedentes
<p align="justify">
AWS proporciona varios servicios útiles de facturación y soporte que ayudan a los usuarios de la nube a hacer un uso más eficiente de sus recursos. Estos servicios incluyen una calculadora para estimar los costos mensuales, paneles de facturación para visualizar los gastos y una serie de planes de soporte con precios y servicios diferentes. Para facilitar el pago de servicios a empresas grandes con muchas cuentas, Organizations permite la facturación unificada, lo que habilita a una cuenta a pagar el resto de las cuentas de la organización.</p>

<p align="justify">
Todos los clientes de AWS reciben el nivel básico de soporte sin costo adicional. Tenga en cuenta que solo las cuentas de nivel Enterprise reciben el beneficio de un TAM. Un TAM proporciona conocimientos técnicos a los clientes de nivel Enterprise sobre toda la gama de servicios de AWS y comprende de manera pormenorizada sus casos de uso y arquitecturas tecnológicas. Los TAM trabajan con los arquitectos de soluciones de AWS para ayudarlo a lanzar nuevos proyectos y lo asesoran en la aplicación de las prácticas recomendadas durante todo el ciclo de vida de la implementación. Usted dispone de una línea telefónica directa para comunicarse con su TAM, quien funciona como punto de contacto principal para atender a necesidades de soporte continuas.</p>

Organizations es un gran recurso con muchos beneficios. Al permitir que una organización vincule varias cuentas de AWS en una cuenta central, una persona puede:

- Administrar de manera centralizada las políticas de varias cuentas de AWS
- Gobernar el acceso a los servicios, los recursos y las regiones de AWS
- Automatizar la creación y la administración de cuentas de AWS
- Configurar los servicios de AWS de varias cuentas
- Unificar la facturación de varias cuentas de AWS

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7e6d72d7-6d88-48c5-a300-1664e3dc337f" width="800">
</p>

Una unidad organizativa (OU) es un contenedor para varias cuentas. Al asociar una política a una OU, esta se aplica a todas las cuentas de la OU.

## Laboratorio del módulo 14: Calculadora de precios de AWS
### Pasos del laboratorio
1. Diríjase a la Calculadora de precios y seleccione Create estimate (Crear una estimación).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/77c998e6-0fb4-4940-8786-eb17d983fdf0" width="800">
</p>

2. Para crear la estimación de costos de Amazon EC2, configure las siguientes opciones:
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/9e96cb1a-f389-4b80-a25b-7b652db06c9b" width="500">
</p>

3. En la ventana Configure Amazon EC2 (Configurar Amazon EC2), configure los siguientes detalles:
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b61c7d66-5d72-4471-95dd-ecbca6480c4a" width="800">
</p>

4. Para crear la estimación de costos de Amazon S3, en el área de búsqueda Find Service (Buscar servicio), escriba S3, luego, en la lista de resultados filtrados, en el cuadro Amazon Simple Storage Service (S3), elija Configure (Configurar).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a354363b-477b-4a91-b7cc-3a85d4332cff" width="500">
</p>

5. En la ventana Configure Amazon Simple Storage Service (S3) (Configurar Amazon Simple Storage Service [S3]), configure los siguientes detalles:
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/dc159a40-32f7-4a6d-92db-c3d968c51723" width="800">
</p>

6. Elija View summary (Ver resumen).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/89d3ae4b-65ca-4658-9dea-190ff037ec06" width="800">
</p>

7. Para agregar el costo del plan Basic Support a la estimación, elija Add support (Agregar soporte).


8. En la página Support estimate (Estimación de soporte), configure las siguientes opciones:


9. Para exportar la estimación, en Export (Exportar), elija el formato que prefiera. Por ejemplo, elija PDF. 


10. En el cuadro de diálogo que aparece, seleccione OK (Aceptar).


Como puede ver, la Calculadora de precios ofrece un conjunto de funciones que se pueden usar para crear una estimación del costo de los servicios de AWS cuando sabe qué servicios usará y cómo piensa usarlos.
