# src/Historial.py
from src.Acceso import Acceso

class Historial:
    """
    Clase para gestionar el historial de accesos al sistema.
    Permite registrar y listar los accesos.
    """
    def __init__(self):
        """
        Inicializa un nuevo historial de accesos.
        """
        self._registros = []

    def registrar_acceso(self, acceso: Acceso):
        """
        Registra un nuevo evento de acceso en el historial.
        """
        self._registros.append(acceso)

    def listar_accesos(self):
        """
        Lista todos los registros de acceso en el historial.
        """
        for registro in self._registros:
            print(registro)

if __name__ == '__main__':
    # Prueba individuales para la clase Historial

    from src.administrador import Administrador
    from src.Invitado import Invitado
    from datetime import datetime

    historial = Historial()
    admin_prueba = Administrador(103, "AdminTest", "test")
    invitado_prueba = Invitado(202, "GuestTest")
    ahora = datetime.now()

    historial.registrar_acceso(Acceso(admin_prueba, ahora, True))
    historial.registrar_acceso(Acceso(invitado_prueba, ahora, False))

    print("--- Prueba de la clase Historial ---")
    historial.listar_accesos()
    print("-" * 30)