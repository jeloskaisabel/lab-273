Para realizar los ejercicios planteados en la guía de laboratorio sobre la instalación y configuración del servidor DNS bajo ambiente Linux, sigue los siguientes pasos:

### Probar el procedimiento para configurar el DNS como servidor de caché

1. Abre la terminal en tu sistema Linux.

2. Instala el servidor DNS bind9 y las herramientas necesarias con los siguientes comandos:
   ```
   sudo apt update
   sudo apt install bind9 dnsutils
   ```

3. Abre el archivo de configuración del servidor DNS para configurarlo como servidor de caché:
   ```
   sudo nano /etc/bind/named.conf.options
   ```

4. Dentro del archivo, agrega el siguiente bloque que utiliza el DNS de Google como servidor de reenvío:
   ```
   forwarders {
       8.8.8.8;
   };
   ```

5. Guarda y cierra el archivo.

6. Reinicia el servicio DNS para aplicar los cambios:
   ```
   sudo systemctl restart bind9
   ```

7. Prueba el tiempo de consulta utilizando el comando `dig` para consultar un sitio web, por ejemplo:
   ```
   dig google.com
   ```

8. Ejecuta el comando anterior varias veces para observar el tiempo de consulta, que debería ser casi cero en las consultas subsiguientes debido a la caché.

### Configurar DNS primario

1. Abre el archivo de configuración principal del servidor DNS:
   ```
   sudo nano /etc/bind/named.conf.local
   ```

2. Agrega la siguiente zona para configurar el DNS como servidor primario para un dominio (sustituye "ejemplo.com" por tu propio dominio):
   ```
   zone “ejemplo.com” {
       type master;
       file “/etc/bind/db.ejemplo.com”;
   };
   ```

3. Copia el archivo de zona de la plantilla:
   ```
   sudo cp /etc/bind/db.local /etc/bind/db.ejemplo.com
   ```

4. Edita el nuevo archivo de zona para tu dominio:
   ```
   sudo nano /etc/bind/db.ejemplo.com
   ```

5. Reinicia el servicio DNS para aplicar los cambios:
   ```
   sudo systemctl restart bind9
   ```

6. Puedes probar la configuración configurando las entradas de DNS en el archivo de zona para tu dominio.

### Cambiar el DNS de su ISP por el DNS público de Google y luego por el de CloudFlare

Para cambiar el DNS de tu ISP por el DNS público de Google y luego por el de Cloudflare, debes modificar la configuración de red en tu sistema operativo. Estos pasos varían según el sistema operativo que estés utilizando.

En Linux, puedes editar el archivo de configuración de red para cambiar los servidores DNS. Por ejemplo, en Ubuntu, puedes editar el archivo `/etc/netplan/01-netcfg.yaml` y agregar las siguientes líneas para configurar el DNS de Google (8.8.8.8 y 8.8.4.4) o Cloudflare (1.1.1.1 y 1.0.0.1):

```
network:
  version: 2
  ethernets:
    eth0:  # o el nombre de tu interfaz de red
      dhcp4: yes
      dhcp4-overrides:
        use-dns: false
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

Después de guardar los cambios, aplica la configuración de red con el comando `sudo netplan apply`.

Luego, realiza pruebas de velocidad de acceso a sitios web utilizando los servidores DNS de Google y Cloudflare y elabora un cuadro comparativo de los resultados obtenidos, analizando la velocidad de acceso y la estabilidad de cada servidor DNS.

