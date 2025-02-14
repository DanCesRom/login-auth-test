# login-auth-test

# Login Authentication System

Este es un simple metodo de autenticacion de usuario en un sistema con registro y incio funcion de inicio de sesion, armado en Python and bcrypt para el hashing de la .


## Estructura de Archivos

login_auth.py: Contiene la logica de autenticacion
test_login_auth.py:Contiene la uinidad de testeo para la logica de autenticacion
requirements.txt:Lista las dependencias del proyecto



## Setup

1. Clonar el repositorio.

2. Crear y activar un ambiente virtual.
   ```bash
   python -m venv venv
   .\venv\Scripts\activate

3. Instalar las dependencias
   pip install -r requirements.txt


## Uso

1. Correr la aplicacion importando authenticator desde login_auth.py
2. Registrar y autenticar los usuarios usando register_user(username, password) and authenticate_user(username, password)

#Correr Pruebas
1. Para correr la prueba, ejecuta el comando siguiente:
	pytest test_login_auth.py