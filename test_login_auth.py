import pytest
from login_auth import Authenticator

@pytest.fixture
def auth():
    """Crea una instancia de Authenticator para usar en las pruebas."""
    return Authenticator()

def test_register_user(auth):
    """Prueba el registro de un usuario nuevo."""
    assert auth.register_user("user1", "password123") is True
    assert auth.register_user("user1", "password123") is False  # No debe permitir duplicados

def register_user(self, username: str, password: str) -> bool:
        """Registra un usuario asegurando que el nombre y la clave sean validos."""
        
        #  Verificar si el username o password estan vacios o solo contienen espacios
        if not username.strip():
            print(" Error: El nombre de usuario no puede estar vacio")
            return False

        if not password.strip():
            print(" Error: La clave no puede estar vacaa")
            return False

        # Verificar si el usuario ya existe
        if username in self.users:
            print(" Error: El usuario ya existe")
            return False
        
        # Hash de la contraseña
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.users[username] = hashed_password
        print(" Usuario registrado correctamente")
        return True



def test_authenticate_user(auth):
    """Prueba la autenticacion de un usuario registrado."""
    auth.register_user("user2", "securepass")
    assert auth.authenticate_user("user2", "securepass") is True
    assert auth.authenticate_user("user2", "wrongpass") is False
    assert auth.authenticate_user("unknown", "securepass") is False