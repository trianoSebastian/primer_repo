class Cliente:

    def __init__(self , nombre , telefono , direccion):
        self.nombre = nombre
        #self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion

   # def __str__(self):
   #     return f"nombre: {self.nombre} local: {self.empresa} telefono: {self.telefono}"
    def __str__(self):
        return f"nombre: {self.nombre}  telefono: {self.telefono} direccion: {self.direccion}"