# Introducción a Flask 

Este es un tutorial acerca de Flask y la contenerización de una aplicación basada en Flask en una imagen de contenedor de Docker. 
Así mismo, se hace una explicación de la manera como se puede usar una base de datos como PostgreSQL como el _backend_ de nuestra aplicación.

Para continuar, por favor ir al _branch_ cuyo nombre es `paso-01`.

## `paso-01`

Inicialmente se creará el espacio donde las librerías y dependencias de nuestra aplicación se instalarán.

```
python3 -m venv venv
```

Una vez se tiene el espacio, se pasa a la activación de este espacio para poder llevar a cabo allí la instalación de paquetes y librerías que usará nuestra aplicación.

```
source venv/bin/activate
```

Se crea ahora un archivo llamado `requirements.txt` que contiene las siguientes líneas:

```
flask
flask-sqlalchemy
```

A continuación veremos el código tipo `hola mundo` en Flask.
Se creará un archivo llamado `app.py` que contiene las siguientes líneas:

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello, world"

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
```

Una vez se han instalado las librerías y se ha creado el archivo `app.py` se procede a ejecutar el programa en este archivo.

```
python3 app.py
```

Una vez se ejecuta el navegador, un mensaje como el siguiente debería aparecer en pantalla:

```
 * Serving Flask app 'app'                                                                                                                                                   
 * Debug mode: on                                                                                                                                                            
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.                                                       
 * Running on all addresses (0.0.0.0)                                                                                                                                        
 * Running on http://127.0.0.1:5000                                                                                                                                          
Press CTRL+C to quit                                                                                                                                                         
 * Restarting with stat                                                                                                                                                      
 * Debugger is active!
 * Debugger PIN: 169-269-208
```

Abrir ahora un navegador en la dirección `http://localhost:5000`.
