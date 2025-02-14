# login-auth-test

# Sistema de Autenticación de Login

Este es un simple método de autenticación de usuario en un sistema con registro e inicio de sesión, desarrollado en Python y bcrypt para el hashing de la contraseña.


## Estructura de Archivos

login_auth.py: Contiene la lógica de autenticación.
test_login_auth.py: Contiene las pruebas unitarias para la lógica de autenticación.
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

1. Correr la aplicación importando authenticator desde login_auth.py.
2. Registrar y autenticar los usuarios usando register_user(username, password) y authenticate_user(username, password).

#Correr Pruebas
1. Para correr las pruebas, ejecuta el siguiente comando:
	pytest test_login_auth.py


## Pruebas Unitarias Agregadas

## Casos de Prueba

- **Nombre de usuario y contraseña vacíos**: Garantiza que los usuarios no puedan registrarse ni autenticarse con credenciales vacías.
- **Caracteres especiales**: Prueba si se aceptan caracteres especiales en los nombres de usuario y contraseñas.
- **Nombres de usuario/contraseñas largos**: Verifica que se manejen correctamente los nombres de usuario y contraseñas largos.
- **Sensibilidad a mayúsculas y minúsculas**: Comprueba si el sistema diferencia entre "user" y "User".
- **Autenticación antes del registro**: Garantiza que los usuarios no puedan iniciar sesión antes de registrarse.
- **Múltiples inicios de sesión**: Verifica que varios usuarios puedan iniciar sesión simultáneamente.
- **Hashing de contraseñas**: Garantiza que las contraseñas se encripten durante el registro y la autenticación.
