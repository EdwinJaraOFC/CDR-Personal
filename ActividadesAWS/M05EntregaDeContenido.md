<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 5: Entrega de Contenido</h1>
</p>

## Finalidad del módulo
Obtendremos información sobre la red de entrega de contenido (CDN) de Amazon Web Services (AWS), Amazon CloudFront. 

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| Amazon CloudFront  | <p align="justify">Servicio CDN rápida que entrega datos, aplicaciones e interfaces de programación de aplicaciones (API) de forma segura a clientes de todo el mundo con baja latencia y altas velocidades de transferencia.</p>  |
| AWS Direct Connect  |  <p align="justify">Proporciona la capacidad de establecer una conexión de red dedicada/privada desde su entorno en las instalaciones a AWS.</p> |
| Almacenamiento en caché  | <p align="justify">Almacena los datos solicitados con frecuencia en ubicaciones de borde para que se pueda acceder a ellos con mayor rapidez.</p>  |
| Red de entrega de contenido (CDN)  | <p align="justify">Sistema de servidores distribuidos (red) que entrega páginas y contenido web a un usuario, en función de las ubicaciones geográficas del usuario, el origen de la página web y el servidor de entrega de contenido.</p>  |
| Distribución  | <p align="justify">Indica a CloudFront donde obtener la información almacenada en caché y cómo administrar la entrega de contenido.</p>  |
| Ubicación de borde  | <p align="justify">Sitio en el que se pueden almacenar los datos para reducir la latencia.</p>  |
| Origen  | <p align="justify">Tipo complejo que describe el bucket de AmazonS3, el servidor de protocolo de transferencia de hipertexto (HTTP).</p>  |

## Laboratorio: Uso de CloudFront como CDN para un sitio web
### Objetivo
Configurar una distribución de CloudFront y adjuntarla a un sitio web.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b09a4749-2478-4a77-b359-d392c6c76284">
</p>

### Preguntas
<p align="justify">
  
#### ¿Hubo algún paso para crear un bucket de S3 o adjuntar una distribución de CloudFront que necesite una explicación más detallada? ¿Dónde cree que puede buscar para obtener más información sobre esa parte del proceso?
No es necesario una explicación más detallada, puedo encontrar más información en la documentación de AWS.
#### ¿Por qué sería importante tener una red de distribución en la nube como CloudFront para una empresa de streaming de video o streaming de audio, como Hulu o Spotify?
Porque mejora la rapidez de la entrega de contenido, maneja eficientemente el tráfico masivo y simultáneo de usuarios, y proporciona una experiencia de usuario óptima y segura.
#### En base a lo que ha aprendido sobre las redes de distribución en la nube, ¿qué pensará o sentirá cuando un sitio web responda lentamente o un video tarde mucho en almacenarse en búfer?
"Esta situación subraya la importancia de tener una buena CDN para entregar contenido de manera eficiente y rápida".
#### ¿Qué tipos de datos cree que es más importante almacenar en caché para una distribución rápida?
Los archivos estáticos, como las página web estáticas, también contenidos multimedia.
</p>
