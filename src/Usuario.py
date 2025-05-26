# src/usuario.py
# Miembros del grupo: [LEMA, ROCANO, AYOVI, ALVARADO, SALAZAR]

class Usuario:
    """
    Clase base abstracta para representar a un usuario del sistema.
    Define atributos y métodos comunes para todos los tipos de usuarios.
    """
    def __init__(self, usuario_id, nombre, clave):
        """
        Inicializa un nuevo usuario.
        """
        self._usuario_id = usuario_id
        self._nombre = nombre
        self._clave = clave

    # Properties para acceder a atributos con getters y setters
    @property
    def usuario_id(self):
        """Getter para el ID del usuario."""
        return self._usuario_id

    @property
    def nombre(self):
        """Getter para el nombre del usuario."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Setter para el nombre del usuario."""
        self._nombre = nuevo_nombre

    def verificar_clave(self, clave_ingresada):
        """
        Verifica si la clave ingresada coincide con la clave del usuario.
        """
        return self._clave == clave_ingresada

    def verificar_permisos(self):
        """
        Método polimórfico abstracto para verificar los permisos del usuario.
        Las subclases deben implementar este método.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def __str__(self):
        return f"Usuario(ID={self.usuario_id}, Nombre='{self.nombre}')"

if __name__ == '__main__':
    # Pruebas individuales para la clase Usuario

    usuario_base = Usuario(1, "UsuarioBase", "clave123")
    print("--- Pruebas de la clase Usuario ---")
    print(usuario_base)
    print(f"ID del usuario: {usuario_base.usuario_id}")
    print(f"Nombre inicial: {usuario_base.nombre}")
    usuario_base.nombre = "NuevoNombre"
    print(f"Nombre actualizado: {usuario_base.nombre}")
    print(f"Clave correcta: {usuario_base.verificar_clave('clave123')}")
    print(f"Clave incorrecta: {usuario_base.verificar_clave('otra_clave')}")
    try:
        usuario_base.verificar_permisos()
    except NotImplementedError as e:
        print(f"Error esperado: {e}")
    print("-" * 30)