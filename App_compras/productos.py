class Producto:

    def __init__(self , codigo , nombreP , presentacion , precio , otro = None):
        self.codigo = codigo
        self.nombreP = nombreP
        self.presentacion = presentacion
        self.precio = precio
        self.otro = otro

    def __str__(self):
        return f"codigo: {self.codigo} nombre: {self.nombreP} otro: {self.otro}"