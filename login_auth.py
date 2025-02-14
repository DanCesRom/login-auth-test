import bcrypt

class Authenticator:
    def __init__(self):
        """Diccionario simulado como base de datos (usuario: password encriptada)"""
        self.users = {}

    def register_user(self, username: str, password: str) -> bool:
        """Registra un nuevo usuario con una password encriptada."""
        if username in self.users:
            return False  # Usuario ya existe
        
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.users[username] = hashed_password
        return True

    def authenticate_user(self, username: str, password: str) -> bool:
        """Verifica si el usuario y la password son correctos."""
        if username not in self.users:
            return False  # Usuario no encontrado
        
        return bcrypt.checkpw(password.encode(), self.users[username])
