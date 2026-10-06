# Datos de las generales del 23-J 2023 por circunscripción

Fichero: `data/resultados_2023_provincias.json` · Comprobación: `data/check_dhondt.py`

## De dónde salen los datos

El acceso directo a `infoelectoral.interior.gob.es`, a Wikipedia (es/en) y a las hemerotecas de resultados (El País, RTVE, Europa Press, epdata…) está bloqueado por la política de salida de red de esta sesión, así que hubo que ir por otro camino:

1. **Votos por provincia (fuente principal)**: `data.json` del repositorio público [josemam/MiCongreso](https://github.com/josemam/MiCongreso) (descargado de `raw.githubusercontent.com`). El autor lo construye a partir del fichero oficial de descarga del Ministerio del Interior (`02202307`, área de descargas de infoelectoral). Contiene, para las 52 circunscripciones, los votos de **todas** las candidaturas, los votos en blanco, los nulos y el censo. Son los resultados **definitivos** (incluyen CERA), no los provisionales de la noche electoral.
2. **Escaños por circunscripción**: reparto del Real Decreto 400/2023 de convocatoria (37 Madrid, 32 Barcelona, 16 Valencia, 12 Alicante y Sevilla, 11 Málaga, 10 Murcia, 9 Cádiz, 8 A Coruña/Baleares/Bizkaia/Las Palmas, 7 Asturias/Granada/Pontevedra/S.C. Tenerife/Zaragoza, 6 Almería/Córdoba/Girona/Gipuzkoa/Tarragona/Toledo, 5 Badajoz/Cantabria/Castellón/Ciudad Real/Huelva/Jaén/Navarra/Valladolid, 4 Albacete/Álava/Burgos/Cáceres/La Rioja/León/Lleida/Lugo/Ourense/Salamanca, 3 Ávila/Cuenca/Guadalajara/Huesca/Palencia/Segovia/Teruel/Zamora, 2 Soria, 1 Ceuta y Melilla = 350). Badajoz bajó de 6 a 5 respecto a 2019 y Valencia subió de 15 a 16.
3. **Contraste**: página de Wikipedia en inglés *Results breakdown of the 2023 Spanish general election (Congress)* (la única accesible, por caché). Coinciden al voto:
   - Tabla de Madrid: PP 1.463.183, PSOE 1.004.599, Sumar 557.780, Vox 506.164, blancos 28.960, válidos 3.608.673.
   - Totales nacionales: PP 8.160.837, PSOE 7.821.718, Vox 3.057.000, Sumar 3.044.996, ERC 466.020, Junts 395.429, EH Bildu 335.129, PNV 277.289, BNG 153.995, CCa 116.363, UPN 52.188, CUP 99.644, blancos 200.673, válidos 24.688.087, nulos 264.360. La suma de las 52 provincias del JSON da exactamente esas cifras.

## Normalización de candidaturas

| En el fichero oficial | En el JSON |
|---|---|
| PP, PSOE (incluye PSC/PSdeG), VOX, SUMAR (incluye Comuns) | PP, PSOE, VOX, SUMAR |
| ERC | ERC |
| JxCAT - JUNTS | JUNTS |
| EH Bildu | BILDU |
| EAJ-PNV | PNV |
| B.N.G. | BNG |
| CCa | CC |
| U.P.N. | UPN |
| CUP-PR | CUP |
| Resto (PACMA, FO, NC-bc, PDeCAT, UPL, Existe, PCTE, GBAI, Adelante Andalucía…) | OTROS (suma) |

Cada circunscripción lleva `escanos`, `censo`, `candidaturas`, `blancos`, `nulos` y `validos` (= candidaturas + blancos, que es la base de la barrera del 3 %). Solo aparecen los partidos con votos en esa provincia.

## Resultado del check D'Hondt

`python3 data/check_dhondt.py` aplica D'Hondt con barrera del 3 % de válidos en cada circunscripción (OTROS no compite) y compara con el Congreso real:

| Partido | D'Hondt sobre el JSON | Real 2023 |
|---|---|---|
| PP | 137 | 137 |
| PSOE | 121 | 121 |
| VOX | 33 | 33 |
| SUMAR | 31 | 31 |
| ERC | 7 | 7 |
| JUNTS | 7 | 7 |
| BILDU | 6 | 6 |
| PNV | 5 | 5 |
| BNG | 1 | 1 |
| CC | 1 | 1 |
| UPN | 1 | 1 |

**Cuadra al 100 %, y no solo el total nacional: el reparto provincia a provincia reproduce el real** (Madrid 16/10/6/5, Barcelona PSC 13 / Sumar 5 / PP 5 / ERC 4 / Junts 3 / Vox 2, Bizkaia PNV 2 / PSE 2 / Bildu 2 / PP 1 / Sumar 1, Gipuzkoa Bildu 2 / PSE 2 / PNV 2, Álava 1/1/1/1, Navarra PSN 2 / Bildu 1 / PP 1 / UPN 1, S.C. Tenerife CC 1, etc.). No hubo que corregir ningún dato.

## Avisos para el simulador

- La barrera del 3 % se calcula sobre válidos (candidaturas + blancos), que es lo que hace la LOREG. En 2023 no cambió ningún escaño, pero conviene mantenerlo así.
- Para las de noviembre de 2026 el reparto de escaños por provincia lo fija el decreto de convocatoria según el padrón; Madrid y Valencia pueden volver a ganar escaño. Hasta que salga el decreto, usar el reparto de 2023.
- Si se quiere refrescar desde la fuente primaria cuando haya red, el fichero oficial es `https://infoelectoral.interior.gob.es/estaticos/docxl/apliextr/02202307_TOTA.zip` (registros `07`/`08` = datos y candidaturas de ámbito provincial).
