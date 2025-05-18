class Cliente:
    """
    Modelo de un cliente en la tienda.
    """

    def __init__(self, username: str, password: str, email: str, address: str):
        self.username = username
        self._password = password
        self.email = email
        self.address = address
        self.orders = []  # lista de pedidos (ejemplo de atributo adicional)

    def __str__(self):
        return f"Cliente({self.username}, {self.email})"

    def verificar_contrasena(self, password: str) -> bool:
        """Verifica que la contraseña coincida."""
        return self._password == password

    def actualizar_direccion(self, new_address: str):
        """Actualiza la dirección del cliente."""
        self.address = new_address


class ClienteVIP(Cliente):
    def __init__(self, username: str, password: str, email: str, address: str, discount: float):
        super().__init__(username, password, email, address)
        self.discount = discount

    def obtener_descuento(self) -> float:
        """Retorna el porcentaje de descuento para el cliente VIP."""
        return self.discount