## Documentación del Proyecto: Operaciones con Conjuntos y Visualización con Diagramas de Venn

### Descripción General

Este proyecto es una aplicación de consola en Python diseñada para realizar operaciones básicas con conjuntos (unión, intersección, diferencia, y diferencia simétrica) y visualizar las relaciones entre tres conjuntos mediante diagramas de Venn. La aplicación permite a los usuarios ingresar elementos para cada conjunto, seleccionar conjuntos para realizar operaciones, y visualizar los resultados de estas operaciones así como los conjuntos mismos.

### Dependencias

- **matplotlib**: Utilizada para generar los diagramas de Venn.
- **matplotlib_venn**: Proporciona funciones específicas para crear y manipular diagramas de Venn.

### Uso

Para ejecutar el proyecto, se necesita tener Python y las dependencias mencionadas instaladas. El script se inicia desde la línea de comandos y sigue una serie de pasos interactivos donde el usuario introduce datos y selecciona operaciones para ejecutar.

### Funciones

#### `getValues()`

- **Propósito**: Captura los elementos de un conjunto de números enteros ingresados por el usuario.
- **Comportamiento**: Solicita al usuario la cantidad de elementos y luego cada elemento por separado, añadiéndolos a un conjunto para evitar duplicados.
- **Retorno**: Un conjunto (`set`) de números enteros.

#### `printUnion(value1, value2)`

- **Propósito**: Calcula y muestra la unión de dos conjuntos.
- **Comportamiento**: Utiliza el operador `|` para realizar la unión y luego imprime el resultado.
- **Entradas**: Dos conjuntos (`value1`, `value2`).

#### `printInterceccion(value1, value2)`

- **Propósito**: Calcula y muestra la intersección de dos conjuntos.
- **Comportamiento**: Emplea el operador `&` para determinar los elementos comunes y los imprime.
- **Entradas**: Dos conjuntos (`value1`, `value2`).

#### `printDiferencia(value1, value2)`

- **Propósito**: Calcula y muestra la diferencia de dos conjuntos.
- **Comportamiento**: Aplica el operador `-` para encontrar los elementos de `value1` que no están en `value2` y los imprime.
- **Entradas**: Dos conjuntos (`value1`, `value2`).

#### `printDiferenciaSimetrica(value1, value2)`

- **Propósito**: Calcula y muestra la diferencia simétrica entre dos conjuntos.
- **Comportamiento**: Usa el operador `^` para obtener elementos únicos en ambos conjuntos y los imprime.
- **Entradas**: Dos conjuntos (`value1`, `value2`).

#### `getOperation(a, b, c)`

- **Propósito**: Permite al usuario seleccionar uno de los tres conjuntos disponibles.
- **Comportamiento**: Presenta un menú de opciones al usuario, captura la elección y devuelve el conjunto correspondiente. Si la selección es inválida, se elige el conjunto `a` por defecto.
- **Entradas**: Tres conjuntos (`a`, `b`, `c`).
- **Retorno**: El conjunto elegido.

### Flujo de Ejecución

1. **Inicio**: Solicita al usuario ingresar elementos para los conjuntos A, B, y C.
2. **Visualización**: Muestra los conjuntos A, B, y C y sus relaciones a través de un diagrama de Venn.
3. **Operaciones con Conjuntos**: Permite al usuario realizar y visualizar operaciones entre los conjuntos seleccionados.

### Visualización de Diagramas de Venn

Utiliza `venn3` para mostrar un diagrama de Venn de tres conjuntos y `venn3_circles` para personalizar los círculos que representan cada conjunto. Los conjuntos se visualizan después de ser definidos por el usuario, proporcionando una representación gráfica inmediata de sus relaciones.

### Ejecución de Operaciones

El script invita al usuario a realizar operaciones específicas entre los conjuntos. Para cada operación, el usuario debe seleccionar dos conjuntos sobre los cuales operar. Las operaciones disponibles son unión, intersección, diferencia, y diferencia simétrica.

### Consideraciones de Mejora

- Implementar validaciones de entrada para asegurar que los usuarios solo puedan ingresar números enteros.
- Mejorar la interacción del usuario con una interfaz gráfica que facilite la selección de operaciones y conjuntos.
- Añadir la capacidad de realizar operaciones con

 más conjuntos y visualizar conjuntos de mayor complejidad en los diagramas de Venn.

Esta documentación ofrece una visión detallada del proyecto, incluyendo su propósito, uso, y estructura de código, lo cual es esencial para su mantenimiento y futuras mejoras.