# Tarea 4
#### Jeloska Isabel Chavez Paredez
### Primera Forma Normal (1FN)

| ISBN       | Título | Autor  | Nombre de Usuario | Dirección de Usuario | Fecha de Préstamo | Fecha de Devolución |
|------------|--------|--------|-------------------|----------------------|-------------------|---------------------|
| 1234567890 | Libro A| Autor 1| Usuario 1         | Dirección 1          | 2023-01-15        | 2023-01-30          |
| 1234567890 | Libro A| Autor 1| Usuario 3         | Dirección 3          | 2023-03-05        | 2023-03-20          |
| 2345678901 | Libro B| Autor 2| Usuario 2         | Dirección 2          | 2023-02-10        | 2023-02-25          |
| 3456789012 | Libro C| Autor 3| Usuario 2         | Dirección 2          | 2023-04-15        | 2023-04-30          |

### Segunda Forma Normal (2FN)
Observamos que la clave principal en esta tabla es el ISBN. Ahora, verifiquemos si los atributos no clave dependen completamente de esta clave:

Título, Autor, Nombre de Usuario y Dirección de Usuario son atributos no clave. En este caso, Nombre de Usuario y Dirección de Usuario dependen completamente del ISBN, ya que están relacionados con un libro específico. Sin embargo, Título y Autor no dependen completamente del ISBN, ya que pueden repetirse para diferentes préstamos de libros.
Para cumplir con la segunda forma normal (2NF), debemos dividir la tabla en dos:


1. **Tabla de Libros**:

| ISBN       | Título | Autor  |
|------------|--------|--------|
| 1234567890 | Libro A| Autor 1|
| 2345678901 | Libro B| Autor 2|
| 3456789012 | Libro C| Autor 3|

2. **Tabla de Préstamos**:

| ISBN       | Nombre de Usuario | Dirección de Usuario | Fecha de Préstamo | Fecha de Devolución |
|------------|-------------------|----------------------|-------------------|---------------------|
| 1234567890 | Usuario 1         | Dirección 1          | 2023-01-15        | 2023-01-30          |
| 1234567890 | Usuario 3         | Dirección 3          | 2023-03-05        | 2023-03-20          |
| 2345678901 | Usuario 2         | Dirección 2          | 2023-02-10        | 2023-02-25          |
| 3456789012 | Usuario 2         | Dirección 2          | 2023-04-15        | 2023-04-30          |

### Tercera Forma Normal (3FN)
Para lograr la **3NF**, debemos eliminar la **dependencia transitiva** entre **Nombre de Usuario** y **Dirección de Usuario** en la tabla de Préstamos. Para ello, crearemos una nueva tabla llamada **Usuarios**:


1. **Tabla de Libros**:

| ISBN       | Título | Autor  |
|------------|--------|--------|
| 1234567890 | Libro A| Autor 1|
| 2345678901 | Libro B| Autor 2|
| 3456789012 | Libro C| Autor 3|


2. **Tabla de Usuarios**:

| Nombre de Usuario | Dirección de Usuario |
|-------------------|----------------------|
| Usuario 1         | Dirección 1          |
| Usuario 2         | Dirección 2          |
| Usuario 3         | Dirección 3          |

Ahora, actualizaremos la tabla de Préstamos para que solo contenga la **clave principal** (**ISBN**) y las **llaves foráneas** (**Nombre de Usuario** y **Dirección de Usuario**):

3. **Tabla de Préstamos (actualizada)**:

| ISBN       | Nombre de Usuario | Dirección de Usuario | Fecha de Préstamo | Fecha de Devolución |
|------------|-------------------|----------------------|-------------------|---------------------|
| 1234567890 | Usuario 1         | Dirección 1          | 2023-01-15        | 2023-01-30          |
| 1234567890 | Usuario 3         | Dirección 3          | 2023-03-05        | 2023-03-20          |
| 2345678901 | Usuario 2         | Dirección 2          | 2023-02-10        | 2023-02-25          |
| 3456789012 | Usuario 2         | Dirección 2          | 2023-04-15        | 2023-04-30          |
