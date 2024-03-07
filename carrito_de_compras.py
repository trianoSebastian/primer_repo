class Carrito:
	def __init__(self):
		"""
		En el constructor creamos una lista vacía que va actuar como carrito y una variable que va a funcionar como contador de los productos.
		"""
		self.articulos = []
		self.cantidad = 0

	def agregar_articulo(self,articulo,precio):
		"""
		El metodo agregar_articulo recibe como argumentos el articulo y el precio que luego agrega a un diccionario. Finalmente aumenta el contador de productos en 1 unidad.
		"""
		self.articulos.append({'articulo':articulo,'precio':precio})
		self.cantidad +=1

	def ver_articulos(self):
		"""
		Este metodo imprime la cantidad actual de articulos que hay en la lista. Y con un ciclo for recorre la lista articulos e imprimer cada elemento en pantalla. La impresion la hace a traves de llamar la clave de cada elemento del diccionario, lo que devuelve el valor almacenado.
		"""
		print(f'Cantidad de artículos: {self.cantidad}')
		for item in self.articulos:
			print('{0} - ${1}'.format(item['articulo'],item['precio']))
			#print(type(item))

	def remover_articulo(self,articulo):
		"""
		Este metodo recibe como argumento un articulo, con un ciclo for recorre la lista de productos. Dentro del ciclo, si el valor del elemento actual coincide con el valor pasado por argumento, se remueve ese articulo. Finalmente decrementa la cantidad en 1 unidad. 
		"""
		for item in self.articulos:
			if item['articulo'] == articulo:
				self.articulos.remove(item)
				self.cantidad -=1

	def calcular_total(self):
		"""
		Este metodo calcula el monto total de la compra, sumando el precio de los articulos, accediendo al mismo a traves de la clave de cada elemento dentro del diccionario. 
		"""
		total = 0
		for item in self.articulos:
			total += item['precio']
		return total


mi_carrito = Carrito()

mi_carrito.agregar_articulo('remera',2500)
mi_carrito.agregar_articulo('zapatillas',90000)
mi_carrito.agregar_articulo('short',8500)
mi_carrito.agregar_articulo('buzo',140000)
print()
mi_carrito.ver_articulos()
print()
print('El valor de la compra es: $',mi_carrito.calcular_total())
mi_carrito.remover_articulo('buzo')
print()
mi_carrito.ver_articulos()
print()


print('El valor de la compra es: $',mi_carrito.calcular_total())
