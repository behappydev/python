class Cliente:
    """
    Modelo de un cliente en la tienda.
    """

    def __init__(self, username: str, password: str, email: str, address: str):
        self.username = username
        self._password = password
        self.email = email
        self.address = address
        self.orders = [] 

    def __str__(self) -> str:
        return f"Cliente({self.username}, {self.email})"

    def verificar_contrasena(self, password: str) -> bool:
        """Verifica que la contraseña coincida."""
        return self._password == password

    def actualizar_direccion(self, new_address: str) -> None:
        """Actualiza la dirección del cliente."""
        self.address = new_address


class ClienteVIP(Cliente):
    """
    Cliente con beneficios VIP.
    """

    def __init__(self, username: str, password: str, email: str, address: str, discount: float):
        super().__init__(username, password, email, address)
        self.discount = discount  

    def __str__(self) -> str:
        pct = int(self.discount * 100)
        return f"ClienteVIP({self.username}, {self.email}, Descuento: {pct}% )"

    def obtener_descuento(self) -> float:
        """Retorna el porcentaje de descuento."""
        return self.discount