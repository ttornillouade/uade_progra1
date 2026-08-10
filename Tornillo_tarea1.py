import random


def cargar_bandas():
    bandas = []

    nombre_banda = input("Ingrese el nombre de una banda (-1 para finalizar): ").strip()

    while nombre_banda != "-1":

        while nombre_banda == "":
            print("El nombre de la banda no puede estar vacío.")
            nombre_banda = input("Ingrese el nombre de una banda (-1 para finalizar): ").strip()

        entradas_vendidas = random.randint(1000, 1500)
        precio_promedio = random.randint(150, 300)

        monto_recaudado = entradas_vendidas * precio_promedio

        fila = [nombre_banda, entradas_vendidas, monto_recaudado]
        bandas.append(fila)

        nombre_banda = input(
            "\nIngrese el nombre de otra banda (-1 para finalizar): "
        ).strip()

    return bandas