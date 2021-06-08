#!/bin/bash

rm -rf registro/migrations/

echo "Removidas migraciones del registro"

rm -rf safet/migrations/

echo "Removidas migraciones del safet"

rm -rf bitacora/migrations/

echo "Removidas migraciones del la bitacora"

rm -rf db.sqlite3

echo "Removida la base de datos sqlite si existe"

python manage.py makemigrations registro

echo "Migrados los modelos del sisrep"

python manage.py makemigrations safet

echo "Migrados los modelos del safet"

python manage.py makemigrations bitacora

echo "Migrados los modelos de la bitacora"

python manage.py migrate

echo "Creada la base de datos"

python manage.py createsuperuser

echo "Creado el super usuario del sistema"