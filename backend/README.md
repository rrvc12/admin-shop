# Backend Admin Shop - Instrucciones

Este proyecto es un backend de Django preparado para ejecutarse fácilmente con Docker

## Requisitos previos

- [Docker](https://www.docker.com/get-started) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) instalado

## Pasos para levantar el backend

1. **Clona el repositorio** (si aún no lo has hecho):

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd admin-shop/backend
    ```

2. **Prepara las variables de entorno**

    Crea un archivo `.env` en la raíz del proyecto (donde está el archivo `docker-compose.yml`) con las variables necesarias. Un ejemplo se encuentra en el archivo `.env.example`.

3. **Construye y levanta los contenedores**:

    Desde la raíz del proyecto (donde está el archivo `docker-compose.yml`):

    ```bash
    docker-compose up --build
    ```

    Esto descargará las imágenes necesarias, instalará las dependencias y levantará el backend de Django.

    Las siguientes veces solo es necesario levantar

    ```bash
    docker-compose up
    ```

3. **Accede al backend**:

   Por defecto, el backend estará disponible en:

   - http://localhost:8000/

4. **Migraciones y superusuario** (opcional):

   Si necesitas aplicar migraciones manualmente o crear un superusuario, puedes acceder al contenedor de la app:

   ```bash
   docker-compose exec app bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

