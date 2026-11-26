"""Pruebas automáticas. Ejecutar desde la raíz del proyecto:
    python -m unittest discover -s pruebas -v
"""
import os
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from validaciones import validar_dni, validar_texto, validar_tramite, validar_fecha
from expedientes import (
    generar_codigo, nombre_tramite, ordenar_por_codigo,
    registrar_expediente, contar_por_tramite,
)
from archivos import cargar_archivo, guardar_archivo


def listas():
    return [], [], [], [], [], [], []


class TestValidaciones(unittest.TestCase):
    def test_dni_valido(self):
        self.assertTrue(validar_dni("12345678"))

    def test_dni_invalido(self):
        for dni in ("1234abcd", "1234567", "123456789", "", "1234 678"):
            self.assertFalse(validar_dni(dni), dni)

    def test_texto(self):
        self.assertTrue(validar_texto("Ana Perez"))
        self.assertFalse(validar_texto("   "))
        self.assertFalse(validar_texto("Ana|Perez"))

    def test_tramite(self):
        self.assertTrue(validar_tramite(4))
        self.assertFalse(validar_tramite(0))
        self.assertFalse(validar_tramite(5))

    def test_fecha_valida(self):
        self.assertTrue(validar_fecha("13/11/2026"))
        self.assertTrue(validar_fecha("29/02/2024"))  # bisiesto

    def test_fecha_invalida(self):
        for f in ("13/11/2026ss", "31/02/2026", "29/02/2025", "1/1/2026",
                  "2026-11-13", "", "aa/bb/cccc", "13/13/2026"):
            self.assertFalse(validar_fecha(f), f)

    def test_fecha_futura(self):
        self.assertFalse(validar_fecha("01/01/2999"))


class TestExpedientes(unittest.TestCase):
    def test_generar_codigo(self):
        self.assertEqual(generar_codigo([]), 1)
        self.assertEqual(generar_codigo([3, 1, 7]), 8)

    def test_nombre_tramite(self):
        self.assertEqual(nombre_tramite(1), "Constancia de matricula")
        self.assertEqual(nombre_tramite(9), "Desconocido")

    def test_ordenar(self):
        cod = [5, 2, 9, 1]
        dni_a = ["a", "b", "c", "d"]
        otros = [list("wxyz") for _ in range(4)]
        tram = [1, 2, 3, 4]
        ordenar_por_codigo(cod, dni_a, otros[0], otros[1], otros[2], tram, otros[3], 4)
        self.assertEqual(cod, [1, 2, 5, 9])
        self.assertEqual(dni_a, ["d", "b", "a", "c"])  # filas siguen a su código
        self.assertEqual(tram, [4, 2, 1, 3])

    def test_resumen(self):
        self.assertEqual(contar_por_tramite([1, 1, 2, 4]), [2, 1, 0, 1])

    def test_registrar_con_reintentos(self):
        entradas = iter([
            "1234abcd", "12345678",   # DNI apoderado: 1.º inválido
            "",  "luis soto",         # nombre: 1.º vacío
            "87654321", "ana soto",
            "9", "2",                 # trámite: 1.º fuera de rango
            "31/02/2026", "13/11/2026",  # fecha: 1.º inválida
        ])
        l = listas()
        with patch("builtins.input", lambda _: next(entradas)):
            n = registrar_expediente(*l, 0)
        self.assertEqual(n, 1)
        self.assertEqual(l[0], [1])
        self.assertEqual(l[2], ["LUIS SOTO"])
        self.assertEqual(l[5], [2])
        self.assertEqual(l[6], ["13/11/2026"])

    def test_limite_100(self):
        l = listas()
        self.assertEqual(registrar_expediente(*l, 100), 100)


class TestArchivos(unittest.TestCase):
    def test_guardar_y_cargar(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = os.path.join(d, "datos", "exp.txt")
            guardar_archivo(ruta, [1, 2], ["11111111", "22222222"], ["A", "B"],
                            ["33333333", "44444444"], ["C", "D"], [1, 4],
                            ["01/11/2026", "02/11/2026"], 2)
            cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n = cargar_archivo(ruta)
        self.assertEqual(n, 2)
        self.assertEqual(cod, [1, 2])
        self.assertEqual(tram, [1, 4])
        self.assertEqual(fec[1], "02/11/2026")

    def test_archivo_inexistente(self):
        *_, n = cargar_archivo("no_existe/xyz.txt")
        self.assertEqual(n, 0)

    def test_lineas_corruptas(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = os.path.join(d, "exp.txt")
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("1|11111111|A|22222222|B|1|01/11/2026\n")
                f.write("linea rota\n")
                f.write("x|11111111|A|22222222|B|1|01/11/2026\n")
                f.write("3|11111111|A|22222222|B|9|01/11/2026\n")
            *_, n = cargar_archivo(ruta)
        self.assertEqual(n, 1)


if __name__ == "__main__":
    unittest.main()
