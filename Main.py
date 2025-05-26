# main.py
from src.administrador import Administrador
from src.Invitado import Invitado
from src.Operador import Operador
from src.Acceso import Acceso
from src.Historial import Historial
from datetime import datetime

if __name__ == "__main__":
    # Crear instancias de usuarios
    admin = Administrador(1, "LEMA", "admin123")
    invitado = Invitado(2, "RUDY" , "agui12")
    operador = Operador(3, "DIANA", "op456")

    print("--- Prueba de Usuarios ---")
    print(admin)
    print(invitado)
    print(operador)
    print("-" * 30)

    # Prueba del método polimórfico verificar_permisos()
    print("--- Prueba de Permisos ---")
    print(f"{admin.nombre} tiene permisos: {admin.verificar_permisos()}")
    print(f"{invitado.nombre} tiene permisos: {not invitado.verificar_permisos()}")
    print(f"{operador.nombre} tiene permisos: {operador.verificar_permisos()}")
    print("-" * 30)

    # Simulaciónes de accesos
    historial_accesos = Historial()
    ahora = datetime.now()

    historial_accesos.registrar_acceso(Acceso(admin, ahora, True))
    historial_accesos.registrar_acceso(Acceso(invitado, ahora, False))
    historial_accesos.registrar_acceso(Acceso(operador, ahora, True))

    print("--- Historial de Accesos ---")
    historial_accesos.listar_accesos()
    print("-" * 30)