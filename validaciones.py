"""Funciones de validación de datos de entrada."""
from datetime import datetime


def validar_dni(dni):
    """El DNI debe tener exactamente 8 dígitos."""
    return len(dni) == 8 and dni.isdigit()


def validar_texto(texto):
    """El texto no puede estar vacío ni contener el separador '|'."""
    return len(texto.strip()) > 0 and "|" not in texto


def validar_tramite(opcion):
    """El tipo de trámite debe ser 1, 2, 3 o 4."""
    return opcion in (1, 2, 3, 4)


def validar_fecha(fecha):
    """Valida el formato DD/MM/AAAA y que sea una fecha real y no futura.

    Usa datetime.strptime (conocimiento nuevo, fuera del temario de clase).
    Rechaza casos como '31/02/2026', '13/11/2026ss' o '1/1/2026'.
    """
    if len(fecha) != 10:
        return False
    try:
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        return False
    return fecha_dt <= datetime.now()
