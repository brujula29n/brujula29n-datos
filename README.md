# Brújula 29N · datos y fuentes

Datos, fuentes y motor de cálculo de **[brujula29n.com](https://brujula29n.com)**, el observatorio ciudadano e independiente de las elecciones generales del 29 de noviembre de 2026.

Este repositorio existe para que cualquiera pueda **comprobar cada cifra** de la web y **proponer correcciones**. Se actualiza solo cada vez que cambia la web (dos veces al día durante la campaña).

## Qué hay

| Carpeta | Contenido |
|---|---|
| `data/` | Lo que muestra la web, en JSON legible: encuestas (`encuestas.json`), partidos, problemas, programas, escenarios, países (`semaforo.json`), diario, calendario y resultados de 2023 por provincia |
| `data/historico/` | Una foto por día de la media de encuestas y la proyección, para seguir la evolución |
| `fuentes/` | La investigación de base: cada hecho con fecha, enlace y nivel de evidencia |
| `motor/` | El reparto D'Hondt y el Monte Carlo en Python (`engine.py`) y la comprobación contra los escaños reales de 2023 (`check_dhondt.py`) |

## Niveles de evidencia

- **A**: sentencia judicial, dato oficial (INE, BOE, Banco de España, Interior…) u organismo independiente.
- **B**: lo publican de forma coincidente varios medios.
- **C**: acusación de un rival, versión de un solo medio o lectura propia. Siempre marcado como tal.

Método completo: [brujula29n.com/metodologia](https://brujula29n.com/metodologia/).

## Reproducir los escaños

```
python3 motor/check_dhondt.py   # D'Hondt sobre los votos de 2023 → debe dar los 350 escaños reales
```

## Corregir un dato

Abre una [incidencia](../../issues/new/choose) con el dato, dónde aparece y **la fuente que lo corrige** (mejor nivel A). Si se confirma, se cambia y queda anotado en el diario de la web.

## Licencia

La elaboración propia (medias, proyecciones, fichas, lecturas y textos): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es). Código de `motor/`: MIT. Los datos y textos de terceros (encuestas, estadísticas oficiales, noticias) son de sus autores y se citan con su fuente; si usas uno, cita la fuente original (está en cada registro).

Aviso legal y privacidad: [brujula29n.com/legal](https://brujula29n.com/legal/).
