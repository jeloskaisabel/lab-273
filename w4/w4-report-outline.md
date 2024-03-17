## Item 2: Errores Potenciales
### 1. TCP Duplicate ACKs (Acknowledgments) (Frames 21, 23)

En el análisis de los paquetes de la captura de tráfico, se han detectado errores relacionados con TCP Duplicate ACKs (Acknowledgments) en los paquetes 21 y 23. Estos errores señalan la recepción de confirmaciones duplicadas de paquetes que fueron previamente enviados, lo cual sugiere la posible existencia de problemas relacionados con la congestión en la red o pérdida de paquetes.

En el paquete 21, se identificó un TCP Duplicate ACK #1, lo que indica que se recibió un duplicado del ACK asociado con el paquete número 19. El ACK relativo es 9577, lo que evidencia la recepción de datos hasta ese punto específico. Además, la ventana de recepción en este paquete es de 196, mostrando la capacidad del receptor para aceptar más datos. La presencia de un checksum no verificado resalta una falta de integridad en los datos transmitidos.

Por otro lado, en el paquete 23 se observó un TCP Duplicate ACK #2, indicando un segundo duplicado del ACK del paquete 19. Los valores de secuencia relativa, ACK relativo y ventana de recepción en este paquete fueron consistentes con el primer duplicado, confirmando la recepción de datos hasta la secuencia relativa 9577. Al igual que en el paquete anterior, la ventana de recepción es de 196, lo que indica la capacidad del receptor para aceptar más datos.

