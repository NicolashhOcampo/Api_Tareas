# Api Tareas

## Inicializar Proyecto
```bash
#Crear entorno virtual
python -m venv .venv

#Activar entorno virtual
source .venv/Scripts/activate

#Levantar servidor
fastapi dev app/main.py

```

## Migraciones
```bash
#Crear migracion
alembic revision --autogenerate -m <nombre_migracion>

#Aplicar migraciones
alembic upgrade head

```