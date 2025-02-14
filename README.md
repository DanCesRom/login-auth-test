# login-auth-test

# Sistema de Autenticaci�n de Login

Este es un simple m�todo de autenticaci�n de usuario en un sistema con registro e inicio de sesi�n, desarrollado en Python y bcrypt para el hashing de la contrase�a.


## Estructura de Archivos

login_auth.py: Contiene la l�gica de autenticaci�n.
test_login_auth.py: Contiene las pruebas unitarias para la l�gica de autenticaci�n.
requirements.txt: Lista las dependencias del proyecto.



## Setup

1. Clonar el repositorio.

2. Crear y activar un ambiente virtual.
   ```bash
   python -m venv venv
   .\venv\Scripts\activate

3. Instalar las dependencias
   pip install -r requirements.txt


## Uso

1. Correr la aplicaci�n importando authenticator desde login_auth.py.
2. Registrar y autenticar los usuarios usando register_user(username, password) y authenticate_user(username, password).

#Correr Pruebas
1. Para correr las pruebas, ejecuta el siguiente comando:
	pytest test_login_auth.py


## Pruebas Unitarias Agregadas

## Casos de Prueba

- **Nombre de usuario y contrase�a vac�os**: Garantiza que los usuarios no puedan registrarse ni autenticarse con credenciales vac�as.
- **Caracteres especiales**: Prueba si se aceptan caracteres especiales en los nombres de usuario y contrase�as.
- **Nombres de usuario/contrase�as largos**: Verifica que se manejen correctamente los nombres de usuario y contrase�as largos.
- **Sensibilidad a may�sculas y min�sculas**: Comprueba si el sistema diferencia entre "user" y "User".
- **Autenticaci�n antes del registro**: Garantiza que los usuarios no puedan iniciar sesi�n antes de registrarse.
- **M�ltiples inicios de sesi�n**: Verifica que varios usuarios puedan iniciar sesi�n simult�neamente.
- **Hashing de contrase�as**: Garantiza que las contrase�as se encripten durante el registro y la autenticaci�n.
