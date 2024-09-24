# Usa la imagen oficial de Nginx
FROM nginx:latest

# Establece el directorio de trabajo en el directorio de Nginx
WORKDIR /usr/share/nginx/html

# Elimina los archivos estáticos predeterminados de Nginx
RUN rm -rf ./*

# Copia tu archivo HTML al directorio de trabajo
COPY ./formulario.html .

# Expone el puerto 5000
EXPOSE 8080

# Inicia Nginx en modo foreground
CMD ["nginx", "-g", "daemon off;"]
