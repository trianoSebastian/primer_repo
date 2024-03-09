from clientes import Cliente
from Add_client import Carga_cliente
from pedido import Pedidos
#from pedido import Elegir

Carga_cliente()
print()
#Pedidos.Elegir() 
pedido_uno =  Pedidos("producto1" , "Juan perez" , 5)
pedido_uno.ver_productos()
print()
pedido_uno.elegir_producto()
print()

 
#luego de ejecutar Carga_cliente aparece los detalles del mismo, necesitamos que solo aparezca el listado de productos para que concrete su pedido


#tiene que recurrir una clase que te imprima el detalle del pedido ,el monto a pagar y el cliente