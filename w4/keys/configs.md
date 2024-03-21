Para cambiar la ubicación por defecto usada por Apache para almacenar contenidos de los sitios web y establecer la nueva ubicación en `/u/apache`, siga los siguientes pasos:

1. **Modificar la configuración de Apache:**
   Abra el archivo de configuración de Apache (`httpd.conf` o `apache2.conf`, dependiendo de la distribución de Linux que esté utilizando) en un editor de texto como root o utilizando `sudo`.

   ```bash
   sudo nano /etc/apache2/apache2.conf
   ```

2. **Buscar la directiva `DocumentRoot`:**
   Utilice el comando de búsqueda del editor (`Ctrl + W` en nano) para encontrar la directiva `DocumentRoot`. Esta línea indica la ubicación actual donde se almacenan los archivos del sitio web.

   ```apache
   DocumentRoot /var/www/html
   ```

3. **Cambiar la ubicación del `DocumentRoot`:**
   Reemplace la ubicación actual (`/var/www/html`) con la nueva ubicación deseada (`/u/apache`). La línea modificada debería verse así:

   ```apache
   DocumentRoot /u/apache
   ```

4. **Guardar y salir del editor:** 
   En nano, use `Ctrl + O` para guardar y `Ctrl + X` para salir.

5. **Reiniciar Apache:**
   Después de hacer cambios en la configuración de Apache, es necesario reiniciar el servicio para que los cambios surtan efecto.

   ```bash
   sudo systemctl restart apache2
   ```

6. **Crear una página de prueba:**
   Cree un archivo HTML en la nueva ubicación para verificar que los cambios se hayan realizado correctamente.

   ```bash
   sudo nano /u/apache/index.html
   ```

   Inserte el siguiente contenido en el archivo `index.html`:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Nueva Ubicación Apache</title>
   </head>
   <body>
       <h1>¡La nueva ubicación de Apache funciona!</h1>
       <p>Esta es una página de prueba creada en la nueva ubicación.</p>
   </body>
   </html>
   ```

7. **Guardar y salir del editor:** 
   En nano, use `Ctrl + O` para guardar y `Ctrl + X` para salir.

8. **Verificar la nueva ubicación:**
   Abra un navegador web y visite la dirección IP de su servidor o el nombre de dominio (si está configurado) seguido de `/index.html` (por ejemplo, `http://su_direccion_ip/index.html`). Debería ver la página de prueba que creó en la nueva ubicación.

Al seguir estos pasos, habrá cambiado la ubicación por defecto utilizada por Apache para almacenar los contenidos de los sitios web y habrá creado una página de prueba en la nueva ubicación para verificar que todo esté funcionando correctamente.