Ambos errores de Duplicate ACK (#1 y #2) reflejan un comportamiento atípico en la comunicación TCP, donde el receptor envía confirmaciones duplicadas consecutivas para el mismo paquete. Esta situación puede ser indicativa de problemas de congestión en la red, donde los ACKs se reenvían debido a la pérdida de paquetes o a la congestión en la ruta de entrega de los datos.

### 2. TCP Fast Retransmission (Frame 24)
El Frame 24 revela un evento de TCP Fast Retransmission, una acción tomada por el protocolo TCP cuando el receptor detecta la pérdida de un paquete o recibe tres ACK duplicados consecutivos. En lugar de esperar al tiempo de espera para retransmitir el paquete perdido, TCP realiza una retransmisión rápida para mejorar la eficiencia y reducir la latencia en la recuperación de datos perdidos.

Este hallazgo sugiere que ha ocurrido una pérdida de paquetes en la comunicación, posiblemente debido a congestión en la red, problemas en el enlace de comunicación o errores en los dispositivos de red. La rápida retransmisión busca garantizar la correcta entrega de datos al destino, aunque también puede señalar problemas de rendimiento o calidad en la conexión.

En cuanto al paquete específico del Frame 24, se trata de un segmento TCP de 1368 bytes enviado desde el puerto 80 al puerto 49683. Su número de secuencia relativa es 9577, indicando la secuencia en la que se envió en relación con otros segmentos. El campo de ACK en el paquete tiene un valor de 133, indicando que el receptor ha recibido los datos hasta el número de secuencia 133 y solicita el siguiente segmento con un número de secuencia de 10945.

El paquete también tiene activada la bandera PSH (Push), lo que indica una entrega urgente de los datos al proceso de aplicación receptor. Esto puede ser parte de la estrategia de retransmisión rápida para asegurar la pronta llegada de los datos perdidos al destino.

En relación con otros paquetes:

1. **Frame 23 (Duplicate ACK #2):** Este paquete es un ACK duplicado del paquete original perdido. La TCP Fast Retransmission se activa en respuesta a estos ACK duplicados para retransmitir rápidamente el paquete perdido.
2. **Frame 25 (ACK al paquete retransmitido):** Tras la retransmisión rápida en el Frame 24, se envía un ACK confirmando la recepción del paquete retransmitido.
3. **Frame 26 (ACK del paquete original):** Este paquete confirma la recepción del paquete original perdido, completando así el proceso de recuperación de la pérdida de datos.

## 3. Error de Captura de Segmento Anterior (Previous segment not captured) (Frame 20)
El error observado en el paquete del Frame 20 se manifiesta como la advertencia "Previous segment(s) not captured", indicando que los segmentos anteriores a este no fueron registrados en la trama de red. Esta advertencia es típica al iniciar una captura de tráfico, especialmente cuando se inicia después de que la comunicación TCP ya haya comenzado. La ausencia de estos segmentos previos dificulta el análisis completo de la secuencia de la comunicación TCP.

Esta advertencia se genera cuando los segmentos anteriores al actual no están disponibles en la captura de tráfico. Esta carencia de segmentos previos complica la comprensión total de la comunicación TCP, incluyendo aspectos críticos como la secuencia de datos, los números de secuencia y de acuse de recibo (ACK), entre otros elementos cruciales para el análisis de la interacción entre el emisor y el receptor.

La advertencia afecta la relación con los frames tanto anteriores como posteriores en la secuencia de la comunicación TCP. La falta de segmentos previos limita la capacidad de establecer una conexión lógica y completa entre estos frames. Es crucial destacar que esta advertencia es algo común al inicio de una captura y no necesariamente señala un problema grave en la comunicación. Más bien, indica una restricción en la información disponible para el análisis exhaustivo de la interacción TCP.


## Item 3: Calcular % paquetes perdidos
Los paquetes retransmitidos y los ACK duplicados son indicadores clave de pérdida de paquetes en una red TCP/IP. La pérdida de paquetes puede ocurrir debido a factores como congestión de red, errores en el enlace, o problemas en los dispositivos de red.

1. **Retransmisión de Paquetes:**
   - Cuando un paquete se pierde en la red, TCP espera un tiempo para recibir el ACK que confirma su recepción. Si este ACK no llega dentro del tiempo esperado, TCP retransmite el paquete. La detección de paquetes retransmitidos indica pérdida de paquetes en la red.

2. **ACKs Duplicados:**
   - Un ACK duplicado indica al emisor que se ha perdido un paquete y debe ser retransmitido. Esto ocurre cuando el receptor detecta la pérdida de un paquete o recibe un paquete fuera de secuencia.

Analizando los paquetes específicos proporcionados y su relación con estos indicadores:

- **Paquete 21 - TCP Duplicate ACK #1:**
  - Este paquete muestra un Duplicate ACK del paquete 19, indicando que el receptor no recibió el paquete original. Sugiere la pérdida del paquete 19 en la red.

- **Paquete 23 - TCP Duplicate ACK #2:**
  - Similar al paquete 21, muestra un Duplicate ACK del paquete 19, confirmando la pérdida persistente del paquete 19.

- **Paquete 24 - TCP Fast Retransmission:**
  - Indica una Fast Retransmission debido a la pérdida de paquetes o ACKs duplicados consecutivos. Confirma la pérdida del paquete 19 y su retransmisión rápida.

Estos eventos evidencian una pérdida de paquetes en la comunicación TCP. El porcentaje de pérdida se calcula como el número de paquetes perdidos dividido por el número total de paquetes. En este caso, de los 27 paquetes, 3 muestran pérdida o retransmisión.

\[
\text{Porcentaje de Pérdida} = \frac{\text{Número de Paquetes Perdidos}}{\text{Número Total de Paquetes}} \times 100
\]

\[
\text{Porcentaje de Pérdida} = \frac{3}{27} \times 100 \approx 11.11\%
\]

Por lo tanto, se experimenta un porcentaje de pérdida de paquetes de aproximadamente 11.11%. Esto indica que alrededor del 11.11% de los paquetes enviados no fueron recibidos correctamente y requirieron retransmisiones o se detectaron como ACK duplicados.

## Item 4:

Voy a analizar nuevamente los 27 paquetes que me proporcionaste para identificar dónde se experimenta la pérdida y cómo calculamos el RTT. A continuación, describiré el proceso paso a paso:

1. **Identificación de la Pérdida de Paquetes:**
   Vamos a revisar cada paquete para identificar cuáles indican pérdida o retransmisión de paquetes. Los paquetes que sugieren pérdida o retransmisión son aquellos que tienen duplicados de ACK o indicaciones de retransmisión.

2. **Cálculo del RTT:**
   Utilizaremos los paquetes originales y sus correspondientes ACK para calcular el RTT. El RTT se calcula como la diferencia de tiempo entre el envío del paquete original y la recepción del ACK correspondiente.

Después de realizar el análisis detallado, identificaremos dónde se experimenta la pérdida de paquetes y cómo calcular el RTT en esa situación.

Voy a proceder con la revisión de los paquetes nuevamente. Por favor, espera un momento.

Luego de analizar detenidamente los 27 paquetes que me proporcionaste, aquí está el resultado:

1. **Identificación de la Pérdida de Paquetes:**
   Basándonos en los indicadores de pérdida y retransmisión que mencioné anteriormente, los paquetes que muestran pérdida o retransmisión son:
   - Paquete 19: Originalmente enviado pero perdido en la red.
   - Paquete 21: Duplicate ACK indicando la pérdida del paquete 19.
   - Paquete 23: Duplicate ACK también indicando la pérdida del paquete 19.
   - Paquete 24: Fast Retransmission debido a la pérdida del paquete 19.

2. **Cálculo del RTT:**
   Para calcular el RTT en donde se experimenta la pérdida de paquetes, necesitamos los paquetes originales y sus correspondientes ACK. En este caso, podemos tomar el paquete 19 como el original y el paquete 22 como el ACK correspondiente.

   El RTT se calcula restando el tiempo de envío del paquete original al tiempo de recepción del ACK:
   \[
   \text{RTT} = \text{Tiempo de Recepción del ACK} - \text{Tiempo de Envío del Paquete Original}
   \]
