#!/bin/bash
set -e

# Esperar a la base de datos si está configurada
if [ -n "$DB_HOST" ]; then
  echo "Esperando a la base de datos..."
  while ! nc -z $DB_HOST $DB_PORT; do
    echo "Esperando a que la base de datos esté disponible en $DB_HOST:$DB_PORT..."
    sleep 2
  done
  echo "Base de datos disponible"
fi

# Ejecutar migraciones
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# Cargar fixtures si existen
# if [ -f "fixtures/extensiones.json" ]; then
#   echo "Cargando fixtures..."
#   python manage.py loaddata fixtures/extensiones.json
# fi

# if [ -f "fixtures/carreras.json" ]; then
#   echo "Cargando fixtures de carreras..."
#   python manage.py loaddata fixtures/carreras.json
# fi

if [ -f "fixtures/extensiones.json" ]; then
  if [ "$(python manage.py shell -c 'from extensiones.models import Extension; print(Extension.objects.count())')" = "0" ]; then
    echo "Cargando fixtures..."
    python manage.py loaddata fixtures/extensiones.json
  else
    echo "Fixtures de extensiones ya están cargados."
  fi
fi

if [ -f "fixtures/carreras.json" ]; then
  if [ "$(python manage.py shell -c 'from carreras.models import Carrera; print(Carrera.objects.count())')" = "0" ]; then
    echo "Cargando fixtures de carreras..."
    python manage.py loaddata fixtures/carreras.json
  else
    echo "Fixtures de carreras ya están cargados."
  fi
fi

# Colectar archivos estáticos (si es necesario)
if [ "$COLLECT_STATIC" = "true" ]; then
  echo "Recolectando archivos estáticos..."
  python manage.py collectstatic --noinput
fi

# Ejecutar el comando principal (Gunicorn o lo que se pase)
exec "$@"