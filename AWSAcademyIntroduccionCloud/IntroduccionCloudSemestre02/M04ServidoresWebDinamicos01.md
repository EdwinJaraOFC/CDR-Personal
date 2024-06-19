<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 4: Servidores web dinámicos I</h1>
</p>

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| Sitio Web estático  | <p align="justify">Sitio web que no cambia en función a las interacciones del usuario, generalmente se crea mediante HTML y CSS.</p>  |
| Sitio Web dinámico  | <p align="justify">Sitio web que cambia en función a las interacciones del usuario, generalmente se crea mediante Python, JavaScript, PHP o ASP con HTML.</p>  |

## Conceptos
Los siguientes diagramas ilustran cómo funcionan los sitios web estáticos y dinámicos.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/85d7f8bd-d73a-4960-98cf-4768375c9807" width="800">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ea5703b9-2d2b-4cea-a659-492f6dce94b1" width="800">
</p>

## Laboratorio del módulo 4: configuración de un sitio web estático
### Tarea 1: Crear y configurar un bucket como sitio web
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7bc23f5a-5c85-44bd-8b68-2392a5b6cc54)

### Tarea 2: Editar la configuración del bloqueo del acceso público
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/0ceef286-f506-4cc0-8e3b-3b71d4052473)

### Tarea 3: Agregar una política de buckets para el acceso público
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForGetBucketObjects",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::EXAMPLE-BUCKET/*"
            ]
        }
    ]
}
```

### Tarea 4: Cargar un documento índice
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e9eff574-7848-4c9a-b21d-ccbc3503c07f)

### Tarea 5: Probar el sitio web
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/3aea68c0-3bd5-40b1-89f5-28f31193212c)

