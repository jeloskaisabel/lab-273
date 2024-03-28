Para realizar las actividades mencionadas en Debian, puedes seguir estos pasos:

1. **Encuentra la IP del servidor que aloja a www.google.com.bo**:
   Puedes usar el comando `dig` para realizar consultas DNS y obtener la dirección IP de un dominio. Por ejemplo:
   ```bash
   dig www.google.com.bo +short
   ```

2. **Realiza una consulta inversa para obtener el nombre asociado a la IP 208.67.222.222**:
   Utiliza el comando `dig -x` seguido de la dirección IP para realizar una consulta inversa y obtener el nombre asociado:
   ```bash
   dig -x 208.67.222.222 +short
   ```

3. **Encuentra los nombres de los servidores DNS autorizados y sus direcciones IP para el dominio umsa.bo**:
   Puedes usar el siguiente comando para obtener la información de los servidores DNS autorizados para el dominio umsa.bo:
   ```bash
   dig ns umsa.bo +short
   ```

4. **Configura un servidor DNS primario para el dominio apellido.net**:
   Para configurar un servidor DNS primario en Debian, debes instalar el paquete `bind9`, que es el servidor DNS estándar en sistemas Debian. Puedes instalarlo utilizando el siguiente comando:
   ```bash
   sudo apt-get update
   sudo apt-get install bind9
   ```

   Luego, debes configurar los archivos de zona en `/etc/bind` para el dominio `apellido.net`. Puedes crear un archivo de zona directa (`db.apellido.net`) y un archivo de zona inversa (`db.192`) para las resoluciones directas e inversas respectivamente.

   Aquí tienes un ejemplo básico de cómo podrían ser estos archivos de zona:

   **Archivo de zona directa (`db.apellido.net`)**:
   ```
   $TTL 3600
   @       IN      SOA     ns1.apellido.net. admin.apellido.net. (
                           2022032801 ; Serial
                           3600       ; Refresh
                           1800       ; Retry
                           604800     ; Expire
                           86400 )    ; Minimum TTL

   @       IN      NS      ns1.apellido.net.
   @       IN      A       192.168.1.100
   ns1     IN      A       192.168.1.100
   host1   IN      A       192.168.1.101
   host2   IN      A       192.168.1.102
   ```

   **Archivo de zona inversa (`db.192`)**:
   ```
   $TTL 3600
   @       IN      SOA     ns1.apellido.net. admin.apellido.net. (
                           2022032801 ; Serial
                           3600       ; Refresh
                           1800       ; Retry
                           604800     ; Expire
                           86400 )    ; Minimum TTL

   @       IN      NS      ns1.apellido.net.
   100     IN      PTR     ns1.apellido.net.
   101     IN      PTR     host1.apellido.net.
   102     IN      PTR     host2.apellido.net.
   ```

   Después de crear estos archivos de zona, debes modificar el archivo de configuración principal de BIND (`named.conf`) para incluir las referencias a estos archivos de zona.

   Reinicia el servicio BIND para aplicar los cambios:
   ```bash
   sudo systemctl restart bind9
   ```

   Finalmente, asegúrate de configurar correctamente la resolución DNS en los clientes para que apunten al servidor DNS que has configurado. Esto se hace modificando el archivo `/etc/resolv.conf` en los clientes.

Estos pasos te guiarán a través de las actividades que deseas realizar en Debian relacionadas con DNS. Asegúrate de ajustar los detalles según tu entorno específico.