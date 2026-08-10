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

def mostrar_bandas(bandas):
    if len(bandas) == 0:
        print("\nNo hay bandas registradas.")
    else:
        print("\nBANDAS REGISTRADAS")
        print("-------------------")

        for i in range(len(bandas)):
            print("\nBanda:", bandas[i][0])
            print("Entradas vendidas:", bandas[i][1])
            print("Monto recaudado: $", bandas[i][2], sep="")


def ordenar_bandas(bandas):
    # Ordenamiento por selección de mayor a menor recaudación
    for i in range(len(bandas) - 1):

        posicion_mayor = i

        for j in range(i + 1, len(bandas)):
            if bandas[j][2] > bandas[posicion_mayor][2]:
                posicion_mayor = j

        if posicion_mayor != i:
            auxiliar = bandas[i]
            bandas[i] = bandas[posicion_mayor]
            bandas[posicion_mayor] = auxiliar

    print("\nRANKING POR RECAUDACIÓN")
    print("-----------------------")

    for i in range(len(bandas)):
        print(
            str(i + 1) + ".",
            bandas[i][0],
            "- $" + str(bandas[i][2])
        )


def buscar_banda(bandas):
    nombre_buscado = input("\nIngrese el nombre de la banda a buscar: ").strip()

    while nombre_buscado == "":
        print("El nombre no puede estar vacío.")
        nombre_buscado = input("Ingrese el nombre de la banda a buscar: ").strip()

    encontrada = False
    i = 0

    while i < len(bandas) and encontrada == False:

        if bandas[i][0].lower() == nombre_buscado.lower():
            encontrada = True
        else:
            i = i + 1

    if encontrada:
        print("\nBANDA ENCONTRADA")
        print("----------------")
        print("Banda:", bandas[i][0])
        print("Entradas vendidas:", bandas[i][1])
        print("Monto recaudado: $", bandas[i][2], sep="")
    else:
        print("\nLa banda no se encuentra registrada.")


def mostrar_estadisticas(bandas):
    total_bandas = len(bandas)
    total_entradas = 0
    total_recaudado = 0

    mayor_entradas = bandas[0][1]
    banda_mayor_entradas = bandas[0][0]

    for i in range(len(bandas)):

        total_entradas = total_entradas + bandas[i][1]
        total_recaudado = total_recaudado + bandas[i][2]

        if bandas[i][1] > mayor_entradas:
            mayor_entradas = bandas[i][1]
            banda_mayor_entradas = bandas[i][0]

    promedio_entradas = total_entradas / total_bandas

    print("\nESTADÍSTICAS DEL FESTIVAL")
    print("-------------------------")
    print("Cantidad de bandas:", total_bandas)
    print("Total de entradas vendidas:", total_entradas)
    print("Total recaudado: $", total_recaudado, sep="")
    print("Promedio de entradas por banda:", round(promedio_entradas, 2))
    print("Banda que más entradas vendió:", banda_mayor_entradas)
    print("Cantidad de entradas:", mayor_entradas)


def main():
    bandas = cargar_bandas()

    mostrar_bandas(bandas)

    if len(bandas) > 0:
        ordenar_bandas(bandas)

        mostrar_bandas(bandas)

        buscar_banda(bandas)

        mostrar_estadisticas(bandas)


if __name__ == "__main__":
    main()