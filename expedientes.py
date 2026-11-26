#ordenamiento burbuja de expediente por codigo
"""Operaciones sobre los expedientes (arreglos paralelos)."""
from validaciones import (
    validar_dni, validar_texto, validar_tramite, validar_fecha,)
LIMITE = 100
def nombre_tramite(opcion):
    tramites = {
        1: "Constancia de matricula",
        2: "Constancia de vacante",
        3: "Certificado de estudios",
        4: "Ficha unica de matricula (FUM)",
    }
    return tramites.get(opcion, "Desconocido")
def generar_codigo(cod):
    mayor = 0
    for c in cod:
        if c > mayor:
            mayor = c
    return mayor + 1

def _pedir_dni(mensaje):
    while True:
        dni = input(mensaje).strip()
        if validar_dni(dni):
            return dni
        print("El DNI debe contener exactamente 8 digitos.")

def _pedir_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip().upper()
        if validar_texto(nombre):
            return nombre
        print("Ingrese un nombre valido.")

def _pedir_tramite():
    print("\nTIPOS DE TRAMITE")
    print("1. Constancia de matricula")
    print("2. Constancia de vacante")
    print("3. Certificado de estudios")
    print("4. Ficha unica de matricula (FUM)")
    while True:
        try:
            tipo = int(input("Seleccione el tipo de tramite: "))
            if validar_tramite(tipo):
                return tipo
            print("Seleccione una opcion entre 1 y 4.")
        except ValueError:
            print("Ingrese un numero valido.")

def _pedir_fecha():
    while True:
        fecha = input("Fecha de recepcion (DD/MM/AAAA): ").strip()
        if validar_fecha(fecha):
            return fecha
        print("Fecha invalida. Use DD/MM/AAAA, una fecha real y no futura.")

def registrar_expediente(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n):
    print("\n--- REGISTRO DE NUEVO EXPEDIENTE ---")

    if n >= LIMITE:
        print(f"Se alcanzo el limite de {LIMITE} expedientes.")
        return n

    codigo = generar_codigo(cod)
    dni_apoderado = _pedir_dni("DNI del apoderado: ")
    nombre_apoderado = _pedir_nombre("Nombre del apoderado: ")
    dni_estudiante = _pedir_dni("DNI del estudiante: ")
    nombre_estudiante = _pedir_nombre("Nombre del estudiante: ")
    tipo = _pedir_tramite()
    fecha = _pedir_fecha()

    cod.append(codigo)
    dni_a.append(dni_apoderado)
    nom_a.append(nombre_apoderado)
    dni_e.append(dni_estudiante)
    nom_e.append(nombre_estudiante)
    tram.append(tipo)
    fec.append(fecha)
    n += 1

    print("\nExpediente registrado correctamente. Codigo asignado: EXP-" + str(codigo))
    return n

def _mostrar(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, i):
    print("Codigo: EXP-", cod[i], sep="")
    print("DNI apoderado:", dni_a[i])
    print("Apoderado:", nom_a[i])
    print("DNI estudiante:", dni_e[i])
    print("Estudiante:", nom_e[i])
    print("Tramite:", nombre_tramite(tram[i]))
    print("Fecha de recepcion:", fec[i])

def consultar_expediente(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n):
    print("\n--- CONSULTA DE EXPEDIENTE ---")

    try:
        codigo = int(input("Ingrese el codigo que desea consultar: "))
    except ValueError:
        print("Codigo invalido.")
        return

    for i in range(n):
        if cod[i] == codigo:
            print("\nEXPEDIENTE ENCONTRADO")
            print("--------------------------------")
            _mostrar(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, i)
            return

    print("No se encontro el expediente solicitado.")

def ordenar_por_codigo(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n):
    """Ordenamiento burbuja ascendente por código."""
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if cod[j] > cod[j + 1]:
                cod[j], cod[j + 1] = cod[j + 1], cod[j]
                dni_a[j], dni_a[j + 1] = dni_a[j + 1], dni_a[j]
                nom_a[j], nom_a[j + 1] = nom_a[j + 1], nom_a[j]
                dni_e[j], dni_e[j + 1] = dni_e[j + 1], dni_e[j]
                nom_e[j], nom_e[j + 1] = nom_e[j + 1], nom_e[j]
                tram[j], tram[j + 1] = tram[j + 1], tram[j]
                fec[j], fec[j + 1] = fec[j + 1], fec[j]

    print("Expedientes ordenados correctamente.")

def listar_expedientes(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n):
    print("\n--- EXPEDIENTES REGISTRADOS ---")

    if n == 0:
        print("No hay expedientes registrados.")
        return

    for i in range(n):
        print("\n--------------------------------")
        _mostrar(cod, dni_a, nom_a, dni_e, nom_e, tram, fec, i)

def contar_por_tramite(tram):
    """Devuelve [c1, c2, c3, c4] con la cantidad de expedientes por trámite."""
    conteo = [0, 0, 0, 0]
    for tipo in tram:
        if 1 <= tipo <= 4:
            conteo[tipo - 1] += 1
    return conteo

def mostrar_resumen(tram, n):
    c1, c2, c3, c4 = contar_por_tramite(tram)
    print("\n--- RESUMEN DE ATENCIONES ---")
    print("Total de expedientes:", n)
    print("Constancia de matricula:", c1)
    print("Constancia de vacante:", c2)
    print("Certificado de estudios:", c3)
    print("Ficha unica de matricula (FUM):", c4)
