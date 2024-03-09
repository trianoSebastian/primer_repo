from clientes import Cliente #tiene que recurrir a la clase cliente

#lista_clientes.append(Cliente(input("Miranda", "Pompas de Jabon", 4225076, "direccion 1")))
def Carga_cliente():
 lista_clientes = []
# while True:
 bienvenida = print("Bienvenido ,haga su pedido ya mismo!")
 #respuesta = (input("Bienvenido ,haga su pedido ya mismo!"))
#  if  respuesta == "si":
# Solicitar al usuario que ingrese los detalles de cada cliente por teclado
 for i in range(1):  # Puedes ajustar el rango según el número de clientes que desees ingresar
     nombre = input("Ingrese el nombre del cliente: ")
     #empresa = input("Ingrese el nombre de la empresa: ")
     telefono = int(input("Ingrese el número de teléfono: "))
     direccion = input("Ingrese la dirección: ")

    # Crear un nuevo objeto Cliente y agregarlo a la lista_clientes
     nuevo_cliente = Cliente(nombre, telefono, direccion)
     lista_clientes.append(nuevo_cliente)

 for nuevo_cliente in lista_clientes: 
     print(nuevo_cliente)

"""else:
break
print("fin!")
Escribir la lista de clientes en un archivo de texto 
------
with open("lista_clientes.txt", "w") as file:
        for nuevo_cliente in lista_clientes:
            file.write(f"Nombre: {nuevo_cliente.nombre}\n")
             file.write(f"Empresa: {nuevo_cliente.empresa}\n")
            file.write(f"Teléfono: {nuevo_cliente.telefono}\n")
            file.write(f"Dirección: {nuevo_cliente.direccion}\n")
            file.write("\n")
"""
 