# Mesa de Partes Digital – I.E. 2032

Prototipo en Python para registrar, consultar, ordenar y guardar expedientes
de una mesa de partes escolar. Curso: Fundamentos de Programación (CIIN1205P).

## Estructura
| Archivo | Responsabilidad |
|---|---|
| `main.py` | Menú principal |
| `validaciones.py` | DNI, texto, trámite y fecha (`datetime.strptime`) |
| `expedientes.py` | Registrar, consultar, ordenar (burbuja), listar, resumen |
| `archivos.py` | Cargar y guardar en `datos/expedientes.txt` (formato `a|b|c`) |
| `pruebas/` | Pruebas automáticas con `unittest` |

## Ejecutar
```
python main.py
python -m unittest discover -s pruebas -v
```

## Formato del archivo
`codigo|dni_apoderado|apoderado|dni_estudiante|estudiante|tramite|fecha`

Los textos no pueden contener `|`.

## Integrantes
- Marco Antonio Calongos Lopez — Desarrollo del prototipo y control de versiones (Git/GitHub)
- Justin César Alfonso Gómez Porras — Levantamiento de requerimientos y análisis del proceso
- Maribel Huillca Huallpa — Diseño de algoritmos, documentación e informe técnico
- Mia Kassandra Manrique Dextre — Validación, pruebas con datos reales y presentación (PPT)
- Adriano Félix Zamudio Poma — Persistencia de datos, revisión de código y soporte en pruebas
