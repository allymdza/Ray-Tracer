from vectores import vectores

def colores_int(color):
    rojo = color.x
    verde = color.y
    azul = color.z

    rojo = min(1, max(0, rojo))
    verde = min(1, max(0, verde))
    azul = min(1, max(0, azul))

    rojo = round(rojo * 255)
    verde = round(verde * 255)
    azul = round(azul * 255)

    return rojo, verde, azul

def escribir_ppm(nombre_archivo, ancho, alto, pixeles):
    tamanio = ancho * alto
    if len(pixeles) != tamanio:
        raise ValueError("No coinciden los valores")
    with open(nombre_archivo, "w") as f:
        f.write("P3\n")
        f.write(f"{ancho} {alto}\n")
        f.write("255\n")
        for color in pixeles:
            r, g ,b = colores_int(color)
            f.write(f"{r} {g} {b}\n")

