from .cliente import Cliente, ClienteVIP

# Credenciales fijas de administrador
ADMIN_USER = 'admin'
ADMIN_PASS = 'admin'

# Catálogo de productos de ejemplo
def cargar_productos() -> list:
    return [
        {'id': 1, 'nombre': 'Camiseta', 'precio': 19.99},
        {'id': 2, 'nombre': 'Pantalón',  'precio': 39.50},
        {'id': 3, 'nombre': 'Zapatos',   'precio': 59.90},
        {'id': 4, 'nombre': 'Gorra',     'precio': 12.00},
    ]

# ------ FUNCIONES DE CLIENTE ------

def registrar_cliente(clientes: dict) -> None:
    """Registra un nuevo cliente normal."""
    while True:
        username = input("Nuevo username: ").strip()
        if not username:
            print("El nombre de usuario no puede estar vacío.")
            continue
        if username in clientes or username == ADMIN_USER:
            print("El nombre de usuario ya está en uso.")
        else:
            break

    password = input("Password: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    clientes[username] = Cliente(username, password, email, address)
    print(f"Cliente '{username}' registrado exitosamente.\n")


def login_cliente(clientes: dict) -> Cliente:
    """Inicia sesión como cliente o VIP."""
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = clientes.get(username)
    if not user:
        print("Usuario no registrado.\n")
        return None
    if not user.verificar_contrasena(password):
        print("Contraseña incorrecta.\n")
        return None
    print(f"Bienvenido, {username}!\n")
    return user

# ------ FUNCIONES DE ADMIN ------

def login_admin() -> bool:
    """Valida credenciales de administrador."""
    user = input("Admin user: ").strip()
    pwd = input("Admin password: ").strip()
    if user == ADMIN_USER and pwd == ADMIN_PASS:
        print("Acceso de administrador concedido.\n")
        return True
    print("Credenciales de administrador inválidas.\n")
    return False


def mostrar_clientes(clientes: dict) -> None:
    """Muestra todos los clientes (normales y VIP)."""
    if not clientes:
        print("No hay clientes registrados.\n")
        return
    print("Listado de clientes:")
    for c in clientes.values():
        print(f"- {c}")
    print()


def elevar_a_vip(clientes: dict) -> None:
    """Promueve un cliente normal a VIP con porcentaje de descuento."""
    username = input("Username a promover: ").strip()
    user = clientes.get(username)
    if not user:
        print("Cliente no encontrado.\n")
        return
    if isinstance(user, ClienteVIP):
        print("El cliente ya es VIP.\n")
        return
    try:
        discount = float(input("Descuento (0.0-1.0): "))
        if not (0.0 <= discount <= 1.0):
            raise ValueError
    except ValueError:
        print("Valor de descuento inválido. Debe ser entre 0.0 y 1.0.\n")
        return
    # Reemplazo de instancia
    nuevos_datos = (user.username, user._password, user.email, user.address)
    clientes[username] = ClienteVIP(*nuevos_datos, discount)
    print(f"Cliente '{username}' elevado a VIP con {int(discount*100)}% de descuento.\n")

# ------ FUNCIÓN PARA MOSTRAR PRODUCTOS ------

def mostrar_productos(productos: list, cliente) -> None:
    """Muestra catálogo aplicando descuento si el cliente es VIP."""
    if not cliente:
        print("Debes estar logueado como cliente para ver productos.\n")
        return
    print("Catálogo de productos:")
    for p in productos:
        price = p['precio']
        if isinstance(cliente, ClienteVIP):
            price *= (1 - cliente.obtener_descuento())
        print(f"{p['id']}. {p['nombre']} - U$S {price:.2f}")
    print()

# ------ MENÚ PRINCIPAL ------

def menu():
    clientes = {}  
    productos = cargar_productos()
    session = {'user': None, 'role': None}  

    while True:
        if session['role'] is None:
            # Menú sin sesión
            print("--- Bienvenido a Shop ---")
            print("1. Registrarse")
            print("2. Iniciar sesión")
            print("3. Administrador")
            print("4. Salir")
            choice = input("Opción: ").strip()

            if choice == '1':
                registrar_cliente(clientes)
            elif choice == '2':
                user = login_cliente(clientes)
                if user:
                    session.update(user=user, role='client')
            elif choice == '3':
                if login_admin():
                    session.update(user='admin', role='admin')
            elif choice == '4':
                print("Gracias por usar Shop. Hasta luego!")
                break
            else:
                print("Opción inválida. Inténtelo de nuevo.\n")

        elif session['role'] == 'client':
            # Menú de cliente
            print(f"--- Cliente: {session['user'].username} ---")
            print("1. Ver productos")
            print("2. Cerrar sesión")
            choice = input("Opción: ").strip()

            if choice == '1':
                mostrar_productos(productos, session['user'])
            elif choice == '2':
                print(f"Sesión cerrada para {session['user'].username}.\n")
                session.update(user=None, role=None)
            else:
                print("Opción inválida. Inténtelo de nuevo.\n")

        elif session['role'] == 'admin':
            # Menú de administrador
            print("--- Panel Administrador ---")
            print("1. Mostrar clientes")
            print("2. Elevar cliente a VIP")
            print("3. Cerrar sesión")
            choice = input("Opción: ").strip()

            if choice == '1':
                mostrar_clientes(clientes)
            elif choice == '2':
                elevar_a_vip(clientes)
            elif choice == '3':
                print("Cierre de sesión de administrador.\n")
                session.update(user=None, role=None)
            else:
                print("Opción inválida. Inténtelo de nuevo.\n")

if __name__ == '__main__':
    menu()