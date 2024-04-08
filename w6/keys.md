Claro, aquí tienes una guía paso a paso para realizar las actividades descritas en la imagen:

**Actividad 1: Configuración de NGINX para un sitio virtual**

1. **Instalación de NGINX**:
   - Abre una terminal en tu servidor.
   - Actualiza el índice de paquetes de tu gestor de paquetes, por ejemplo: `sudo apt update` en Ubuntu/Debian.
   - Instala NGINX utilizando el gestor de paquetes, por ejemplo: `sudo apt install nginx`.

2. **Configuración del Sitio Virtual**:
   - Navega al directorio de sitios disponibles de NGINX, usualmente ubicado en `/etc/nginx/sites-available/`.
   - Crea un nuevo archivo de configuración para tu sitio, por ejemplo `sitioWeb1`.
   - Edita el archivo con un editor de texto y configura el servidor virtual. A continuación, un ejemplo básico de configuración:
     ```
     server {
         listen 80;
         server_name sitioWeb1;
     
         root /var/www/sitioWeb1;
         index index.html;
     
         location / {
             try_files $uri $uri/ =404;
         }
     }
     ```
   - Guarda y cierra el archivo.

3. **Creación del Directorio del Sitio Web y Archivo Index**:
   - Crea el directorio para tu sitio web: `sudo mkdir -p /var/www/sitioWeb1`.
   - Asigna permisos apropiados: `sudo chown -R www-data:www-data /var/www/sitioWeb1`.
   - Navega a `/var/www/sitioWeb1` y crea un archivo `index.html`.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Empresa de Software - Página Principal</title>
</head>
<body>
    <h1>Bienvenido a nuestra empresa de software</h1>
    <p>Somos una empresa dedicada al desarrollo de software de alta calidad.</p>
    <img src="imagen.jpg" alt="Logo de la empresa">
    <a href="pagina2.html">Ir a la segunda página</a>
</body>
</html>


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Segunda Página</title>
</head>
<body>
    <h1>Esta es nuestra segunda página</h1>
    <p>Aquí encontrarás más información sobre nuestros servicios.</p>
</body>
</html>
```
   - Añade contenido HTML básico y enlaza a tu imagen preferida.

4. **Habilitar el Sitio y Reiniciar NGINX**:
   - Crea un enlace simbólico del archivo de configuración en `sites-available` a `sites-enabled`: 
     `sudo ln -s /etc/nginx/sites-available/sitioWeb1 /etc/nginx/sites-enabled/`.
   - Verifica la configuración de NGINX: `sudo nginx -t`.
   - Reinicia NGINX: `sudo systemctl restart nginx`.

5. **Configurar el Host Local (Opcional)**:
   - Para acceder localmente, añade una entrada a tu archivo `/etc/hosts`: `127.0.0.1 sitioWeb1`.

**Actividad 2: Desarrollo de una Página con Formulario LAMP**

1. **Instalación de LAMP** (Linux, Apache, MySQL, PHP):
   - Instala Apache: `sudo apt install apache2`.
   - Instala MySQL: `sudo apt install mysql-server`.
   - Instala PHP: `sudo apt install php libapache2-mod-php php-mysql`.

2. **Creación de la Página del Formulario**:
   - Navega al directorio de tu servidor web, usualmente es `/var/www/html`.
   - Crea un nuevo archivo `form.php`.
   - Escribe el código PHP para manejar el método POST y un formulario HTML para el registro de alumnos.
     Aquí un ejemplo básico:
```php

// Comprobar si el formulario ha sido enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $email = $_POST['email'];

    // Mostrar los datos del usuario
    echo "Nombre: " . htmlspecialchars($nombre) . "<br>";
    echo "Correo electrónico: " . htmlspecialchars($email) . "<br>";
} else {
    // Mostrar el formulario si no se ha enviado
    ?>
    <form action="form.php" method="post">
        Nombre: <input type="text" name="nombre"><br>
        Correo electrónico: <input type="text" name="email"><br>
        <input type="submit" value="Enviar">
    </form>
    <?php
}
?>

```

3. **Probar el Formulario**:
   - Abre un navegador web y ve a `http://localhost/form.php`.
   - Completa el formulario y envíalo para ver los datos devueltos por el servidor.

Recuerda reemplazar los nombres de directorios y configuraciones con los que correspondan a tu sistema y necesidades.

## Desacativar el apache2
systemctl stop apache2
systemctl disable apache2
