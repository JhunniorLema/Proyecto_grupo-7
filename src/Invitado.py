# src/Invitado.py
# Miembros del grupo: [LEMA, ROCANO, AYOVI, ALVARADO, SALAZAR]

from src.Usuario import Usuario

class Invitado(Usuario):
    """
    Clase que representa a un invitado del sistema.
    Hereda de la clase Usuario y tiene permisos limitados.
    """
    def __init__(self, usuario_id, nombre="Invitado", clave=""):
        super().__init__(usuario_id, nombre, clave)

    def verificar_permisos(self):
        """
        Implementación polimórfica para verificar los permisos del invitado.
        Los invitados tienen permisos limitados (solo lectura).
        """
        return False  # Los invitados tienen permisos limitados

    def __str__(self):
        return f"Invitado(ID={self.usuario_id}, Nombre='{self.nombre}')"

if __name__ == '__main__':
    # Pruebas individuales para la clase Invitado
    invitado = Invitado(201, "InvitadoAnonimo")
    print("--- Pruebas de la clase Invitado ---")
    print(invitado)
    print(f"¿Tiene permisos de lectura? {not invitado.verificar_permisos()}")
    print("-" * 30)