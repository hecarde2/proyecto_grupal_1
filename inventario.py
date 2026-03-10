nombre=input("Ingrese su nombre: ")
print("Hola", nombre, "bienvenido al programa de inventario")
precio=float(input("Ingrese el precio del producto: "))
cantidad=int(input("Ingrese la cantidad del producto: "))

if precio < 0 or cantidad < 0:
    print("Error: El precio y la cantidad deben ser números positivos.")    
else:
    total=precio*cantidad
    print("El total del inventario es:", total)