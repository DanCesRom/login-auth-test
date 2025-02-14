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

def test_empty_username(auth):
    """Test registration and authentication with empty username."""
    assert auth.register_user("", "password123") is False  # Empty username should fail
    assert auth.authenticate_user("", "password123") is False  # Empty username should fail

def test_empty_password(auth):
    """Test registration and authentication with empty password."""
    assert auth.register_user("user1", "") is False  # Empty password should fail
    assert auth.authenticate_user("user1", "") is False  # Empty password should fail

def test_special_characters(auth):
    """Test registration and authentication with special characters."""
    special_username = "user!@#"
    special_password = "pass$%^"
    assert auth.register_user(special_username, special_password) is True
    assert auth.authenticate_user(special_username, special_password) is True

def test_long_username_password(auth):
    """Test registration and authentication with long usernames and passwords."""
    long_username = "a" * 101  # More than 100 characters
    long_password = "b" * 101  # More than 100 characters
    assert auth.register_user(long_username, long_password) is True
    assert auth.authenticate_user(long_username, long_password) is True

def test_case_sensitivity(auth):
    """Test case sensitivity during registration and authentication."""
    assert auth.register_user("User", "password123") is True
    assert auth.authenticate_user("user", "password123") is False  # Case mismatch

def test_authenticate_before_registration(auth):
    """Test authentication before registering the user."""
    assert auth.authenticate_user("newuser", "password123") is False  # Should fail before registration

def test_multiple_logins(auth):
    """Test multiple users logging in with different credentials."""
    auth.register_user("user1", "password123")
    auth.register_user("user2", "password456")
    assert auth.authenticate_user("user1", "password123") is True
    assert auth.authenticate_user("user2", "password456") is True
    assert auth.authenticate_user("user1", "wrongpass") is False  # Should fail for user1 with wrong password

def test_password_hashing(auth):
    """Test that the password is hashed and compared correctly."""
    username = "hasheduser"
    password = "securepassword"
    assert auth.register_user(username, password) is True
    # Ensure the password is hashed and not stored as plain text
    assert auth.users[username] != password  # Should be hashed
    assert auth.authenticate_user(username, password) is True  # Should authenticate correctly