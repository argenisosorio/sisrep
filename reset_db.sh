#!/bin/bash

rm -rf registro/migrations/

echo "Removidas las migraciones del modulo registro"

rm -rf safet/migrations/

echo "Removidas migraciones del modulo safet"

rm -rf bitacora/migrations/

echo "Removidas migraciones del modulo bitacora"

rm -rf db.sqlite3

echo "Removida la base de datos sqlite es que esta existiera"

python manage.py makemigrations registro

echo "Migrados los modelos del modulo sisrep"

python manage.py makemigrations safet

echo "Migrados los modelos del modulo safet"

python manage.py makemigrations bitacora

echo "Migrados los modelos del modulo bitacora"

python manage.py migrate

echo "Creada la base de datos"

echo "Por favor cree un usuario administrador del sistema"

python manage.py createsuperuser

echo "Creado el usuario administrador del sistema"