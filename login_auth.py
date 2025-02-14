import bcrypt

class Authenticator:
    def __init__(self):
        """Diccionario simulado como base de datos (usuario: password encriptada)"""
        self.users = {}

    def register_user(self, username: str, password: str) -> bool:
        """Registra un nuevo usuario con una clave encriptada."""
        
        # Verificar si el username o clave estan vacios
        if not username.strip():
            print("Error: El nombre de usuario no puede estar vacio")
            return False

        if not password.strip():
            print("Error: La clave no puede estar vacia")
            return False

        if username in self.users:
            print("Error: El usuario ya existe")
            return False  # Usuario ya existe
        
        # Hash de la clave
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.users[username] = hashed_password
        print("Usuario registrado correctamente")
        return True

    def authenticate_user(self, username: str, password: str) -> bool:
        """Verifica si el usuario y la password son correctos."""
        if username not in self.users:
            return False  # Usuario no encontrado
        
        return bcrypt.checkpw(password.encode(), self.users[username])
