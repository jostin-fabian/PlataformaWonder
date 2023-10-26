# Plataforma Wonder - Apoyo Psicológico para Estudiantes

¡Bienvenido a Plataforma Wonder! Este proyecto tiene como objetivo proporcionar apoyo psicológico a estudiantes de instituto a través de una plataforma en línea. Este README.md proporciona una visión general del proyecto y sus características clave.

## Descripción del Proyecto

Plataforma Wonder es una plataforma en línea diseñada para estudiantes que necesitan apoyo psicológico. Permite a los estudiantes conectarse con psicólogos y programar citas para recibir atención profesional.

## Características Clave

- **Registro de Alumnos:** Los estudiantes pueden registrarse en la plataforma para acceder a los servicios de apoyo psicológico.

- **Registro de Psicólogos:** Los psicólogos pueden registrarse en la plataforma y ofrecer apoyo a los estudiantes.

- **Chat Psicológico:** Los estudiantes pueden comunicarse con los psicólogos a través de un chat en línea para recibir apoyo.

- **Calendario de Citas:** Los estudiantes pueden programar citas con psicólogos utilizando un calendario integrado.

- **Gestión de Citas:** Los estudiantes tienen la capacidad de modificar o cancelar sus citas según sea necesario.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- Python 3.9 o superior
- Django 3.2 o superior
- PostgreSQL 13 o superior
- Redis 6 o superior
## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/jostin-fabian/PlataformaWonder.git
```

2. Crea un entorno virtual e instala las dependencias:

```bash
cd PlataformaWonder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Crea una base de datos PostgreSQL y configura las variables de entorno:

```bash
createdb wonder
export DATABASE_URL=postgres://user:password@host:port/wonder
export SECRET_KEY=your_secret_key
export DEBUG=True # or False for production
# add any other environment variables you need
```

4. Ejecuta las migraciones y crea un usuario administrador:

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

6. Inicia el servidor de Redis y el worker de Celery:

```bash
redis-server # in another terminal
```

7. Abre tu navegador y visita http://localhost:8000 para ver la plataforma.

## Uso

Para crear y editar cursos, accede al panel de administración en http://localhost:8000/admin con el usuario que creaste anteriormente.

Para personalizar la apariencia y el contenido de la plataforma, modifica los archivos en la carpeta `templates` y `static`.

Para integrar la plataforma con servicios externos, consulta la documentación oficial de cada servicio y añade las credenciales correspondientes a las variables de entorno.

## Contribuir

Si quieres contribuir a este proyecto, puedes hacerlo de las siguientes formas:

- Reportar errores o sugerir mejoras abriendo un issue en GitHub.
- Enviar un pull request con tus cambios siguiendo las buenas prácticas de código.
- Compartir el proyecto con otras personas que puedan estar interesadas.

## Licencia

Este proyecto está bajo la licencia MIT.
