# src/Operador.py
# Miembros del grupo: [LEMA, ROCANO, AYOVI, ALVARADO, SALAZAR]

from src.Usuario import Usuario

class Operador(Usuario):
    """
    Clase que representa a un operador del sistema.
    Hereda de la clase Usuario y tiene permisos específicos.
    """
    def __init__(self, usuario_id, nombre, clave):
        super().__init__(usuario_id, nombre, clave)

    def verificar_permisos(self):
        """
        Implementación polimórfica para verificar los permisos del operador.
        Los operadores tienen permisos para ciertas operaciones.
        """
        return True  # Los operadores tienen permisos específicos

    def __str__(self):
        return f"Operador(ID={self.usuario_id}, Nombre='{self.nombre}')"

if __name__ == '__main__':
    # Prueba individuales para la clase Operador

    operador = Operador(301, "Op1", "op_pass")
    print("--- Pruebas de la clase Operador ---")
    print(operador)
    print(f"¿Tiene permisos de operación? {operador.verificar_permisos()}")
    print("-" * 30)