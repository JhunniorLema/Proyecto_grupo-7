# src/administrador.py
# Miembros del grupo: [LEMA, ROCANO, AYOVI, ALVARADO, SALAZAR]

from src.Usuario import Usuario

class Administrador(Usuario):
    """
    Clase que representa a un administrador del sistema.
    Hereda de la clase Usuario y tiene permisos de administrador.
    """
    def __init__(self, usuario_id, nombre, clave):
        super().__init__(usuario_id, nombre, clave)

    def verificar_permisos(self):
        """
        Implementación polimórfica para verificar los permisos del administrador.
        Los administradores tienen todos los permisos.
        """
        return True  # Los administradores tienen todos los permisos

    def __str__(self):
        return f"Administrador(ID={self.usuario_id}, Nombre='{self.nombre}')"

if __name__ == '__main__':
    # Pruebas individuales para la clase Administrador

    admin = Administrador(101, "Admin1", "admin_pass")
    print("--- Pruebas de la clase Administrador ---")
    print(admin)
    print(f"¿Tiene permisos de administrador? {admin.verificar_permisos()}")
    print("-" * 30)