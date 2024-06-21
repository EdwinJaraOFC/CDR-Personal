<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 10: Machine Learning</h1>
</p>

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| Algoritmo  | <p align="justify">Conjunto de reglas para un cálculo a seguir.</p>  |
| Aprendizaje profundo  | <p align="justify">Proceso de aprendizaje de IA en el que esta escanea la red neuronal artificial.</p>  |
| Pronóstico  | <p align="justify">Utilización de un algoritmo para analizar patrones de datos a fin de realizar predicciones.</p>  |
| Red neuronal  | <p align="justify">Modelo o algoritmo que se ha diseñado para tomar decisiones de una manera similar a la de un cerebro humano.</p>  |
| Refuerzo de aprendizaje  | <p align="justify">Tipo de ML que se basa en que el sistema informático mejora su toma de decisiones a medida que aprende de las recompensas que recibe.</p>  |
| Aprendizaje supervisado  | <p align="justify">Tipo de ML en el que el sistema informático aprende de fuentes de datos marcadas o etiquetadas por humanos.</p>  |
| Entrenamiento  | <p align="justify">Proceso de proporcionar más puntos de datos de ejemplo a un sistema informático para que pueda aprender.</p>  |
| Machine Learning (ML)  | <p align="justify">Rama de la IA en la que un algoritmo de cómputo puede modificar su propio comportamiento.</p>  |
| Aprendizaje sin supervisar  | <p align="justify">Tipo de ML en el que el sistema informático aprende a analizar patrones en puntos de datos sin etiqueta o sin estructura.</p>  |

## Conceptos
<p align="justify">El ML (aprendizaje automático) permite que las computadoras creen y actualicen algoritmos para mejorar en predicciones o tareas con el tiempo, pareciendo aprender de manera autónoma al procesar más datos. Esto se diferencia de los sistemas tradicionales, que requieren información e instrucciones específicas del programador. Dentro del ML, el aprendizaje por refuerzo es una categoría donde el algoritmo se programa inicialmente para alcanzar un objetivo y recibe recompensas a medida que aprende a ser más eficiente.</p>

Puede tener algunos conceptos erróneos sobre el ML. Corrijamos estos errores de razonamiento.

<p align="justify">La AI y el ML pueden confundirse con seres vivos o conscientes. Sin embargo, puede reforzar el concepto de que el ML es un esfuerzo por conseguir que las computadoras funcionen de manera similar a la mente humana; de hecho, los sistemas de ML a veces se denominan redes neuronales debido a la similitud. No obstante, el núcleo del ML es digital y no se encuentra vivo.</p>
<p align="justify">A veces, los sistemas informáticos se consideran aprendices o pensadores superiores a las personas. Aunque esto quizás sea verdad en el caso de la velocidad de procesamiento, los errores humanos más comunes también pueden estar presentes en el ML. Aquí, el principio de basura entra, basura sale es importante. El sistema de ML aún se basa en algoritmos y datos que se ven afectados por errores subyacentes. Por ejemplo, un banco puede intentar enseñar a una máquina a reconocer el fraude. Si los clientes realizan un mal trabajo al denunciar el fraude o presentan informes falsos, los datos harán que el sistema informático identifique el fraude de forma incorrecta.</p>

## Laboratorio del módulo 10: Aprendizaje por refuerzo con AWS DeepRacer
### Tarea 1: Crear un modelo
| Descripción General  | Imagen  |
| :------------: | :------------: |
| <p align="justify">En el aprendizaje por refuerzo para AWS DeepRacer, un agente (vehículo) aprende de un entorno (una pista) al interactuar con él y recibir recompensas por realizar acciones específicas.</p> <p align="justify">El proceso de entrenamiento del modelo simulará múltiples experiencias del vehículo en la pista en un intento de encontrar una política (una función que asigna el estado actual del agente a una decisión de conducción) que maximice la recompensa total promedio que experimenta el agente </p> <p align="justify">Después del entrenamiento, podrá evaluar el rendimiento del modelo en un nuevo entorno, implementar el modelo en un vehículo físico o enviar el modelo a un circuito virtual.</p>  | <p align= "center"><img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/4507f1b7-611a-4e51-9bfb-2e5e3f4b0ab1" width="500"></p>  |

#### Paso 1
- En la sección Training details (Detalles del entrenamiento), en la opción Model name (Nombre del modelo), ingrese un nombre para el modelo.
- En la sección Environment simulation (Simulación de entorno), elija la pista re:Invent 2018.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/cdc01d95-05a7-4fb7-9cb3-a1ca939e453f" width="900">
</p>

#### Paso 2
- Race type (Tipo de carrera): elija Time trial (Prueba contrarreloj), que es la opción predeterminada.
- Training algorithm and hyperparameters (Hiperparámetros y algoritmo de entrenamiento): elija PPO, que es la opción predeterminada.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a126d6b6-54b0-4d4f-8819-45e699ee36fe" width="900">
</p>

| ¿Por qué es importante el espacio de acción?  | Imagen  |
| :------------: | :------------: |
| <p align="justify">En el aprendizaje por refuerzo, el conjunto de todas las acciones válidas u opciones disponibles para un agente cuando interactúa con un entorno se denomina espacio de acción. En la consola de AWS DeepRacer, puede entrenar agentes en un espacio de acción discreto o continuo.</p><p align="justify">Al entrenar un modelo de AWS DeepRacer, el espacio de acción define qué combinaciones de velocidad y ángulo de dirección están disponibles para el agente. Una acción es una única combinación o opción de velocidad y ángulo de dirección que puede realizar un agente.</p>  | <p align= "center"><img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d788eb4a-d59c-499c-93eb-879962dfe143" width="900"></p>  |

#### Paso 3
- En la sección Select action space (Seleccionar espacio de acción), en la opción Action spaces (Espacios de acción), elija Continuous action space (Espacio de acción continuo), que es la opción predeterminada.

#### Paso 4
- Acepte el vehículo predeterminado (The Original DeepRacer) y elija Next (Siguiente).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/3d9d5f7a-c8db-45eb-b0d3-a36476285bb9" width="900">
</p>

#### Paso 5
- En la sección Automatically submit... (Enviar automáticamente...), desactive la opción Submit this model... (Enviar este modelo...).
- Lea y acepte la sección Terms and conditions (Términos y condiciones).
- Seleccione su país de residencia.
- Seleccione Create model (Crear modelo).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/dea145aa-cb56-46be-b21d-83468a641f49" width="900">
</p>

### Tarea 2: Evaluar la simulación
