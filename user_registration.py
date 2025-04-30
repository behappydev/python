def registrar_usuario(usuarios):
    """Función para registrar un nuevo usuario."""
    while True:
        nombre = input("Ingrese nombre de usuario: ")
        if nombre in usuarios:
            print("El nombre de usuario ya existe. Intente con otro.")
        else:
            break
    contrasena = input("Ingrese contraseña: ")
    usuarios[nombre] = contrasena
    print(f"Usuario '{nombre}' registrado con éxito.\n")


def login_usuario(usuarios):
    """Función para iniciar sesión de un usuario existente."""
    nombre = input("Ingrese nombre de usuario: ")
    contrasena = input("Ingrese contraseña: ")
    if nombre in usuarios and usuarios[nombre] == contrasena:
        print(f"Bienvenido, {nombre}!\n")
    else:
        print("Usuario o contraseña incorrectos.\n")


def mostrar_usuarios(usuarios):
    """Función para mostrar todos los usuarios registrados."""
    if usuarios:
        print("Usuarios registrados:")
        for nombre, contrasena in usuarios.items():
            print(f"- {nombre}: {contrasena}")
        print()
    else:
        print("No hay usuarios registrados.\n")


def main():
    """Función principal que muestra el menú y gestiona la interacción."""
    usuarios = {}
    while True:
        print("Seleccione una opción:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Mostrar usuarios")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            login_usuario(usuarios)
        elif opcion == "3":
            mostrar_usuarios(usuarios)
        elif opcion == "4":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()
