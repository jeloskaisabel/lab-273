Si decides no utilizar conexiones seguras (SSL/TLS) para tu servidor de correo electrónico con Dovecot y Postfix, es importante ser consciente de los riesgos de seguridad implicados. Sin cifrado, las contraseñas y los mensajes de correo electrónico se transmiten en texto plano sobre la red, lo que podría permitir a los atacantes interceptar y leer estos datos. Se recomienda utilizar conexiones seguras siempre que sea posible, especialmente si estás manejando información sensible.

Sin embargo, si tienes una razón válida para proceder sin SSL/TLS (por ejemplo, una red cerrada y segura donde el riesgo de interceptación es bajo), aquí te explicamos cómo configurar Dovecot y Postfix para no usar conexiones seguras.

### Configuración de Dovecot sin SSL/TLS

Para configurar Dovecot para no usar conexiones seguras, realiza los siguientes pasos:

1. **Editar la configuración de SSL en Dovecot**: Encuentra el archivo de configuración `10-ssl.conf` dentro del directorio `/etc/dovecot/conf.d/` y asegúrate de que la línea de configuración de SSL esté establecida en `no`:

   ```conf
   ssl = no
   ```

2. **Comentar o eliminar cualquier referencia a certificados SSL** en el mismo archivo, ya que no serán necesarios:

   ```conf
   #ssl_cert = </etc/dovecot/private/dovecot.pem
   #ssl_key = </etc/dovecot/private/private/dovecot.key
   ```

3. **Reinicia Dovecot** para aplicar los cambios:

   ```bash
   sudo systemctl restart dovecot
   ```

### Configuración de Postfix sin SSL/TLS

Para Postfix, asegúrate de que no estés forzando el uso de conexiones cifradas:

1. **Editar la configuración principal de Postfix**: Edita el archivo `/etc/postfix/main.cf` y asegúrate de que las configuraciones relacionadas con TLS estén deshabilitadas o comentadas. No deberías necesitar cambiar muchas configuraciones aquí para deshabilitar SSL/TLS, pero es bueno revisar que no estés forzando su uso para la autenticación o conexiones, por ejemplo:

   ```conf
   #smtpd_tls_security_level = may
   #smtp_tls_security_level = may
   ```

   Si estas líneas están presentes y descomentadas, cámbialas a `none` o simplemente coméntalas (poniendo un `#` al inicio de la línea).

2. **Reinicia Postfix** para aplicar los cambios:

   ```bash
   sudo systemctl restart postfix
   ```

### Consideraciones Adicionales

- **Autenticación**: Si has configurado `disable_plaintext_auth = no` en Dovecot, significa que permites autenticaciones en texto plano. Esto es coherente con no usar SSL/TLS, pero aumenta el riesgo de que las credenciales de los usuarios sean capturadas por terceros.
- **Seguridad de la Red**: Implementa otras medidas de seguridad de red para proteger tus datos, especialmente si decides operar sin cifrado.
- **Informar a los Usuarios**: Asegúrate de que los usuarios sean conscientes de los riesgos de seguridad asociados con la transmisión de información sin cifrar.

Recuerda, operar sin conexiones seguras expone la información de correo electrónico y las credenciales de los usuarios a riesgos significativos. Evalúa cuidadosamente los riesgos y considera usar SSL/TLS para proteger las comunicaciones de correo electrónico.

