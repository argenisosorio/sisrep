<h1>Sistema para reportar mensualmente los avances de un proyecto</h1>

<b>Creado por Argenis Osorio en la Fundación CENDITEL</b>

<hr />

## Paquetes del Sistema Operativo requeridos
```
postgresql
libpq-dev
python-psycopg2
```

## Paquetes de Python requeridos
```
Django==1.8.8
Python==2.7
postgres
psycopg2
```

<br />

<b>Nota:</b>
<br />
Usaremos $ para describir los comandos que se usaran con usuario regular.

Usaremos # para describir los comandos que se usaran con superusuario. 

<br />

## Instalación de paquetes para crear entornos virtuales
```
# apt-get install install python-setuptools python-dev

# apt-get install python-virtualenv virtualenvwrapper
```

<br />

## Crear un entorno virtual de python
```
$ virtualenv mi_env

$ source mi_env/bin/activate
```

<br />

## Instalación de requerimientos
```
# apt-get install postgresql libpq-dev python-psycopg2

$ cd reporte_mensual_proyecto

$ pip install -r requirements.txt 
```

<br />

## Desplegar el proyecto localmente
```
$ cd reporte_mensual_proyecto

$ cp settings.py_example settings.py

$ cd ..
```

## Creación del usuario y la base de datos del sistema desde la consola de postgresql
```
postgres=# CREATE USER admin PASSWORD '123456';

postgres=# CREATE DATABASE reporte OWNER admin;
```

```
$ bash reset_db.sh

$ python manage.py runserver
```

<br />

## Capturas
![captura-1.jpg](captura-1.jpg "captura-1.jpg")