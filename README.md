**Universidad de Guayaquil - Facultad Ciencias Administrativas**

**Integrantes: Lema Jhunnior, Rudy Rocano, Diana Ayovi, Cindy Alvarado, Samuel Salasar** 

¨**Docente- Guillermo Valarezo** 

**Proyecto_Final Grupo#7**

En este proyecto crearemos un Sistema de Control de Acceso y Seguridad Informática . 
Utilizando todos los principios de Programación Orientada a Objetos (POO) como herencia, polimorfismo 
y encapsulamiento.

Antes de ejecutar este proyecto, asegúremos de tener lo siguiente:

1.	Python instalado.
2.	PyCharm instalado (Community).
3.	El proyecto debe estar organizado con la estructura correcta de carpetas.

**DESCRIPCION GENERAL**

**Usuario (Clase base)**

la clase usuario es como un molde para crear diferentes tipos de usuarios, asegurando que todos tengan una identificación, un nombre y
una forma de verificar su contraseña, y obligando a que cada tipo de usuario defina sus propios permisos.

•	Define los atributos y métodos comunes para todos los usuarios.

• Tambien ncluye métodos para verificar_clave y un método abstracto verificar_permisos(), 
que debe ser implementado por las clases hijas para definir los permisos específicos de cada tipo de usuario.

•	Métodos clave:

o __str__(self): Define cómo se representa un objeto Usuario como una cadena de texto, mostrando su ID y nombre.

o __init__(self, usuario_id, nombre, clave): El constructor de la clase Usuario. Inicializa los atributos usuario_id, nombre y clave.

o	verificar_clave(): Verifica si la clave ingresada es correcta.

o	verificar_permisos(): Método abstracto que debe ser implementado por las subclases.

