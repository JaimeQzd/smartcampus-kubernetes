# Imagen ligera de Nginx para servir el frontend.
FROM nginx:alpine


# Copiamos los archivos de la interfaz web.
COPY index.html /usr/share/nginx/html/index.html
COPY styles.css /usr/share/nginx/html/styles.css
COPY app.js /usr/share/nginx/html/app.js


# Nginx sustituira las variables de entorno
# presentes en esta plantilla al arrancar.
COPY nginx.conf.template /etc/nginx/templates/default.conf.template


# El frontend escucha dentro del contenedor
# en el puerto HTTP 80.
EXPOSE 80