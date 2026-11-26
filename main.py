"""Mesa de Partes Digital - I.E. 2032 (programa principal)."""
from archivos import RUTA_ARCHIVO, cargar_archivo, guardar_archivo
from expedientes import (
    registrar_expediente, consultar_expediente, ordenar_por_codigo,
    listar_expedientes, mostrar_resumen,
)


def main():
    cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n = cargar_archivo(RUTA_ARCHIVO)

    while True:
        print("\n=====================================")
        print(" MESA DE PARTES DIGITAL - I.E. 2032")
        print("=====================================")
        print("1. Registrar expediente")
        print("2. Consultar expediente por codigo")
        print("3. Ordenar por codigo y listar")
        print("4. Ver resumen")
        print("5. Guardar")
        print("6. Guardar y salir")

        try:
            opcion = int(input("Seleccione una opcion (1-6): "))
        except ValueError:
            print("Ingrese una opcion numerica valida.")
            continue

        if opcion == 1:
            n = registrar_expediente(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n)
        elif opcion == 2:
            consultar_expediente(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n)
        elif opcion == 3:
            ordenar_por_codigo(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n)
            listar_expedientes(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n)
        elif opcion == 4:
            mostrar_resumen(tram, n)
        elif opcion == 5:
            guardar_archivo(RUTA_ARCHIVO, cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n)
        elif opcion == 6:
            guardar_archivo(RUTA_ARCHIVO, cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n)
            print("Saliendo del sistema. Gracias por utilizarlo.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()
