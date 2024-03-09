from productos import Producto
from clientes import Cliente

class Pedidos:
 def __init__(self, producto , cliente , precio):
  self.producto = producto
  self.cliente = cliente
  self.precio = precio
  self.lista_productos =[]

#  def Monto(self, cliente , cantidad , precio):
#   print("el pedido de:" , {self.cliente.nombre} , "se ha procesado costo:" , {self.cantidad} * {self.precio})

 def ver_productos(self):
  #print("ingrese sus productos:",{self.Pedidos})
  print("Lista de productos:")

  producto_uno = Producto(7086 , "Jabon Liquido" , "20 litros" , 12000 )
  producto_dos = Producto(7087 , "Lavandina" , "20 litros" , 9000 )
  producto_tres = Producto(7088 , "Limpiapiso" , "10 litros" , 5000 )

  self.lista_productos = [producto_uno , producto_dos , producto_tres]

  for productos in self.lista_productos:
   print(productos)
#pedido_uno = Pedidos(producto_uno )

 def elegir_producto(self):
    codigo=int(input('Elija un producto: (codigo)'))
    for producto in self.lista_productos:
      if producto.codigo == codigo:
        print(f'Ha comprado: {producto.nombreP}')
    