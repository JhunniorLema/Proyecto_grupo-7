# src/Acceso.py
from datetime import datetime
from src.Usuario import Usuario

class Acceso:
    """
    Clase para representar un intento de acceso al sistema.
    Registra el usuario, la hora y si el acceso fue exitoso.
    """
    def __init__(self, usuario: Usuario, hora: datetime, exitoso: bool):
        """
        Inicializa un nuevo registro de acceso.
        """
        self._usuario = usuario
        self._hora = hora
        self._exitoso = exitoso

    @property
    def usuario(self):
        """Getter para el usuario."""
        return self._usuario

    @property
    def hora(self):
        """Getter para la hora del acceso."""
        return self._hora

    @property
    def exitoso(self):
        """Getter para indicar si el acceso fue exitoso."""
        return self._exitoso

    def __str__(self):
        estado = "Exitoso" if self._exitoso else "Fallido"
        return f"Acceso(Usuario={self.usuario.nombre}, Hora={self.hora.strftime('%Y-%m-%d %H:%M:%S')}, Estado={estado})"

if __name__ == '__main__':
    # Pruebas individuales para la clase Acceso

    from src.administrador import Administrador
    admin_prueba = Administrador(102, "TestAdmin", "test")
    ahora = datetime.now()
    acceso_exitoso = Acceso(admin_prueba, ahora, True)
    acceso_fallido = Acceso(admin_prueba, ahora, False)
    print("--- Pruebas de la clase Acceso ---")
    print(acceso_exitoso)
    print(acceso_fallido)
    print("-" * 30)