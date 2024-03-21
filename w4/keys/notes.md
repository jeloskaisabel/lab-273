## Directorios
`/var/www/` creamos el proyectos
`/etc/apache2/` confiramos el servidor


## Cambiando permisos
```bash
root@debian:/var/www# chown -R www-data:www-data .
root@debian:/var/www# chmod -R 755 .
```

## Archivos importantes
`/etc/apache2/ports.conf` agregamos listen

`/etc/hosts/` modificamos alias


## Archivo config

```txt
<VirtualHost *:80>
	ServerName servidor.com
	ServerAdmin root@servidor.com
	ServerAlias www.servidor.com
	DocumentRoot /var/www/carpeta_ejemplo
	DirectoryIndex index.html
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

