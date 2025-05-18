from .cliente import Cliente, ClienteVIP


def registrar_cliente(clientes: dict):
    username = input("Username: ")
    if username in clientes:
        print("Usuario ya existe.\n")
        return
    password = input("Password: ")
    email = input("Email: ")
    address = input("Address: ")
    clientes[username] = Cliente(username, password, email, address)
    print(f"Cliente '{username}' registrado.\n")


def login_cliente(clientes: dict):
    username = input("Username: ")
    password = input("Password: ")
    cliente = clientes.get(username)
    if cliente and cliente.verificar_contrasena(password):
        print(f"Bienvenido {cliente}\n")
    else:
        print("Credenciales inválidas.\n")


def mostrar_clientes(clientes: dict):
    if not clientes:
        print("No hay clientes registrados.\n")
        return
    print("Clientes registrados:")
    for cliente in clientes.values():
        print(f"- {cliente}")
    print()


def menu():
    clientes = {}
    opciones = {
        "1": registrar_cliente,
        "2": login_cliente,
        "3": mostrar_clientes
    }
    while True:
        print("1. Registrar cliente")
        print("2. Iniciar sesión")
        print("3. Mostrar clientes")
        print("4. Salir")
        opcion = input("Opción: ")
        if opcion == "4":
            print("Hasta luego!")
            break
        accion = opciones.get(opcion)
        if accion:
            accion(clientes)
        else:
            print("Opción inválida. Intente de nuevo.\n")


if __name__ == "__main__":
    menu()