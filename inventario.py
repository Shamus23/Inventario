#Inventario.
print("INVENTARIO")
#Este programa calcula el valor total del producto en existencia dentro del inventario.
#Declaracion de variables.
nombre: str = ""; precio: float  = 0.0 ;cantidad: int = 0
#Solicita el ingreso del dato: Nombre del producto y lo asigna a la variable nombre.
nombre = str(input("ingrese el nombre : "))
#Solicita el ingreso del dato: Precio y lo asigna a la variable precio, asegurandose que sea un dato valido.
while True :
    try :
        precio = float(input("ingrese el precio : "))
        break 
    except: print("Ingrese un dato valido")
#Solicita el ingreso del dato: Cantidad y lo asigna a la variable cantidad, asegurandose que sea un dato valido.
while True :
    try :
        cantidad = int(input("ingrese la cantidad : "))
        break 
    except: print("Ingrese un dato valido")
#Calcular el Total y asignarlo en la variable costo_total, multiplicando precio*cantidad.
costo_total = precio*cantidad
#Imprime el mensaje final 
print("Producto : ",nombre)
print("Precio : ",precio)
print("Cantidad : ",cantidad)
print("Total : ",costo_total)