Evidencia de ejecución


 ![Captura de pantalla 2025-05-26 094027](https://github.com/user-attachments/assets/d46fdfbe-2ca2-42a5-b3ef-4a6364e6a372)



**Administrador**

la clase Administrador define un tipo de usuario con acceso completo al sistema, construyéndose 
sobre la estructura básica proporcionada por la clase Usuario.

•	Hereda de Usuario.

•	Tiene todos los permisos del sistema.

•	Método sobrescrito: verificar_permisos() devuelve True.

evidencia de ejecución


 ![Captura de pantalla 2025-05-26 094116](https://github.com/user-attachments/assets/1f13ac7e-376b-4f45-abb5-987c8e1f3b65)



**Invitado**

la clase Invitado define un tipo de usuario con permisos restringidos, utilizando la estructura base proporcionada por la clase Usuario.

•	Hereda de Usuario.

•	Solo tiene permisos de lectura.

   Metodos:
   
•	Método sobrescrito: verificar_permisos() devuelve False.

• __init__(self, usuario_id, nombre=Invitado, clave=): El constructor de la clase Invitado. 
Llama al constructor de la clase padre (Usuario) y establece un nombre predeterminado de Invitado si no se proporciona uno.

•verificar_permisos(self): Implementación del método abstracto verificar_permisos de la clase Usuario. Para la clase Invitado
este método siempre devuelve False, indicando que los invitados tienen permisos limitados (en este contexto, se interpreta como no tener
permisos de escritura o modificación).

• __str__(self): Define cómo se representa un objeto Invitado como una cadena de texto, mostrando su ID y nombre, indicando que es un Invitado.
   Evidencia de ejecución

   
 ![Captura de pantalla 2025-05-26 092844](https://github.com/user-attachments/assets/3a55cdd8-0bb2-4eae-873e-524b3a405fd1)



**Operador**

la clase Operado es un molde para crear usuarios que son operadores en el sistema, con la capacidad de tener permisos específicos
para realizar ciertas tareas.

•	Hereda de Usuario.

•	Tiene permisos operativos (más que un invitado, menos que un administrador).

•	Método sobrescrito: verificar_permisos() devuelve True.
  Atributos: Hereda los siguientes atributos de la clase Usuario:
  
1	usuario_id: Identificador único del operador.

2	nombre: Nombre del operador.

3	clave: Contraseña del operador.

  Metodos
  
1	__init__(self, usuario_id, nombre, clave): El constructor de la clase Operador. Llama al constructor de la clase padre (Usuario) 
para inicializar los atributos básicos.

2	verificar_permisos(self): Implementación específica para la clase Operador. En esta versión, devuelve True, lo que indica que
los operadores tienen permisos para realizar ciertas operaciones dentro del sistema. La naturaleza exacta de estas operaciones 
no se define en esta clase, pero se diferencia de los permisos totales del Administrador y los permisos limitados del Invitado.

3	__str__(self): Define cómo se representa un objeto Operador como una cadena de texto, mostrando su ID y nombre.
Evidencia de ejecución


![Captura de pantalla 2025-05-26 093551](https://github.com/user-attachments/assets/c7624f3c-e98b-43c4-81c6-42d81ff1c402)



**Acceso**

La clase Acceso guarda información crucial sobre quién intentó acceder, cuándo lo hizo y si se le permitió la entrada.
Esto es fundamental para llevar un registro de la actividad del sistema y potencialmente para auditorías de seguridad.

  Atributos
  
I.	usuario: Un objeto de la clase Usuario (o una de sus subclases, como Administrador, Invitado, Operador) 
que representa a la persona que intentó acceder.

II.	hora: Un objeto datetime que indica el momento exacto en que se realizó el intento de acceso.

III.	exitoso: Un valor booleano (True o False) que señala si el acceso fue concedido o no.
  Métodos (Properties)
  
1.	La clase utiliza properties para acceder a sus atributos de forma controlada:

2.	usuario: Permite obtener el objeto Usuario asociado con el acceso
  
3.	hora: Permite obtener la hora del intento de acceso.

4.	exitoso: Permite saber si el acceso fue exitoso.
   
   
  Método __str__
  
•	 __str__(self): Define cómo se mostrará un objeto Acceso cuando se use la función print().
Proporciona una representación legible que incluye el nombre del usuario, la hora del acceso (en formato Año-Mes-Día Hora:Minuto:Segundo) y el estado del acceso (Exitoso o Fallido).

•	Representa un intento de acceso al sistema.

•	Estado (éxito o fallo)
 Evidencia de ejecución


![Captura de pantalla 2025-05-26 095046](https://github.com/user-attachments/assets/e96e90ea-df5d-4f19-bbfd-8e0fdaab5f31)



 **Historial**

la clase Historial actúa como un contenedor y una herramienta para gestionar y visualizar la historia de quién ha intentado acceder 
al sistema y cuándo.

  Atributos
  
• _registros: Una lista Python donde se guardan todos los objetos de la clase Acceso que representan los intentos de acceso. 
Inicialmente, esta lista está vacía.

    Métodos
    
I.	__init__(self: El constructor de la clase Historial. Simplemente inicializa la lista vacía _registros.

II.	registrar_acceso(self, acceso: Acceso): Este método toma un objeto de la clase Acceso como argumento y lo añade a la lista
_registros. Cada vez que alguien intenta acceder (ya sea con éxito o no), se crea un objeto Acceso y se registra aquí.

III.	listar_accesos(self): Este método recorre la lista _registros y para cada objeto Acceso que encuentra,
imprime su información utilizando el método __str__ definido en la clase Acceso. Esto permite ver un listado de todos los accesos registrados.

Evidencia de  ejecución


![Captura de pantalla 2025-05-26 095840](https://github.com/user-attachments/assets/3d86ce92-76ee-4726-9099-c156bad5211c)



**Archivo Principal: main.py**

1.	Ejecuta pruebas de integración entre las clases:
   
2.	Crea usuarios de tipo Administrador, Invitado, y Operador.
   
3.	Verifica los permisos de cada uno usando polimorfismo.
   
4.	Simula accesos al sistema y almacena los registros en un historial.
   
5.	Muestra el historial de accesos con hora y estado.
    
Evidencia de ejecución


![Captura de pantalla 2025-05-26 100108](https://github.com/user-attachments/assets/066f5f5c-8a48-4659-893a-3962a05d95ee)


EVIDENCIA DE TRABAJO EN EQUIPO 


![Captura de pantalla 2025-05-25 215213](https://github.com/user-attachments/assets/47d80871-87cb-47ce-871a-e2045e945ad9)


![Captura de pantalla 2025-05-25 215243](https://github.com/user-attachments/assets/3a0c1ee9-e2e6-4486-ac5f-0393edd6a4d4)


![Captura de pantalla 2025-05-25 215301](https://github.com/user-attachments/assets/71b4aeec-a392-49c4-b99c-b1e6bc3d6df5)
















 















 





