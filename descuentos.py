print("\n1. Porcentaje")
print("2. M * N")
print("3. Descuento X por cada Y")
print()
tipoDescuento = int(input("Tipo de descuento: "))
print()

if tipoDescuento == 1:
    precio = float(input("Precio: $"))
    porcentaje = int(input("Descuento: %"))
    descuento = precio * porcentaje / 100
    precioFinal = precio - descuento
    print("Descuento: $", descuento)
    print("Precio final: $", precioFinal)
    
elif tipoDescuento == 2:
    m = int(input("Valor de M: "))
    n = int(input("Valor de n: "))
    mismoPrecio = input("Mismo precio (s/n)? ") == "s"
    
    if mismoPrecio:
        precio = float(input("Precio: $"))
        precioFinal = precio * n
        precioPieza = precioFinal / m
        print("Precio por pieza: $", precioPieza)
        print("Precio promoción: $", precioFinal)
    
    else:
        print("Capturar precio de cada producto")
    
elif tipoDescuento == 3:
    x = float(input("Valor de X: "))
    y = float(input("Valor de Y: "))
    precio = float(input("Precio: $"))
    nDescuentos = int(precio / y)
    descuento = x * nDescuentos
    precioFinal = precio - descuento
    print("Descuento: $", descuento)
    print("Precio final: $", precio - descuento)
    