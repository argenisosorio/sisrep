<h1>Sistema para reportar mensualmente los avances de un proyecto</h1>

<b>Creado por Argenis Osorio en la Fundación CENDITEL</b>

<hr />

## Paquetes de Python requeridos
```
Django==1.8.8
Python==2.7
```

Usaremos $ para describir los comandos que se usaran con usuario regular.

Usaremos # para describir los comandos que se usaran con superusuario. 

## Instalación de paquetes para crear entornos virtuales
```
# apt-get install install python-setuptools python-dev

# apt-get install python-virtualenv virtualenvwrapper
```

## Crear un entorno virtual de python
```
$ virtualenv mi_env

$ source mi_env/bin/activate
```

## Instalación de requerimientos
```
$ cd reporte_mensual_proyecto

$ pip install -r requirements.txt 
```

## Desplegar el proyecto localmente
```
$ cd reporte_mensual_proyecto

$ cp settings.py_example settings.py

$ cd ..

$ bash reset_db.sh

$ python manage.py runserver
```

## Capturas
![captura-1.jpg](captura-1.jpg "captura-1.jpg")