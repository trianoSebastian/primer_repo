class Carrito:

    """
    En el constructor creamos una lista vacía que va actuar como carrito y una variable que va a funcionar como contador de los productos.
    """
    def __init__(self):
        self.articulos = []
        self.cantidad = 0
    
  
    def agregar_articulo(self,articulo,precio):
        """
        El metodo agregar_articulo recibe como argumentos el articulo y el precio que luego agrega a un diccionario. Finalmente aumenta el contador de productos en 1 unidad.
        """
        self.articulos.append({'articulo':articulo,'precio':precio})
        self.cantidad += 1
    
    def ver_carrito(self):    
        """
        Este metodo imprime la cantidad actual de articulos que hay en la lista. Y con un ciclo for recorre la lista articulos e imprime cada elemento en pantalla. La impresion la hace a traves de llamar la clave de cada elemento del diccionario, lo que devuelve el valor almacenado.
        """
        print('Cantidad de productos:',self.cantidad)
        for item in self.articulos:
            print('{0} - ${1}'.format(item['articulo'],item['precio']))
        
    def remover_articulo(self,articulo):
        """Este metodo recibe como argumento un articulo, con un ciclo for recorre la lista de productos. Dentro del ciclo, si el valor del elemento actual coincide con el valor pasado por argumento, se remueve ese articulo. Finalmente decrementa la cantidad en 1 unidad. 
        """
        for item in self.articulos:
            if item['articulo'] == articulo:
                self.articulos.remove(item)
                self.cantidad -=1
            
    def total_compra(self):
        """
        Este metodo calcula el monto total de la compra con un ciclo for, sumando el precio de los articulos, accediendo al mismo a traves de la clave de cada elemento dentro del diccionario. 
        """
        total = 0
        for item in self.articulos:
            total += item['precio']
        return total

mi_carrito = Carrito()

mi_carrito.agregar_articulo('zapatillas',150000)
mi_carrito.agregar_articulo('remera',8000)
mi_carrito.ver_carrito()
print(f'${mi_carrito.total_compra()}')
  
  
  
  