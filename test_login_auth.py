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

def test_authenticate_user(auth):
    """Prueba la autenticacion de un usuario registrado."""
    auth.register_user("user2", "securepass")
    assert auth.authenticate_user("user2", "securepass") is True
    assert auth.authenticate_user("user2", "wrongpass") is False
    assert auth.authenticate_user("unknown", "securepass") is False