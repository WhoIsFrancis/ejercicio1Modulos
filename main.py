from operacionesBasicas import operaciones


def main():
    print("Suma: ", operaciones.suma(10, 20))
    print("Resta: ", operaciones.resta(44, 20))
    print("Multiplicar: ", operaciones.multplicacion(3, 9))
    print("Division: ", operaciones.dividir(7, 10))
    print("Division: ", operaciones.dividir(7, 0))


if __name__ == '__main__':
    main()
