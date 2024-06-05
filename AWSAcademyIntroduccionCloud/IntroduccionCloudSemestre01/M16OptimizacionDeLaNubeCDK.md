<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 16: Optimización de la nube con AWS CDK</h1>
</p>

## Finalidad del módulo
Exploraremos el kit de desarrollo de la nube de AWS (AWS CDK) y cómo se integra con los servicios de la consola de administración de AWS. Desarrollaremos un artefacto computacional que demuestre su comprensión.

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| Kit de desarrollo de la nube de AWS (AWS CDK)  | <p align="justify">Marco de desarrollo de software de código que modela y aprovisiona recursos de aplicaciones en la nube mediante lenguajes de programación conocidos..</p>  |

## Antecedentes

El aprovisionamiento de aplicaciones en la nube puede ser un proceso desafiante que requiere que los usuarios realicen acciones manuales, escriban scripts personalizados, mantengan plantillas o aprendan lenguajes específicos de dominio. AWS CDK utiliza la familiaridad y el poder expresivo de los lenguajes de programación para aplicaciones de modelado. Proporciona a los usuarios componentes de alto nivel que preconfiguran los recursos de la nube con valores predeterminados comprobados, para que puedan crear aplicaciones en la nube sin necesidad de ser expertos. AWS CDK aprovisiona los recursos de forma segura y repetible a través de AWS CloudFormation. También permite a los usuarios componer y compartir sus propios componentes personalizados que incorporan los requisitos de su organización, lo que les ayuda a comenzar nuevos proyectos más rápido. AWS CDK reduce el trabajo de definición y configuración de recursos de red en comparación con el uso de Amazon CloudFront solamente.

Beneficios

AWS CDK acelera la incorporación a Amazon Web Services (AWS) porque hay muy pocas cosas nuevas que aprender. Con AWS CDK, puede utilizar las habilidades y herramientas existentes y aplicarlas a la tarea de crear infraestructura en la nube. También proporciona componentes de alto nivel que preconfiguran recursos en la nube con valores predeterminados comprobados, lo que ayuda a los usuarios a crear en AWS sin necesidad de ser expertos.

AWS CDK proporciona a los usuarios el poder expresivo de los lenguajes de programación para definir la infraestructura. Las características conocidas, como objetos, bucles y condiciones, aceleran el proceso de desarrollo. Los usuarios también pueden utilizar AWS CDK con su entorno de desarrollo integrado (IDE) para aprovechar las herramientas de productividad y los marcos de pruebas existentes.

Con AWS CDK, los usuarios pueden diseñar sus propios componentes reutilizables que cumplan los requisitos de seguridad, conformidad y gobernanza de su organización. Al igual que con cualquier otra biblioteca de software, los usuarios pueden compartir componentes en su organización, lo que les permite comenzar rápidamente nuevos proyectos con las prácticas recomendadas de forma predeterminada.

AWS CDK permite a los usuarios crear una aplicación en la nube sin salir de su IDE. Los usuarios pueden escribir su código de tiempo de ejecución y definir sus recursos de AWS con el mismo lenguaje de programación. La administración de la infraestructura como código proporciona grandes beneficios y, a menudo, es un paso importante para la aplicación exitosa de las prácticas de DevOps. De esta forma, en lugar de confiar en los pasos realizados manualmente, tanto los administradores como los desarrolladores pueden automatizar el aprovisionamiento de los servicios informáticos, de almacenamiento, de red y de aplicaciones que requieren sus aplicaciones, mediante archivos de configuración.

Por ejemplo, definir la infraestructura como código permite:

Mantener el código de la infraestructura y la aplicación en el mismo repositorio.
Hacer que los cambios de infraestructura sean repetibles y predecibles en distintos entornos, cuentas de AWS y regiones de AWS.
Replicar la producción en un entorno de almacenamiento provisional para permitir pruebas continuas.
Replicar la producción en un entorno de pruebas de rendimiento utilizado solo durante el tiempo necesario para ejecutar una prueba de esfuerzo.
Liberar los cambios de infraestructura utilizando las mismas herramientas que los cambios de código para que las implementaciones incluyan actualizaciones de infraestructura.
Aplicar las prácticas recomendadas de desarrollo de software a la administración de infraestructuras, como las revisiones de código o la implementación de pequeños cambios, con frecuencia.
Fuente de la imagen: https://aws.amazon.com/cdk/
Fuente de la imagen: https://aws.amazon.com/cdk/

Construcciones

Las construcciones son componentes en la nube que codifican los detalles de configuración, plantilla y lógica de adherencia para utilizar uno o varios servicios de AWS. AWS CDK proporciona una biblioteca de componentes fijos que cubren muchos servicios y características de AWS, lo que permite a los usuarios definir la infraestructura de sus aplicaciones a un alto nivel. Además, las construcciones son ajustables y componibles. Los usuarios pueden cambiar rápidamente cualquiera de los parámetros o codificar su propia construcción personalizada.

AWS CDK también proporciona construcciones de bajo nivel denominadas Recursos de CFN, que representan directamente los recursos de CloudFormation de nivel básico y proporcionan una forma de definir CloudFormation con un lenguaje de programación. Los recursos de CFN proporcionan una cobertura completa de los recursos de CloudFormation y están disponibles poco después de que se actualice un recurso de CloudFormation o esté disponible de nuevo.

Con AWS CDK, cualquier persona puede personalizar, compartir y reutilizar construcciones dentro de su organización o comunidad, como ocurre con cualquier otra biblioteca de software. Esto permite a los usuarios crear construcciones que ayudan a comenzar más rápido e incorporar las prácticas recomendadas de forma predeterminada.

AWS CDK permite a los usuarios definir su infraestructura mediante código y aprovisionarla a través de CloudFormation. Obtienen todas las ventajas de CloudFormation, incluida la implementación repetible, restauración rápida y detección de desviaciones.

AWS CDK permite a los usuarios modelar la infraestructura de aplicaciones mediante TypeScript, Python, Java (versión preliminar para desarrolladores) y .NET (versión preliminar para desarrolladores). Con AWS CDK, los desarrolladores pueden utilizar IDE, herramientas de prueba y patrones de flujo de trabajo existentes. Mediante el uso de herramientas como autocompletar y documentación en línea, AWS CDK permite a los usuarios pasar menos tiempo cambiando entre la documentación del servicio y su código.

AWS CDK permite a los usuarios referenciar sus activos de código de tiempo de ejecución en el mismo proyecto con el mismo lenguaje de programación. Por ejemplo, pueden incluir su código de tiempo ejecución de AWS Lambda o la imagen de contenedor Docker en un proyecto de AWS CDK y, cuando implementan su aplicación, el marco de AWS CDK carga y configura automáticamente el servicio de AWS con sus activos de tiempo de ejecución. Una vez finalizada la implementación de AWS CDK, tendrán una aplicación totalmente funcional.

La interfaz de línea de comandos (CLI) de AWS CDK permite a los usuarios interactuar con sus aplicaciones AWS CDK y facilita la funcionalidad, como sintetizar una plantilla de CloudFormation, mostrar las diferencias entre la pila en ejecución y los cambios propuestos, confirmar los cambios relacionados con la seguridad antes de la implementación e implementar varias pilas en varios entornos.

Fuente de la imagen: https://aws.amazon.com/blogs/aws/aws-cloud-development-kit-cdk-typescript-and-python-are-now-generally-available/
Fuente de la imagen: https://aws.amazon.com/blogs/aws/aws-cloud-development-kit-cdk-typescript-and-python-are-now-generally-available/
