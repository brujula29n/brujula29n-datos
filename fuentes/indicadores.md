# Semáforo de deriva institucional — Base de datos de indicadores

**Fecha de cierre de la investigación:** 5 de octubre de 2026
**Países:** España (ESP), Venezuela (VEN), México (MEX), Colombia (COL), Cuba (CUB)
**Objetivo:** alimentar el módulo "Semáforo de deriva institucional" (se convertirá en JSON para gráficas).

## Leyenda de nivel de evidencia

- **A** = índice internacional o dato oficial (V-Dem, WJP, Freedom House, TI, RSF, EIU, FMI, Banco Mundial, INE, Banco de España, Comisión Europea, Consejo de Europa, BOE, Congreso).
- **B** = reportado por prensa de calidad o agencias (EFE/Europa Press vía Infobae, El País, El Mundo, Reuters, El Tiempo, CNN, France 24, etc.) o por ONG con metodología pública (Foro Penal, Prisoners Defenders, Hay Derecho, CEMOP).
- **C** = opinión, estimación o interpretación (incluida la mía al construir la tabla de señales).

Convención: "ed. 2026" = edición publicada en 2026 (suele medir el año 2025). Cuando el dato de una edición no se ha podido obtener, se dice explícitamente "NO DISPONIBLE / no obtenido".

---

## 1. V-Dem — Liberal Democracy Index (LDI) y Electoral Democracy Index (EDI)

Fuente de la serie: V-Dem Dataset v16 (publicado marzo 2026, mide hasta 2025) procesado por Our World in Data. Escala 0–1. **Nivel A.**
- Serie LDI: https://ourworldindata.org/grapher/liberal-democracy-index (descarga CSV filtrada por país/año)
- Serie EDI: https://ourworldindata.org/grapher/electoral-democracy-index
- Informe anual: V-Dem Democracy Report 2026 "Unraveling the Democratic Era?" (10ª ed.): https://www.v-dem.net/documents/75/V-Dem_Institute_Democracy_Report_2026_lowres.pdf
- Informe 2025: https://www.v-dem.net/documents/60/V-dem-dr__2025_lowres.pdf

### 1.1 LDI (0–1) — serie histórica (v16)

| País | 1995 | 2000 | 2010 | 2015 | 2018 | 2020 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| España | 0,818 | 0,817 | 0,825 | 0,759 | 0,776 | 0,786 | 0,743 | **0,741** |
| Venezuela | 0,604 | 0,310 | 0,154 | 0,103 | 0,061 | 0,056 | 0,046 | **0,042** |
| México | 0,281 | 0,481 | 0,465 | 0,433 | 0,452 | 0,406 | 0,246 | **0,221** |
| Colombia | 0,428 | 0,426 | 0,498 | 0,551 | 0,533 | 0,496 | 0,554 | **0,555** |
| Cuba | 0,037 | 0,040 | 0,050 | 0,057 | 0,061 | 0,060 | 0,056 | **0,057** |

Lecturas útiles para el semáforo (nivel C, interpretación mía sobre datos A):
- España pierde ~0,08 puntos entre 2010 (0,825) y 2025 (0,741): el máximo de la serie es 2010 y el mínimo reciente 2024–2025. Sigue en el grupo de "democracia liberal" pero en la zona baja de Europa occidental.
- Venezuela cae de 0,604 (1995) a 0,310 (2000, primer año de Chávez tras la Constituyente) y a 0,154 (2010): la mitad del deterioro se produjo en los **primeros dos años** de Chávez; el resto fue gradual hasta 2017.
- México: caída de 0,406 (2020) a 0,221 (2025), es decir, casi la mitad del índice en cinco años; el salto más brusco es 2024→2025 (reforma judicial).
- Colombia es estable (0,50–0,55) y mejoró respecto a 2000.

### 1.2 EDI / Polyarchy (0–1)

| País | 1995 | 2000 | 2010 | 2015 | 2020 | 2025 |
|---|---|---|---|---|---|---|
| España | 0,892 | 0,893 | 0,892 | 0,856 | 0,874 | **0,822** |
| Venezuela | 0,748 | 0,573 | 0,419 | 0,300 | 0,206 | **0,181** |
| México | 0,491 | 0,671 | 0,662 | 0,643 | 0,664 | **0,469** |
| Colombia | 0,560 | 0,550 | 0,624 | 0,681 | 0,643 | **0,679** |
| Cuba | 0,108 | 0,113 | 0,167 | 0,168 | 0,178 | **0,176** |

### 1.3 Clasificación de régimen (Regimes of the World, datos 2025, Democracy Report 2026, Tabla 1 pp. 14–15) — Nivel A

| País | Régimen 2025 | Episodio |
|---|---|---|
| España | **Democracia liberal (LD)** | Sin episodio de transformación de régimen. Única mención: pertenece a la región "Europa occidental y Norteamérica", que "registra el descenso más notable" en 2025, pero "España no muestra autocratización activa". |
| Venezuela | Autocracia electoral (EA) | Sin episodio activo (ya consumado). |
| México | **Autocracia electoral (EA+)**, zona gris "límite superior" | En **autocratización desde 2019** (gobierno de López Obrador); 5º entre los 10 mayores "autocratizadores autónomos" con un cambio de **–0,207 en LDI** desde el inicio del episodio (Tabla 4, p. 23). El informe lo describe como "un caso raro de autocratización impulsada por la izquierda en la tercera ola" y cita la reforma para elegir jueces por voto popular como politización de los tribunales. En el Democracy Report 2025 aún figuraba como "ED–" (democracia electoral en zona gris). |
| Colombia | Democracia electoral (ED) | Sin episodio. |
| Cuba | Autocracia cerrada (CA) | Sin episodio. |

Cifras globales del Democracy Report 2026 (p. 4): 92 autocracias y 87 democracias a finales de 2025; 44 países en autocratización; 74 % de la población mundial (6.000 millones) vive en autocracias; sólo 7 % en democracias liberales. Reparto: 31 LD, 56 ED, 57 EA, 35 CA.

Rankings LDI de ediciones previas (CRS R46016 citando Democracy Report 2025, sobre 179 países) — Nivel A: Venezuela 168, México 108, Colombia 52, Cuba 160. (Rango de España en 2025/2026: no obtenido; el informe no publica tabla de rangos.) https://www.everycrsreport.com/files/2025-04-25_R46016_de5c43f4ed8a51a5bceba76bf34ebb2d476113be.html

---

## 2. World Justice Project — Rule of Law Index

Escala 0–1. Edición 2025 publicada el 28-10-2025, 143 países. **Nivel A.**
- Informe global 2025: https://worldjusticeproject.org/rule-of-law-index/downloads/WJPIndex2025.pdf
- Nota de prensa 2025: https://worldjusticeproject.org/news/wjp-rule-law-index-2025-global-press-release
- Perfiles país 2025 (PDF): España https://worldjusticeproject.org/sites/default/files/documents/Spain_3.pdf · México https://worldjusticeproject.org/sites/default/files/documents/Mexico_3.pdf · Venezuela https://worldjusticeproject.org/sites/default/files/documents/Venezuela,%20RB.pdf
- Informe global 2024 (142 países): https://worldjusticeproject.org/rule-of-law-index/downloads/WJPIndex2024.pdf · Colombia 2024 https://worldjusticeproject.org/sites/default/files/documents/Colombia_2.pdf

Contexto global 2025: el 68 % de los países empeoró (57 % el año anterior); caídas concentradas en independencia judicial, libertades cívicas y rendición de cuentas. Top: Dinamarca, Noruega, Finlandia, Suecia, Nueva Zelanda. Cola: Venezuela (143), Afganistán, Camboya, Haití, Nicaragua.

### 2.1 Puntuación global y ranking

| País | 2024 score | 2024 rank /142 | 2025 score | 2025 rank /143 | Variación 2024→25 |
|---|---|---|---|---|---|
| España | 0,71 | 25 | **0,71** | **25** | –0,6 % |
| México | 0,41 | 118 | **0,40** | **121** | –2,8 % |
| Colombia | 0,48 | 91 | **0,47** | **95** | –1,8 % |
| Venezuela | 0,26 | 142 (último) | **0,26** | **143 (último)** | –0,4 % |
| Cuba | **No incluida en el índice WJP** (no hay datos) | — | — | — | — |

España ed. 2025: 18/31 en su región (UE+AELC+Norteamérica) y 25/51 entre países de renta alta; el perfil cita "descensos en independencia judicial y libertades cívicas".

### 2.2 Subfactores — rankings globales ed. 2025 (Nivel A)

| Factor | España /143 | México /143 | Venezuela /143 | Colombia (ed. 2024, /142) |
|---|---|---|---|---|
| F1 Limitaciones al poder del Gobierno | 27 | 108 | 143 | 82 |
| F2 Ausencia de corrupción | 23 | 134 | 136 | 100 |
| F3 Gobierno abierto | 23 | 54 | 141 | 35 |
| F4 Derechos fundamentales | 20 | 95 | 137 | 83 |
| F5 Orden y seguridad | 39 | 132 | 129 | 130 |
| F6 Cumplimiento regulatorio | 29 | 113 | 143 | 62 |
| F7 Justicia civil | 30 | 134 | 143 | 99 |
| F8 Justicia penal | 25 | 135 | 143 | 114 |

### 2.3 Subfactores — puntuaciones (0–1) ed. 2024 (Nivel A; de WJPIndex2024.pdf)

| Factor | España | México | Colombia | Venezuela |
|---|---|---|---|---|
| F1 Limitaciones al poder del Gobierno | 0,70 | 0,43 | 0,50 | 0,18 |
| F2 Ausencia de corrupción | 0,73 | 0,27 | 0,39 | 0,26 |
| F3 Gobierno abierto | 0,69 | 0,57 | 0,62 | 0,27 |
| F4 Derechos fundamentales | 0,78 | 0,47 | 0,51 | 0,29 |
| F5 Orden y seguridad | 0,82 | 0,52 | 0,53 | 0,53 |
| F6–F8 | no obtenido | no obtenido | no obtenido | no obtenido |

**NO DISPONIBLE:** puntuaciones numéricas por factor de la ed. 2025 (WJP las ha trasladado a su web interactiva, que no pudo leerse) y serie histórica de puntuaciones globales 2015/2020 (no obtenida; el PDF 2025 no la incluye). Los rankings por factor 2025 sí están arriba.

---

## 3. Freedom House — Freedom in the World

Escala 0–100 (derechos políticos /40 + libertades civiles /60). Ed. 2026 publicada en 2026 y mide 2025. **Nivel A.**
- Informe global ed. 2026 "The Growing Shadow of Autocracy": https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy
- Perfiles 2026: España https://freedomhouse.org/country/spain/freedom-world/2026 · Venezuela https://freedomhouse.org/country/venezuela/freedom-world/2026 · México https://freedomhouse.org/country/mexico/freedom-world/2026 · Colombia https://freedomhouse.org/country/colombia/freedom-world/2026 · Cuba https://freedomhouse.org/country/cuba/freedom-world/2026
- Serie histórica (OWID a partir de FH; el "año" de OWID es el año medido, no la edición): https://ourworldindata.org/grapher/freedom-score-fh

### 3.1 Ed. 2026 (mide 2025)

| País | Total /100 | Derechos políticos /40 | Libertades civiles /60 | Estatus |
|---|---|---|---|---|
| España | **91** | 37 | 54 | Libre |
| Venezuela | **13** | 0 | 13 | No libre |
| México | **58** | 26 | 32 | Parcialmente libre |
| Colombia | **69** | 31 | 38 | Libre |
| Cuba | **9** | 0 | 9 | No libre |

Notas de los perfiles 2026:
- España: "sistema parlamentario con elecciones multipartidistas competitivas y transferencias pacíficas de poder"; señala "legislación restrictiva adoptada o aplicada en años recientes" (expresión/reunión) y la tensión territorial catalana.
- Venezuela: "las instituciones democráticas se deterioran desde 1999"; elecciones de mayo y julio de 2025 "sin competencia genuina"; ~902 presos políticos al cierre; despliegue militar de EE. UU. desde agosto 2025.
- México: indicador de independencia judicial baja de 2 a 1 puntos por la elección popular de 881 jueces "marcada por preocupaciones de interferencia del partido gobernante Morena" y por el nuevo Tribunal de Disciplina Judicial "con poderes excesivamente amplios".
- Colombia: baja de 70 a 69; "protección frente a la fuerza ilegítima" pasa de 2 a 1 por el repunte de secuestros y asesinatos, "incluido el asesinato de un líder de la oposición" (Miguel Uribe Turbay).
- Cuba: "Estado comunista de partido único que proscribe el pluralismo político, prohíbe los medios independientes y reprime la disidencia".

### 3.2 Serie histórica (año medido; OWID/FH) — Nivel A

| País | 2005 | 2010 | 2015 | 2020 | 2024 (ed. 2025) | 2025 (ed. 2026) |
|---|---|---|---|---|---|---|
| España | 95 | 97 | 95 | 90 | 90 | 91 |
| Venezuela | 54 | 42 | 35 | 14 | 13 | 13 |
| México | 80 | 66 | 65 | 61 | 59 | 58 |
| Colombia | 60 | 61 | 63 | 65 | 70 | 69 |
| Cuba | 8 | 10 | 15 | 13 | 10 | 9 |

Lectura (C): España bajó 7 puntos entre 2010 (97) y 2020 (90) y se ha estabilizado en 90–91. Venezuela perdió 12 puntos entre 2005 y 2010 (Chávez consolidado) y 28 entre 2010 y 2020. México pierde 22 puntos en 20 años, de forma continua.

---

## 4. Transparencia Internacional — Índice de Percepción de la Corrupción (CPI)

Escala 0–100 (100 = muy limpio). Ed. 2025 publicada febrero 2026, 182 países; media mundial 42; 122 países por debajo de 50. **Nivel A.**
- Resultados y análisis: https://www.transparency.org/en/news/cpi-2025-findings-insights-corruption
- Informe PDF: https://files.transparencycdn.org/images/CPI-2025-Report-EN.pdf
- Tabla completa con series (TI Alemania): https://www.transparency.de/fileadmin/Redaktion/Aktuelles/2026/CPI_2025/Tabelle_-_Kopie.pdf
- Nota regional Américas: https://www.transparency.org/en/press/corruption-perceptions-index-2025-corruption-across-americas-damaging-peoples-lives-is-fuelling-violence
- España baja 3 puestos (prensa, B): https://thediplomatinspain.com/en/2026/02/10/spains-ranking-in-the-global-corruption-perceptions-index-worsens-by-three-places/

| País | CPI 2016 | CPI 2021 | CPI 2024 | **CPI 2025** | **Rank 2025 /182** |
|---|---|---|---|---|---|
| España | 58 | 61 | 56 | **55** | **49** (46 en 2024) |
| Venezuela | 17 | 14 | 10 | **10** | **180** |
| México | 30 | 31 | 26 | **27** | **141** |
| Colombia | 37 | 39 | 39 | **37** | **99** |
| Cuba | 47 | 46 | 41 | **40** | **84** |

Comentario TI 2025: Venezuela descrita como "autocracia plena" con corrupción "sistémica a todos los niveles"; México citado entre los países "particularmente peligrosos para periodistas que cubren corrupción". España: pierde 6 puntos desde 2021 (61→55), su peor puntuación de la serie reciente. (Cuba puntúa mejor que México y Colombia; TI advierte que el CPI mide percepción de expertos/empresas y no captura bien autocracias cerradas; nivel C.)

---

## 5. Reporteros Sin Fronteras — Clasificación Mundial de la Libertad de Prensa

Escala 0–100, 180 países. Ed. 2026 publicada mayo 2026. **Nivel A.**
- Índice: https://rsf.org/en/index · Ranking: https://rsf.org/en/ranking · Américas 2026: https://rsf.org/en/classement/2026/americas
- Análisis global 2026 ("mínimo en 25 años"): https://rsf.org/en/2026-rsf-index-press-freedom-25-year-low
- Ficha España: https://rsf.org/en/country/spain

| País | 2025 rank | 2025 score | **2026 rank** | **2026 score** |
|---|---|---|---|---|
| España | 23 | 77,35 | **29** | **75,42** |
| Colombia | no obtenido | no obtenido | **102** | **51,66** |
| México | no obtenido | no obtenido | **122** | **45,23** |
| Venezuela | no obtenido | no obtenido | **159** | **30,48** |
| Cuba | no obtenido | no obtenido | **160** | **29,22** |

Hallazgos 2026: por primera vez más de la mitad de los países están en situación "difícil" o "muy grave"; la media global es la más baja desde 2002; el indicador legal es el que más cae (>60 % de Estados). Américas: –14 puntos desde 2022. Venezuela: garantías "profundamente inciertas" pese a liberar periodistas en 2026; Cuba: "crisis profunda", periodistas independientes trabajan en la clandestinidad; Colombia aparece entre los que mejoran.

España (ficha RSF 2026): baja 6 puestos (23→29). Causas citadas: polarización ("parte de los medios sustituye la información por la opinión"), EMFA no aplicada, SLAPPs y presión judicial, "ley mordaza" sin derogar, precariedad y concentración del mercado, ciberacoso y agresiones (sobre todo a periodistas mujeres) vinculados a la extrema derecha.

---

## 6. Economist Intelligence Unit — Democracy Index

Escala 0–10. Ed. 2025 publicada 7-4-2026 **sin tabla completa** (36 páginas resumidas); los valores país 2025 proceden de la tabla "by country" de Wikipedia (que reproduce el dataset) y de prensa. **Nivel A para 2024 y anteriores; B para 2025.**
- Nota de prensa EIU 2025: https://www.prnewswire.com/news-releases/eiu-democracy-index-2025-democracy-stabilises-after-eight-years-of-decline-302734863.html
- Informe 2024 (PDF): https://d1qqtien6gys07.cloudfront.net/wp-content/uploads/2025/03/Democracy_INDEX_2024.pdf
- Tabla histórica: https://en.wikipedia.org/wiki/The_Economist_Democracy_Index
- España 2025 (puesto 22): https://agendapublica.es/noticia/20922/fin-recesion-democratica-mundial
- Colombia 2025 (–13 puestos): https://www.asuntoslegales.com.co/consultorio/colombia-registro-la-caida-mas-pronunciada-de-toda-latinoamerica-en-el-democracy-index-2025-4383462
- España 2024 (puesto 21, 8,13): https://theobjective.com/internacional/2025-02-27/the-economist-espana-democracia-plena/

Global 2025: media 5,19 (5,17 en 2024); 26 democracias plenas, 48 imperfectas, 32 híbridos, 61 autoritarios. Francia vuelve a "plena".

| País | 2006 | 2010 | 2015 | 2020 | 2022 | 2023 | 2024 (rank) | **2025 (rank)** | Categoría 2025 |
|---|---|---|---|---|---|---|---|---|---|
| España | 8,34 | 8,16 | 8,30 | 8,12 | 8,07 | 8,07 | 8,13 (21) | **8,20 (22)** | Democracia plena |
| Venezuela | 5,42 | 5,18 | 5,00 | 2,76 | 2,23 | 2,31 | 2,25 (142) | **2,13** | Autoritario |
| México | 6,67 | 6,93 | 6,55 | 6,07 | 5,25 | 5,14 | 5,32 (84) | **5,40** | Régimen híbrido |
| Colombia | 6,40 | 6,55 | 6,62 | 7,04 | 6,72 | 6,55 | 6,35 (60) | **6,04 (73)** | Democracia imperfecta (al borde de híbrido) |
| Cuba | 3,52 | 3,52 | 3,52 | 2,84 | 2,65 | 2,65 | 2,58 (135) | **2,58** | Autoritario |

Componentes 2024 (A): España — proceso electoral 9,58 / funcionamiento del Gobierno 7,50 / participación 7,22 / cultura política 7,50 / libertades civiles 8,82. México — 6,92 / 5,00 / 7,22 / 1,88 / 5,59. Venezuela — 0,00 / 1,07 / 5,00 / 3,13 / 2,06. Colombia — 9,17 / 5,71 / 6,11 / 3,13 / 7,65. Cuba — 0,00 / 2,86 / 3,33 / 3,75 / 2,94.

Colombia 2025 (B): la mayor caída de Latinoamérica; motivos citados: asesinato del candidato Miguel Uribe Turbay, 26 políticos asesinados y 35 atentados en 2025, 187 líderes sociales asesinados, 525 agresiones a la prensa, 76 masacres, y choques del Ejecutivo con Corte Constitucional, Congreso, Banco de la República y Consejo Nacional Electoral.

---

## 7. Economía

Fuentes principales: FMI WEO abril 2026 vía API DataMapper (https://www.imf.org/external/datamapper/api/v1/{indicador}/{país}), Banco Mundial API, Banco de España, INE, SHCP (México), MinHacienda/CARF (Colombia), ONEI/CEEC (Cuba). Cuba **no está en el FMI** y el Banco Mundial no publica PIB per cápita PPA ni inflación de Cuba (todos los valores nulos 2000–2024: https://api.worldbank.org/v2/country/CUB/indicator/NY.GDP.PCAP.PP.CD?format=json&date=2000:2024 ).

### 7.1 Deuda pública bruta (% PIB)

España (Banco de España, PDE; Nivel A): 2024 = **101,8 %** (–3,3 pp; media euro 87,4 %) https://www.bde.es/wbe/en/publicaciones/analisis-economico-investigacion/boletin-economico/2025t3-articulo-04-la-evolucion-de-la-deuda-publica-en-espanaen-2024.html · 2025 = **100,7 %** (nota 31-3-2026) https://www.bde.es/wbe/en/noticias-eventos/actualidad-banco-espana/notas-banco-espana/deuda-aapp-2025t4.html · Plan fiscal-estructural: objetivo 90,6 % en 2031 (B) https://www.infobae.com/tag/sostenibilidad-presupuestaria
Serie Banco Mundial para España, deuda del **gobierno central** (GC.DOD.TOTL.GD.ZS; no comparable con la PDE, Nivel A): 2007 31,7 · 2010 49,9 · 2012 77,4 · 2014 104,9 · 2018 107,2 · 2019 111,3 · 2020 139,0 · 2021 132,5 · 2022 109,0 · 2023 107,4 · 2024 105,6. https://api.worldbank.org/v2/country/ESP/indicator/GC.DOD.TOTL.GD.ZS?format=json&date=2000:2024
Orden de magnitud PDE conocido (C, de memoria y coherente con BdE): 2018 ≈ 100 %, 2019 ≈ 98 %, 2020 ≈ 120 %, 2021 ≈ 116 %, 2022 ≈ 110 %, 2023 ≈ 105 %. **Verificar con la serie PDE del BdE antes de graficar.**

FMI WEO abril 2026 (GGXWDG_NGDP; Nivel A):

| País | 2000 | 2010 | 2015 | 2018 | 2020 | 2022 | 2024 | 2025 | 2026p | 2027p |
|---|---|---|---|---|---|---|---|---|---|---|
| México | 38,5 | 40,2 | 51,0 | 52,2 | 58,5 | 53,8 | 59,1 | 61,8 | 62,7 | 63,1 |
| Colombia | 38,0 | 36,5 | 50,4 | 51,8 | 65,3 | 61,3 | 61,0 | 59,9 | 60,9 | 61,3 |
| España | no obtenido vía API (usar BdE arriba) | | | | | | | | | |
| Venezuela | **sin datos en WEO** | | | | | | | | | |

México (SHCP, B): SHRFSP 2024 = 52,0 % PIB; 2025 = **52,6 %** (objetivo 51,4 %); RFSP 2024 = 5,8 %; 2025 = **4,3 %** (objetivo 3,9 %). https://www.bloomberglinea.com/latinoamerica/mexico/mexico-cierra-2025-con-deficit-fiscal-y-deuda-publica-mas-altos-de-lo-estimado-por-hacienda/
Colombia (B, MinHacienda vía Valora Analitik 4-3-2026): deuda GNC cierre 2025 = **64,7 % PIB**, la más alta desde 2001 salvo pandemia. https://www.valoraanalitik.com/confirmado-deficit-fiscal-de-colombia-en-2025-llego-a-64-del-pib-el-segundo-mas-alto-del-siglo-sin-contar-la-pandemia/ · CARF (1-10-2026): deuda neta 2026 60,2 %, 2027 67,4 %; sin medidas podría llegar a 91,2 % en 2030. https://www.infobae.com/colombia/2026/10/01/carf-proyecta-que-el-deficit-fiscal-de-colombia-sera-de-78-del-pib-en-2026-y-95-en-2027/

### 7.2 Déficit público (% PIB; negativo = déficit)

España (IGAE/Hacienda, Nivel A vía prensa B): 2024 = –2,86 % (–2,9 %); 2025 = **–2,18 %** (36.780 M€; –2,39 % incluyendo DANA), objetivo –2,5 %; "el más bajo desde 2008". https://www.pressdigital.es/articulo/economia/2026-03-31/5828883-deficit-publico-cierra-2025-218-pib-36780-millones-mejora-objetivo-gobierno
FMI WEO abr-2026 (GGXCNL_NGDP; A): España 2000 –0,6 · 2005 –2,7 · 2010 –4,1 · 2015 –2,5 · 2018 –1,0 · 2019 –2,0 · 2020 –9,0 · 2021 –5,4 · 2022 –3,6 · 2023 –4,0 · 2024 –4,4 · 2025 –5,3 · 2026 –5,1. **OJO:** estas cifras del FMI para España no cuadran con las de IGAE (–2,2 % en 2025); es probable que la extracción automática haya devuelto otra serie. Usar IGAE/Eurostat para España; marcar la serie FMI como "pendiente de verificación".
Colombia (FMI, A): 2000 –2,9 · 2010 –3,3 · 2015 –3,5 · 2018 –4,7 · 2020 –7,1 · 2021 –7,3 · 2022 –6,4 · 2023 –2,9 · 2024 –6,0 · 2025 –5,7 · 2026 –5,2. Dato oficial GNC (B): 2024 **–6,7 %**, 2025 **–6,4 %**; CARF proyecta **–7,8 % en 2026 y –9,5 % en 2027** (Gobierno: –7,2 % y –9,4 %); cláusula de escape de la regla fiscal vigente hasta 2027.
México: ver SHCP arriba (–5,8 % 2024, –4,3 % 2025). FMI no obtenido vía API.
Venezuela: sin datos fiables (FMI no publica).
Cuba: no hay dato fiable.

### 7.3 Inflación (IPC medio anual, %)

FMI WEO abr-2026 (PCPIPCH; A) y otras:

| País | 2000 | 2010 | 2015 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026p |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| España (FMI) | 3,4 | 1,8 | –0,5 | 1,7 | 0,7 | –0,3 | 3,0 | 8,5 | 3,1 | 2,4 | **2,8** | 2,5 |
| España (INE, IPC medio) | | | | | | | | | | 2,8 | **2,7** | — |
| México | 9,5 | 4,2 | 2,7 | 4,9 | 3,6 | 3,5 | 4,7 | 7,9 | 4,7 | 2,6 | **3,1** | 3,0 |
| Colombia | 9,2 | 2,3 | 5,0 | 3,2 | 3,5 | 2,5 | 3,5 | 10,2 | 11,7 | 6,6 | **5,1** | 5,9 |

España INE 2025 = 2,7 % media anual: https://www.elplural.com/economia/ine-confirma-inflacion-cerro-2025-media-27_378694102 (B sobre INE A).

Venezuela: Banco Mundial (A) sólo hasta 2016: 2010 28,2 · 2013 40,6 · 2014 62,2 · 2015 121,7 · 2016 255,0. https://api.worldbank.org/v2/country/VEN/indicator/FP.CPI.TOTL.ZG?format=json&date=1998:2024 · FMI vía prensa (B): WEO oct-2025 proyectaba 2025 = 269,9 % y 2026 = 682,1 % https://www.bloomberglinea.com/latinoamerica/venezuela/fmi-proyecta-inflacion-de-682-en-venezuela-en-2026-ademas-de-contraccion-en-su-economia/ ; WEO abr-2026 revisa a 2025 = **252 %**, 2026 = **387,4 %**, 2027 = 94,4 % https://es-us.noticias.yahoo.com/fmi-venezuela-crecer%C3%A1-4-2026-140000391.html · Inflación interanual ene-2025 = 78,8 % (CEDICE/OVF, B) https://cedice.org.ve/ogp/reporte/venezuela-en-cifras-enero-2025/ · **NO DISPONIBLE:** serie FMI 2017–2024 (hiperinflación 2017–2020) por fallo de la API; el FMI advierte que sus estimaciones para Venezuela "deben interpretarse con cautela" al no tener diálogo con las autoridades desde 2018.

Cuba (ONEI, mercado formal; B): 2025 interanual **14,07 %** https://oncubanews.com/cuba/economia/cuba-cierra-2025-con-una-inflacion-interanual-del-1407-en-el-mercado-formal/ ; agosto 2026 interanual **25,19 %** (alimentos +36 %) https://www.infobae.com/cuba/2026/09/17/crisis-economica-en-cuba-la-inflacion-alcanzo-el-25-y-comenzaron-a-circular-billetes-de-hasta-20000-pesos/ ; estimaciones independientes ≈70 % en bienes básicos (CEEC reconoce "estimaciones no oficiales más elevadas"). Tipo de cambio informal: **700 CUP/USD** (17-9-2026) frente a 24/120 oficial; circulan billetes de 20.000 pesos.

### 7.4 Paro (% población activa)

FMI WEO abr-2026 (LUR; A):

| País | 2000 | 2007 | 2010 | 2013 | 2015 | 2018 | 2019 | 2020 | 2022 | 2024 | 2025 | 2026p |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| España | 13,9 | 8,2 | 19,9 | 26,1 | 22,1 | 15,3 | 14,1 | 15,5 | 13,0 | 11,3 | **10,5** | 9,8 |
| México | 2,2 | 3,7 | 5,3 | 4,9 | 4,3 | 3,3 | 3,5 | 4,4 | 3,3 | 2,7 | **2,6** | 2,7 |
| Colombia | 13,3 | 11,2 | 11,2 | 8,6 | 8,8 | 10,0 | 9,9 | 13,9 | 10,3 | 9,1 | **8,0** | 9,0 |
| Venezuela | **sin datos en WEO** | | | | | | | | | | | |
| Cuba | sin dato fiable (ONEI publica ~1–2 %, no comparable) | | | | | | | | | | | |

España INE/EPA (A): 4T2024 = 10,45 %; **4T2025 = 9,93 %** (2.477.100 parados; 22.463.300 ocupados; +605.400 ocupados interanual) https://www.ine.es/dyngs/Prensa/EPA4T25.htm ; **2T2026 = 9,87 %** https://www.ine.es/dyngs/Prensa/EPA2T26.htm (B: https://www.eldiariodemadrid.es/articulo/empresas/epa-segundo-trimestre-2026-paro-987-creacion-empleo-desaceleracion/20260731132436138746.html ).

### 7.5 PIB per cápita PPA (dólares internacionales corrientes; FMI WEO abr-2026, PPPPC; A)

| País | 2000 | 2010 | 2015 | 2018 | 2020 | 2022 | 2024 | 2025 | 2026p |
|---|---|---|---|---|---|---|---|---|---|
| España | 21.190 | 29.888 | 31.979 | 34.272 | 32.158 | 37.205 | 39.412 | **41.182** | 42.967 |
| Venezuela | 11.598 | 13.957 | 12.372 | 11.202 | 5.877 | 5.577 | 5.572 | **5.636** | 5.597 |
| México | 9.006 | 10.047 | 10.534 | 10.118 | 9.254 | 10.045 | 10.365 | **10.611** | 10.843 |
| Colombia | 6.681 | 10.834 | 14.075 | 15.481 | 15.588 | 20.154 | 21.499 | **22.543** | 23.576 |
| Cuba | **sin dato** (FMI no cubre; BM nulo) | | | | | | | | |

**Advertencia (C):** la serie PPPPC de México parece anómala (apenas cambia en 25 años; el BM/OCDE sitúan a México ≈ 22.000–25.000 $ PPA en 2024). Posible error de extracción. Verificar antes de graficar; la de Venezuela (–60 % desde 2013) y Colombia son coherentes con otras fuentes.

Lectura (C): Venezuela perdió más de la mitad de su PIB per cápita PPA entre 2013 (13.503) y 2020 (5.877) y no se ha recuperado. España multiplica por ~2 desde 2000.

### 7.6 Crecimiento real del PIB (%)

España (FMI abr-2026, A): 2000 5,0 · 2010 0,0 · 2013 –1,7 · 2015 3,6 · 2018 2,4 · 2019 2,1 · 2020 –11,3 · 2021 5,5 · 2022 5,8 · 2023 2,5 · 2024 2,7 · 2025 2,2(?) · 2026 2,1. **OJO:** el INE (avance 30-1-2026) da **2025 = 2,8 %** y **2024 = 3,2 %** (Reuters/Investing, B): https://www.investing.com/news/economic-indicators/spains-economy-far-outgrows-peers-with-28-expansion-in-2025-4475268 — la serie FMI extraída para 2024–2025 parece desactualizada o mal leída; usar INE para 2024–2025.
Colombia (FMI, A): 2013 5,1 · 2015 3,0 · 2018 2,6 · 2019 3,2 · 2020 –7,2 · 2021 10,8 · 2022 7,3 · 2023 0,8 · 2024 1,5 · 2025 2,6 · 2026 2,3.
México (Banco Mundial, A): 2000 5,0 · 2009 –6,3 · 2010 5,0 · 2015 2,7 · 2018 2,0 · 2019 –0,4 · 2020 –8,4 · 2021 6,0 · 2022 3,7 · 2023 3,1 · 2024 1,4. https://api.worldbank.org/v2/country/MEX/indicator/NY.GDP.MKTP.KD.ZG?format=json&date=2000:2024
Venezuela (Banco Mundial, A): 1998 0,5 · 1999 –5,9 · 2002 –8,7 · 2003 –7,8 · 2004 18,2 · 2008 5,2 · 2010 –1,6 · 2013 1,3 · 2014 –3,9 · 2015 –6,2 · 2016 –17,1 · 2017 –15,7 · 2018 –19,6 · 2019 –27,6 · 2020 –29,8 · 2021 0,6 · 2022 8,1 · 2023 4,0 · 2024 5,5. https://api.worldbank.org/v2/country/VEN/indicator/NY.GDP.MKTP.KD.ZG?format=json&date=1998:2024 — Contracción acumulada 2014–2020 ≈ **–75 %** (C, calculado). FMI (B): 2025 +0,5 % (oct-2025) / 2026 +4,0 % y 2027 +6,0 % (abr-2026, tras el cambio de régimen).
Cuba (B): PIB 2025 ≈ **–5 %** según el CEEC (Universidad de La Habana), tercer año consecutivo de caída, **–15 % acumulado desde 2020**; generación eléctrica –13,7 %; pérdida de 1,5 millones de habitantes en cinco años https://www.infobae.com/america/america-latina/2026/02/10/crisis-en-cuba-la-economia-se-hundio-un-5-en-2025-y-acumula-una-caida-del-15-desde-2020/ · Otra cifra (CEPAL/ONEI vía Infobae 17-9-2026): 2025 –3,8 %, previsión 2026 –10,3 %. Las dos cifras de 2025 no coinciden: usar rango "–3,8 % a –5 %".

### 7.7 Tipo de cambio y reservas

- Venezuela (CEDICE "Venezuela en cifras", ene-2025; B): reservas internacionales BCV **10.330 M USD**; tipo oficial 57,97 Bs/USD (depreciación mensual 12 %), paralelo 68,34 (brecha ~22 %); producción petrolera dic-2024 998 kb/d (PDVSA) / 886 kb/d (fuentes secundarias); riesgo país EMBI 205 pb. https://cedice.org.ve/ogp/reporte/venezuela-en-cifras-enero-2025/ · Para contexto histórico: control de cambios desde 2003 (CADIVI) hasta 2018 (B, cronología Wikipedia abajo). **NO DISPONIBLE:** reservas 2025–2026 actualizadas.
- Cuba: ver 7.3 (700 CUP/USD informal, sep-2026).
- España/México/Colombia: euro / peso flotante; no procede.

### 7.8 España 2018–2026, resumen para la gráfica (fuentes arriba)

| Año | PIB real % | Paro % (media FMI / EPA 4T) | IPC medio % | Deuda PDE % PIB | Déficit % PIB |
|---|---|---|---|---|---|
| 2018 | 2,4 | 15,3 | 1,7 | ≈100 (verificar) | –1,0 (FMI) / –2,5 (IGAE, C) |
| 2019 | 2,1 | 14,1 | 0,7 | ≈98 (verificar) | –2,0 / –3,1 (C) |
| 2020 | –11,3 | 15,5 | –0,3 | ≈120 (verificar) | –9,0 / –10,1 (C) |
| 2021 | 5,5 | 14,9 | 3,0 | ≈116 (verificar) | –5,4 / –6,7 (C) |
| 2022 | 5,8 | 13,0 | 8,5 | ≈110 (verificar) | –3,6 / –4,6 (C) |
| 2023 | 2,5 | 12,2 | 3,1 | 105,1 (BdE: 101,8+3,3) | –4,0 / –3,5 (C) |
| 2024 | 3,2 (INE) | 11,3 / 10,45 | 2,8 | **101,8** | **–2,9** (IGAE, –3,2 con DANA) |
| 2025 | 2,8 (INE) | 10,5 / 9,93 | 2,7 | **100,7** | **–2,2** (–2,4 con DANA) |
| 2026 | 2,1p | 9,8p / 9,87 (2T) | 2,5p | 90,6 % objetivo 2031 | — |

Las celdas marcadas (C)/(verificar) son valores de memoria coherentes con series oficiales pero **no** verificados en esta sesión; sustituir por la serie PDE del Banco de España e IGAE antes de publicar.

---

## 8. Independencia judicial en España

### 8.1 EU Justice Scoreboard (Comisión Europea) y Eurobarómetro — Nivel A

- Cuadro 2026 (publicado 4-6-2026): https://commission.europa.eu/document/download/d1367f58-9eed-4ebd-8eb3-68646b7c7ddc_en?filename=2026_eu_justice_scoreboard.PDF · Nota Representación en España: https://spain.representation.ec.europa.eu/noticias-eventos/noticias-0/el-cuadro-de-indicadores-de-la-justicia-de-2026-destaca-la-importancia-de-contar-con-sistemas-2026-06-04_es
- Eurobarómetro Flash sobre independencia percibida: https://europa.eu/eurobarometer/surveys/detail/3193 (ed. 2024; las de 2025/2026 siguen la misma serie)

Percepción ciudadana de la independencia judicial "bastante buena" o "muy buena" (según el Informe sobre el Estado de Derecho 2026, que cita el Eurobarómetro; A):

| Año | Ciudadanos | Empresas | Clasificación Comisión |
|---|---|---|---|
| 2022 | 38 % | 41 % | media (40–59 %) / baja (<40 %) |
| 2025 | 39 % | 40 % | baja (ciudadanos) / media (empresas) |
| 2026 | **40 %** | **46 %** | media / media |

Desglose Eurobarómetro 2024 (B sobre A; Diario Constitucional 4-7-2025): muy buena 6 %, bastante buena 33 %, bastante mala 32 %, muy mala 20 %, NS 9 %; **razón principal: "interferencias o presiones de gobiernos y actores políticos" 42 %**, intereses económicos 40 %, garantías insuficientes del estatuto judicial 30 %. España, 7ª peor de la UE ese año. https://www.diarioconstitucional.cl/2025/07/04/espana-entre-los-paises-de-la-ue-con-menor-confianza-ciudadana-y-empresarial-en-la-independencia-judicial/
Cuadro 2026 (B sobre A; infoLibre 21-6-2026, Agenda Pública): España **22ª de 27** en percepción ciudadana de independencia (sólo Chipre, Eslovaquia, Hungría, Croacia y Bulgaria peor); 40 % buena / 35 % mala; 19ª en percepción empresarial; 4ª por la cola en tiempos de resolución; 3ª por la cola en pendencia; de las ratios de jueces/100.000 hab. más bajas (sólo Malta, Dinamarca, Irlanda por debajo); 9º gasto en justicia/PIB; líder en digitalización. https://www.infolibre.es/politica/espanoles-colocan-jueces-cola-europa-independencia-influencia-politicos_1_2208997.html · https://agendapublica.es/noticia/21152/justicia-espanola-europa-tecnologia-puntera-sentencias-tardias

### 8.2 Consejo General del Poder Judicial (CGPJ) — Nivel A/B

- Mandato caducado el **4-12-2018**; renovación el **25-7-2024**: **5 años y 7 meses (~2.043 días)** de bloqueo. Reforma de 2021 (LO 4/2021) que impidió al Consejo en funciones hacer nombramientos discrecionales → más del 25–30 % de plazas del Supremo vacantes hacia 2023. Reforma 2022 para permitir sólo el nombramiento de los magistrados del TC. https://es.wikipedia.org/wiki/Bloqueo_del_Consejo_General_del_Poder_Judicial · https://maldita.es/malditateexplica/20240625/renovacion-cgpj-claves-gobierno-psoe-pp/
- Tras la renovación: 196 nombramientos de altos cargos judiciales "la mayoría con amplio consenso" (Informe Estado de Derecho 2026). Febrero 2025: el CGPJ propone dos modelos de elección de vocales (por jueces o por Parlamento). **Comisión de Venecia (oct-2025):** el primer modelo se ajusta al estándar de elección por pares pero con "riesgo de politización interna"; el segundo "no se ajustaría" al estándar del Consejo de Europa. Reforma no aprobada al disolverse las Cortes (oct-2026).
- Recomendación europea repetida por **tercer año consecutivo** (Hay Derecho).

### 8.3 Fiscal General del Estado — Nivel A/B

- Álvaro García Ortiz: nombrado 2-8-2022; el Supremo abre causa el **16-10-2024** (primera imputación de un FGE en ejercicio) por revelación de secretos (filtración de correos del novio de la presidenta Ayuso, marzo 2024); juicio 3–13 nov 2025; **condena 20-11-2025**: 2 años de inhabilitación, multa 7.300 €, 10.000 € de indemnización; dimite 24-11-2025; recurso al TC pendiente (Fiscalía y el propio exfiscal). https://en.wikipedia.org/wiki/%C3%81lvaro_Garc%C3%ADa_Ortiz
- Sucesora: **Teresa Peramato**, propuesta 25-11-2025, informe unánime del CGPJ, toma de posesión 11-12-2025 ante el mismo tribunal que condenó a su antecesor. https://www.infobae.com/espana/agencias/2025/12/11/teresa-peramato-toma-posesion-como-nueva-fiscal-general-ante-el-tribunal-que-condeno-a-garcia-ortiz/
- Reforma del estatuto (anteproyecto 30-10-2025): mandato de 5 años no renovable desligado del Gobierno; informe del CGPJ previo al cese; traspaso de la instrucción a los fiscales (nueva LECrim). **No aprobada** al disolverse las Cortes.
- GRECO insiste en cambiar el sistema de elección del FGE: "sigue generando preocupación pública" (B): https://www.iustel.com/diario_del_derecho/noticia.asp?ref_iustel=1254316

### 8.4 Informes sobre el Estado de Derecho de la Comisión Europea (capítulo España) — Nivel A

**2024 (24-7-2024)** https://commission.europa.eu/document/download/2bd09a6f-ef56-494a-8303-e0de808ee981_en?filename=23_1_58063_coun_chap_spain_en_0.pdf · resumen: https://commission.europa.eu/document/download/606e97d6-718c-4589-b7e6-8708c6132be8_en?filename=6.2_1_58128_count_chap_abstracts_and_recomm_en.pdf
Avances significativos en renovación del CGPJ; algún avance en estatuto del FGE; sin avances en lobbies, conflictos de intereses y acceso a la información. Señala la Ley de Amnistía (mayo 2024) como "controvertida".

**2025 (8-7-2025)** https://www.swissinfo.ch/spa/claves-del-cap%C3%ADtulo-dedicado-a-espa%C3%B1a-en-el-informe-2025-sobre-el-estado-de-derecho-en-ue/89650572 (B sobre A)
40 % de las empresas dicen que la corrupción les impidió ganar licitaciones en 3 años (casi el doble que el año anterior); estrategia anticorrupción prevista para 2024 no iniciada; amnistía avalada por el TC y aplicada ya a >300 personas; FGE "en proceso judicial"; independencia judicial percibida "baja" entre ciudadanos.

**2026 (17-7-2026, SWD(2026) 909)** https://commission.europa.eu/document/download/82ce1391-cde5-49e9-9d1b-3f14f4975eb7_es?filename=13_2_coun_chap_spain_es.pdf
Cumplimiento de las recomendaciones 2025 → recomendaciones 2026:
1. Elección de vocales del CGPJ: **avances significativos** → seguir con estándares europeos y Comisión de Venecia.
2. Estatuto del FGE: **avances significativos** → "disociación en el tiempo de su mandato con el del Gobierno".
3. Duración de causas de corrupción de alto nivel: **algunos avances** → reforma LECrim.
4. Conflictos de intereses / patrimonio de altos cargos: **sin avances**.
5. Lobbies: **algunos avances** → registro público obligatorio (115 enmiendas; plazo de enmiendas prorrogado **21 veces**; sólo 75 diputados notificaron reuniones en 2025, 46 en 2024).
6. Acceso a la información: **sin avances** → aprobar Ley de Información Clasificada (sustituye la Ley 9/1968 de secretos oficiales, aún vigente) y Ley de Administración Abierta.
Otros: Autoridad Independiente de Protección del Informante con 14 de 23 plazas cubiertas y seis CC. AA. sin autoridad; contratación pública vulnerable; RTVE con "riesgo medio-alto" (MPM 2026), informe de los Consejos de Informativos de TVE/RNE (ene-2026) denunciando "deterioro de las normas deontológicas" y "sesgo político"; el TC y otras instituciones alertan de que "declaraciones contra jueces concretos contribuyen a erosionar la confianza pública".
Crítica de Hay Derecho (B): "anuncios que nunca llegan a ejecutarse"; Ley de Información Clasificada con 36 prórrogas del plazo de enmiendas; Plan Estatal Anticorrupción "sin ejecutar en ninguno de sus puntos"; 92 % de los españoles percibe corrupción generalizada (media UE 71 %). https://www.hayderecho.com/portfolio-item/hay-derecho-informe-estado-derecho-comision-europea-2026/

### 8.5 GRECO (Consejo de Europa) — Nivel A

Informes publicados 16-4-2025: https://www.coe.int/es/web/portal/-/greco-publishes-two-reports-assessing-spain-s-progress-in-implementing-its-anti-corruption-recommendations
- 5ª ronda (altos cargos del Ejecutivo y fuerzas de seguridad), informe dic-2023: **0 recomendaciones cumplidas, 13 parcialmente, 6 no cumplidas** de 19 → procedimiento de incumplimiento. https://www.antifrau.cat/en/greco-avisa-Espana-no-cumple-ninguna-19-recomendaciones-prevencion-corrupcion
- 4ª ronda (parlamentarios, jueces y fiscales), junio 2024: 7 cumplidas, 3 parciales, 1 no cumplida; la no cumplida es **el sistema de elección del CGPJ**; parcial: autonomía/transparencia del Ministerio Fiscal.
- Gobierno (1-8-2025) defiende cumplimiento "total o parcial" de la mayoría: https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/presidencia-justicia-relaciones-cortes/paginas/2025/010825-informe-greco-avance.aspx

---

## 9. Señales tempranas: literatura y cronologías comparadas

### 9.1 Marco teórico — Nivel A (obras citadas) / C (síntesis)

- **Levitsky & Ziblatt, "Cómo mueren las democracias" (2018):** cuatro indicadores de comportamiento autoritario: (1) rechazo (o débil compromiso) de las reglas democráticas; (2) negación de la legitimidad de los adversarios; (3) tolerancia o fomento de la violencia; (4) disposición a recortar libertades civiles, incluida la prensa. Mecánica: "capturar a los árbitros" (jueces, fiscales, agencias, órganos electorales), "comprar o neutralizar a los jugadores" (medios, empresarios, oposición) y "reescribir las reglas" (Constitución, ley electoral). Insisten en que la muerte ocurre "lentamente, en pasos apenas visibles" y en la erosión de dos normas no escritas: tolerancia mutua y contención institucional (forbearance). https://www.consilium.europa.eu/en/documents-publications/library/library-blog/posts/how-democracies-die-what-history-reveals-about-our-future/
- **Bermeo, "On Democratic Backsliding" (Journal of Democracy, 2016):** tres vías contemporáneas: golpes "promisorios", **engrandecimiento del Ejecutivo** ("cambios institucionales legitimados por medios legales: nuevas constituyentes, referendos, tribunales o legislaturas existentes", que pueden presentarse como mandato democrático) y manipulación estratégica de elecciones (bloqueo de medios, inhabilitaciones, supresión de voto, de forma incremental). https://en.wikipedia.org/wiki/Democratic_backsliding
- **V-Dem (Lührmann & Lindberg, "third wave of autocratization", 2019; Democracy Reports 2021–2026):** la autocratización actual es gradual y legalista; **secuencia típica: primero libertad de expresión/medios y sociedad civil, después elecciones y controles judiciales/legislativos.** Democracy Report 2026 (44 países en autocratización en 2025): censura gubernamental de medios empeora en 44; libertad académica/cultural 41; autocensura 39; represión de OSC 39; control de entrada/salida de OSC 37; acoso a periodistas 34; autonomía del órgano electoral 28; calidad electoral 22; límites legislativos al Ejecutivo 21. Democracy Report 2025 (2014–2024): censura 44, represión OSC 41, elecciones libres 33, deliberación 27, Estado de derecho 18, límites judiciales 11.

### 9.2 Cronologías de referencia

**Venezuela 1998–2017** (B: https://es.wikipedia.org/wiki/Crisis_institucional_de_Venezuela ; https://www.vozdeamerica.com/a/venezuela-historia-cronologia-chavez-maduro-/3964896.html ; LDI de V-Dem A):
- 1998: Chávez gana con discurso contra "la partidocracia" (LDI 1995 = 0,60).
- 1999: Asamblea Constituyente convocada por referéndum; nueva Constitución; relegitimación de todos los poderes. LDI 2000 = 0,31.
- 2000–2001: leyes habilitantes (49 decretos-ley en 2001) → protestas empresariales.
- 2002: golpe fallido (abril) y paro petrolero; despido de ~18.000 trabajadores de PDVSA.
- 2003: control de cambios (CADIVI) y controles de precios.
- 2004: referéndum revocatorio; "lista Tascón" (represalias a firmantes); **ampliación del TSJ de 20 a 32 magistrados** por ley orgánica, nombrados por mayoría simple.
- 2007: no renovación de la licencia de RCTV (mayo); referéndum constitucional perdido (dic.).
- 2009: referéndum de enmienda → reelección indefinida.
- 2010: nueva ley habilitante tras perder la mayoría cualificada en legislativas.
- 2013: muerte de Chávez; Maduro gana por 1,5 puntos. LDI 2015 = 0,10.
- Dic-2015: la oposición gana 2/3 de la Asamblea Nacional; el Parlamento saliente nombra **13 magistrados "exprés"**.
- 2016: el TSJ declara a la AN "en desacato" y anula sus leyes; se bloquea el revocatorio.
- Mar-2017: sentencias 155 y 156 del TSJ asumen competencias legislativas ("autogolpe"); jul-2017: Asamblea Nacional Constituyente paralela con poderes plenipotenciarios; destitución de la fiscal general Luisa Ortega. LDI 2018 = 0,06.
- 2018: elecciones presidenciales adelantadas sin oposición reconocida; emigración masiva; hiperinflación.
- Epílogo 2024–2026 (B: https://en.wikipedia.org/wiki/2025_in_Venezuela ; https://en.wikipedia.org/wiki/2026_in_Venezuela ): elección jul-2024 sin actas; 10-1-2025 Maduro jura tercer mandato; parlamentarias 25-5-2025 (participación 42,66 %); Nobel de la Paz a M.ª Corina Machado (10-10-2025); despliegue naval de EE. UU. (ago-2025), bloqueo petrolero (16-12-2025); **3-1-2026: ataque estadounidense y captura de Maduro**; 5-1-2026 Delcy Rodríguez presidenta encargada; ley de amnistía (20-2-2026); EE. UU. reconoce al Gobierno (7-3-2026) y reabre embajada (14-3-2026). Presos políticos (Foro Penal, B): **344** a 14-9-2026 (144 militares), 324 tras excarcelaciones de finales de septiembre; ~902 según Freedom House a cierre de 2025. https://www.abc.com.py/internacionales/2026/09/18/la-ong-foro-penal-contabiliza-en-venezuela-344-presos-politicos-32-de-ellos-extranjeros/

**México 2018–2026** (B/A):
- 2018: AMLO gana con 53 %; Morena mayoría en ambas cámaras. V-Dem fecha el inicio de la autocratización en **2019**.
- 2019–2023: Guardia Nacional de mando militar; militarización de aduanas, puertos, obras (Tren Maya, aeropuerto); ataques verbales diarios al INE y a la Suprema Corte; "Plan B" electoral (2023) anulado por la SCJN.
- 5-2-2024: "Plan C" de 20 reformas constitucionales.
- 2-6-2024: Sheinbaum gana (≈60 %); Morena obtiene mayoría cualificada en Diputados y casi en Senado.
- **Reforma judicial:** Diputados 4-9-2024 (357–130), Senado 11-9-2024 (86–41), 17 de 32 congresos estatales en 24 h, promulgada 15-9-2024. Elección popular de todos los jueces federales, SCJN de 11 a 9 ministros, Tribunal de Disciplina Judicial, "jueces sin rostro". Críticas de CIDH, relatora ONU, HRW, embajador de EE. UU. https://en.wikipedia.org/wiki/2024_Mexican_judicial_reform
- Sep-2024: Guardia Nacional pasa a la SEDENA (reforma constitucional, DOF). Oct-2024: reforma de "supremacía constitucional" (inimpugnabilidad de reformas). **21/28-11-2024: eliminación de siete órganos autónomos** (INAI, Cofece, IFT, Coneval, CRE, CNH, Mejoredu), Senado 86–42. https://cnnespanol.cnn.com/2024/11/29/senado-mexico-aprueba-reforma-eliminacion-siete-organos-autonomos-orix
- **1-6-2025: elección judicial**, 881 cargos; **participación 13,02 %**; >20 % de votos nulos; "acordeones" distribuidos por operadores de Morena; TEPJF rechaza anular 3–2 (ago-2025); Hugo Aguilar preside la SCJN; ministras afines reelegidas. https://en.wikipedia.org/wiki/2025_Mexican_judicial_elections
- 2026: reforma electoral de Sheinbaum (INE, plurinominales, –25 % financiación a partidos) **rechazada en Diputados el 11-3-2026** (259–234, sin los 334 necesarios) porque PT y PVEM votaron en contra; PT la calificó de "regreso del partido de Estado". https://www.elfinanciero.com.mx/nacional/2026/03/11/reforma-electoral-va-rumbo-a-la-guillotina-sin-apoyo-del-verde-y-pt-sigue-la-sesion-en-vivo/ · Segunda reforma judicial (may-2026): aplaza la elección judicial a 2028 y crea una "Comisión Coordinadora" de los tres poderes que filtra candidatos; críticas de que "centraliza aún más el control político de Morena". https://www.infobae.com/mexico/2026/05/21/reforma-judicial-de-sheinbaum-es-mucho-peor-de-lo-anunciado-centraliza-el-control-sobre-la-eleccion-de-jueces/
- Resultado en índices: LDI 0,406 (2020) → 0,221 (2025); FH 61 → 58; EIU 6,07 → 5,40 (híbrido); WJP 118 → 121.

**Colombia 2022–2026** (B):
- Ago-2022: Petro, primer presidente de izquierda; coalición amplia que se rompe en 2023.
- 2023–2024: investigación del CNE por violación de topes de campaña 2022 (más de 5.000 M COP no declarados); Petro la califica de "inicio de un golpe de Estado" (oct-2024) y lo denuncia ante el cuerpo diplomático; choques con el fiscal Barbosa, la Corte Suprema (elección de fiscal), el Banco de la República (tipos) y la Procuraduría. https://www.elespanol.com/mundo/america/20241009/investigan-gustavo-petro-financiacion-ilegal-campana-habla-inicio-golpe/891911419_0.html · https://www.infobae.com/colombia/2024/10/16/gustavo-petro-denuncio-presunto-golpe-de-estado-ante-el-cuerpo-diplomatico-alianza-criminal/
- Ene-2025: estado de conmoción interior en el Catatumbo; **dic-2025: la Corte Constitucional tumba la mayoría de los decretos** (sólo mantiene los de armamento); Petro: "fue un error". https://www.infobae.com/colombia/2025/12/03/petro-ataco-a-la-corte-constitucional-tras-tumbar-decretos-clave-de-conmocion-interior-por-ola-de-violencia-en-el-catatumbo-fue-un-error/
- May-2025: el Senado rechaza la consulta popular; Petro la convoca por decreto ("decretazo", 11-6-2025); **el Consejo de Estado la suspende (18-6-2025)**; la Corte Constitucional se declara incompetente (22-7-2025). Propuesta recurrente de asamblea constituyente. https://www.eltiempo.com/justicia/cortes/urgente-consejo-de-estado-suspende-el-decretazo-del-gobierno-petro-que-convocaba-la-consulta-popular-3464645
- Jun-2025: atentado contra el senador y precandidato **Miguel Uribe Turbay** (muere en agosto); 26 políticos asesinados en 2025.
- Fiscal: déficit 2024 –6,7 %, 2025 –6,4 %; cláusula de escape de la regla fiscal; rebajas de rating; CARF prevé –7,8 % (2026) y –9,5 % (2027).
- **Elecciones 2026:** 1ª vuelta 31-5-2026: Abelardo de la Espriella 43,74 % (10,36 M), Iván Cepeda 40,90 % (9,69 M), Paloma Valencia 6,92 %, Fajardo 4,26 %; Petro: "como presidente no acepto los resultados del preconteo". **2ª vuelta 21-6-2026: De la Espriella 49,66 % (12.959.515) – Cepeda 48,70 % (12.708.695)**; Petro vuelve a no reconocer el preconteo ("no se puede proclamar a ningún presidente"); escrutinio judicial confirma; toma de posesión 7-8-2026. https://www.elespectador.com/politica/elecciones-colombia-2026/resultados-elecciones-presidenciales-colombia-2026-en-vivo-quien-gano/ · https://es-us.noticias.yahoo.com/ganando-elecciones-colombia-2026-resultados-195844193.html
- Resultado en índices: las instituciones de control **resistieron** (Consejo de Estado, Corte Constitucional, Registraduría, Congreso), pero EIU baja de 6,35 a 6,04 (puesto 73) y FH de 70 a 69 por violencia política y tensión institucional. Es el "caso de control" del semáforo: deriva verbal del Ejecutivo + frenos que funcionan.

**Cuba 2018–2026** (B/A):
- 2018–2019: traspaso Raúl Castro → Díaz-Canel; Constitución 2019 (partido único consagrado). Decreto-Ley 370 (2019) y 35 (2021) sobre internet.
- 11-7-2021: mayores protestas desde 1959; Código Penal 2022 endurece "sedición"; **217 manifestantes condenados por sedición, pena media 10 años** (Prisoners Defenders).
- 2021–2024: emigración de ~10 % de la población (HRW) / 1,5 millones en cinco años (CEEC vía Infobae); apagones nacionales (5 entre oct-2024 y sep-2025); 30 % de medicamentos esenciales disponibles; 7 de 10 cubanos se saltan comidas (HRW 2026). https://www.hrw.org/es/world-report/2026/country-chapters/cuba
- Presos políticos: HRW ~700 (oct-2025); **Prisoners Defenders 1.339 a 31-8-2026 (récord)**, 2.167 acumulados desde jul-2021, 155 mujeres, 38 detenidos siendo menores. https://www.prisonersdefenders.org/2026/09/10/cuba-alcanza-un-nuevo-record-de-1-339-presos-politicos-reclamar-agua-y-luz-lleva-a-prision-y-castiga-a-familias-enteras/
- Economía: PIB –15 % desde 2020; inflación oficial 25 % (ago-2026), dólar informal 700 CUP.
- Índices: FH 9/100, LDI 0,057, RSF 160/180, EIU 2,58. Cuba es el "suelo" de la escala: autocracia cerrada estable, cuyo deterioro es económico, no institucional (ya no hay instituciones que capturar).

### 9.3 Tabla de señales (síntesis, nivel C sobre datos A/B)

Codificación sugerida para el JSON: 0 = ausente, 1 = incipiente/puntual, 2 = establecida, 3 = consumada. Periodo evaluado: situación actual (2025–2026), con nota de cuándo se activó en los casos históricos.

| # | Señal | Venezuela (cuándo) | México (cuándo) | Colombia (cuándo) | Cuba | **España hoy** | Dato objetivo España (ver §10) |
|---|---|---|---|---|---|---|---|
| S1 | Captura de órganos de control (consejo judicial, TC, órgano electoral, fiscalía) | 3 (TSJ ampliado 2004; magistrados exprés 2015; CNE afín) | 3 (jueces electos 2025; órganos autónomos suprimidos 2024) | 1 (intentos; frenados) | 3 | **1** | CGPJ bloqueado 5 a. 7 m.; FGE condenado; TC con 4 magistrados caducados desde mar-2026; GRECO/CE piden cambiar elección del CGPJ y del FGE |
| S2 | Reforma judicial impulsada por el Ejecutivo | 3 (2004, 2015) | 3 (2024, 2026) | 0 | n/a | **1** | Reforma LECrim (fiscales instruyen) y estatuto del FGE no aprobadas; reforma CGPJ pendiente; 700 plazas nuevas |
| S3 | Ataques a la prensa / captura de medios públicos | 3 (RCTV 2007; Conatel) | 2 (acoso a periodistas; violencia criminal; "mañaneras") | 1 (ataques verbales; 525 agresiones 2025) | 3 | **1** | RSF 23→29; RTVE: consejo ampliado por decreto-ley 2024 a 15 con mayoría simple, informe de los Consejos de Informativos ene-2026, MPM riesgo medio-alto |
| S4 | Ejecutivo frente al Legislativo: gobernar por decreto, presupuestos sin aprobar, leyes bloqueadas | 3 (leyes habilitantes 2000, 2001, 2010; AN anulada 2016–17) | 1 (mayoría cualificada: no necesita decretos) | 2 ("decretazo" 2025, conmoción interior) | n/a | **2** | 60 decretos-ley y 11 derogados en la XV legislatura (récord); PGE 2023 prorrogados 3 veces; 32 leyes en 3 años (mínimo histórico); ~70 proyectos bloqueados |
| S5 | Politización de la fiscalía | 3 (fiscal destituida 2017) | 2 (FGR) | 2 (pulso por la elección de fiscal 2024) | 3 | **2** | Primer FGE imputado y condenado; mandato ligado al Gobierno (CE/GRECO lo señalan desde 2020) |
| S6 | Uso de instrumentos de perdón/excepción para aliados políticos | 3 (amnistías selectivas, ANC 2017) | 1 | 1 | n/a | **2** | Ley de Amnistía (jun-2024) pactada para la investidura; TC 6-4 (jun-2025); TJUE la avala (16-7-2026); Supremo mantiene la orden contra Puigdemont |
| S7 | Deslegitimación del adversario / de jueces y árbitros | 3 | 3 ("conservadores corruptos"; ataques al INE) | 3 ("golpe de Estado" por una investigación del CNE; no reconoce preconteos 2026) | n/a | **1–2** | Gobierno y oposición se acusan de "lawfare" y de "asalto a las instituciones"; TC alerta de declaraciones contra jueces concretos (CE 2026) |
| S8 | Gasto/deuda insostenibles, inflación, controles | 3 (control de cambios 2003; hiperinflación 2017–20; PIB –75 %) | 1 (deuda 52,6 %; déficit 4,3 %) | 2 (déficit 6,4 % → 9,5 % previsto; regla fiscal suspendida) | 3 (PIB –15 %; inflación 25 %; 700 CUP/USD) | **0–1** | Deuda 100,7 % (bajando), déficit 2,2 %, paro 9,9 %, inflación 2,7 %, crecimiento 2,8 %; pero gasto 19 % por encima de lo presupuestado en el trienio sin PGE |
| S9 | Polarización afectiva alta y persistente | 3 | 2 | 3 | n/a | **2** | CEMOP: índice 5,20 (2024) → 4,94 (2025); rechazo a Abascal 67,9 %, Feijóo 55,8 %, Sánchez 54,2 %; 70 % percibe más tensión; confianza en medios 4,1/10 |
| S10 | Manipulación/colonización de instituciones estadísticas o demoscópicas | 3 (INE/BCV dejaron de publicar) | 1 | 0 | 3 | **1** | CIS: sobreestima al bloque de izquierda en 41 de 42 elecciones desde 2018; multa de la JEC 2024; comisión de investigación en el Senado |
| S11 | Dependencia de aliados que condicionan la integridad territorial/constitucional | n/a | n/a | n/a | n/a | **2** | Investidura 179 votos con Junts, ERC, PNV, Bildu, BNG, CC; amnistía, financiación singular y condonación de deuda; Junts rompe (27-10-2025) y tumba decretos → elecciones 29-N |
| S12 | Militarización de la seguridad pública | 3 | 3 (Guardia Nacional → SEDENA 2024) | 1 | 3 | **0** | Sin señal |
| S13 | Elecciones no competitivas / órgano electoral no autónomo | 3 (2018, 2024) | 1 (INE presionado; reforma rechazada 2026) | 1 (presidente no reconoce preconteos, pero cede el poder) | 3 | **0** | Elecciones competitivas, JEC independiente, alternancias 2011/2018/2023 |

Semáforo España (C): **verde** en S8, S12, S13; **ámbar** en S1, S2, S3, S7, S10; **rojo-ámbar** en S4, S5, S6, S9, S11. Comparado con Venezuela 1999–2004 o México 2019–2024, España no presenta captura consumada de árbitros ni reformas que cambien las reglas del juego; sí presenta la **combinación de bloqueo institucional + gobierno por decreto + polarización** que la literatura identifica como fase previa, y un dato cuantitativo que acompaña: LDI 0,825 (2010) → 0,741 (2025) y CPI 61 (2021) → 55 (2025).

---

## 10. España: datos objetivos por señal

### 10.1 Decretos-ley por legislatura — Nivel B (sobre BOE/Congreso, A)

Fuente: Electomanía, 2-10-2026 https://electomania.es/radiografia-del-decreto-ley-en-espana-747-aprobados-16-rechazados-13-en-el-ultimo-gobierno/ ; Nuevaradio 19-8-2026 https://www.nuevaradio.org/2026/08/19/actividad-legislativa-minima-en-el-congreso-con-sanchez-estableciendo-record-en-la-emision-de-decretos/ ; Infobae/EP 25-7-2026 https://www.infobae.com/espana/agencias/2026/07/25/la-huella-legislativa-del-curso-politico-10-leyes-aprobadas-y-21-decretos-convalidados/

| Legislatura | Años | RDL aprobados | Derogados por el Congreso |
|---|---|---|---|
| II (González) | 1982–86 | 40 | 0 |
| III | 1986–89 | 20 | 0 |
| IV | 1989–93 | 30 | 0 |
| V | 1993–96 | 40 | 0 |
| VI (Aznar) | 1996–2000 | 85 | 0 |
| VII | 2000–04 | 42 | 0 |
| VIII (Zapatero) | 2004–08 | 52 | 1 |
| IX | 2008–11 | 56 | 0 |
| X (Rajoy) | 2011–15 | 76 | 0 |
| XI | 2016 | 1 | 0 |
| XII (Rajoy 30 + Sánchez 35) | 2016–18 | 65 | 2 |
| XIII | 2019 | 10 | 0 |
| XIV (Sánchez) | 2019–23 | 97 | 1 |
| **XV (Sánchez)** | **2023–26** | **60** | **11** |

Por presidente: González 130/0; Aznar 127/0; Zapatero 108/1; Rajoy 107/1; **Sánchez 200 aprobados / 13 rechazados** (Electomanía) — Nuevaradio da 168 aprobados y 11 derogados ("de los 14 decretos derogados en democracia, 11 son de Sánchez"). Diferencias por criterio de cómputo; usar Electomanía por ser más reciente y detallado, citando ambos. Leyes aprobadas XV legislatura: 25 el primer año (PSOE), 10 el curso 2025–26, **32 en tres años, mínimo histórico**; ~70 proyectos pendientes, 34 procedentes de decretos-ley. Los dos últimos decretos de vivienda derogados (4-10-2026) desencadenaron la convocatoria electoral.

### 10.2 Presupuestos prorrogados — Nivel B (sobre BOE, A)

- Últimos PGE aprobados: **2023** (aprobados dic-2022). Prorrogados en 2024, 2025 y 2026 (tercera prórroga en vigor desde 1-1-2026). Undécima prórroga de la democracia (precedentes: 1978, 1982, 1995, 2011, 2016, 2017, 2018×2). **Primera legislatura completa sin aprobar unos PGE.** https://www.eldiariodemadrid.es/articulo/politica/legislatura-sanchez-nuevos-presupuestos-generales-estado-pge-2023-prorrogados/20261005103413143316.html
- 1.000 días sin presupuestos nuevos (27-9-2026): https://es.euronews.com/2026/09/27/espana-cumple-1000-dias-sin-nuevos-presupuestos-es-un-hurto-a-los-ciudadanos
- Modificaciones presupuestarias >81.000 M€ hasta 31-8-2026; gasto de las AA. PP. +19 % en el trienio; gasto del Estado 14 % por encima de lo presupuestado; Seguridad Social +20 %; recaudación +24 % (misma fuente, B).

### 10.3 CGPJ — ver §8.2: bloqueo 4-12-2018 → 25-7-2024 (5 años 7 meses, ~2.043 días); reforma 2021 que vació de nombramientos al Consejo en funciones; >25 % de vacantes en el Supremo en 2023; elección de vocales aún no reformada (recomendación CE 2024, 2025 y 2026; GRECO 4ª ronda no cumplida).

### 10.4 Fiscal General — ver §8.3: primer FGE imputado (16-10-2024) y condenado (20-11-2025) en democracia; sucesora en 17 días; reforma del estatuto sin aprobar.

### 10.5 RTVE — Nivel B
- 2024: tres presidencias en un año (Elena Sánchez destituida 26-3-2024; Concepción Cascajosa interina; **José Pablo López** elegido 28-11-2024 con mandato de 6 años). Reforma por **real decreto-ley** (oct-2024) que amplía el Consejo de 10 a 15 miembros y rebaja la mayoría para elegirlo (permite mayoría absoluta en segunda votación), con sueldos fijos de 105.000–125.000 €. https://www.infolibre.es/medios/informe-2024-cnmc-desmonta-tesis-derechas-rtve-seguidismo-gobierno_1_2226238.html · https://www.eldiario.es/vertele/noticias/rtve-consejeros-consejo-administracion-2024-15-nuevos-psoe-pp-sumar-junts-erc-podemos-pnv-jose-pablo-lopez_1_11829934.html
- Ene-2026: informe de los Consejos de Informativos de TVE y RNE denunciando deterioro deontológico y sesgo; Comisión Europea (jul-2026): riesgo "medio-alto" del MPM 2026 en independencia del servicio público (A).
- Contrapunto: informe CNMC 2024 sobre tiempos de palabra (infoLibre lo usa para negar seguidismo; cifras tras muro de pago; no obtenidas).

### 10.6 CIS — Nivel B
- Desde 2018 (Tezanos): fin de la "cocina" anunciado y revertido; sobreestimó al bloque de izquierda en **41 de 42 elecciones** desde 2018; error medio en las europeas 2024 de 1,6 pp, "más del doble que el promedio de las encuestas" (predijo 42,4 % para PSOE+Sumar+Podemos; real 38,1 %); multa de la Junta Electoral (2024) por difundir encuesta en jornada de reflexión; comisión de investigación en el Senado (2024); proposición del PP admitida (may-2025) para vetar expolíticos en la dirección. https://maldita.es/malditateexplica/20250613/errores-encuestas-cis-tezanos/
- Barómetro oct-2025: recuerdo de voto PSOE 38,6 % / PP 18,9 % frente al resultado real de 2023 (31,6 % / 33 %): desviación de 22 puntos; estimación CIS PSOE 34,8 – PP 19,8 frente a Sociométrica PP 34 – PSOE 26,9 (B, El Español). https://www.elespanol.com/espana/politica/20251013/no-va-cis-tezanos-da-puntos-ventaja-sanchez-feijoo-coloca-vox-pp/1003743966815_0.html

### 10.7 Tribunal Constitucional — Nivel B
- Mayoría "progresista" 7–5 desde enero 2023 (presidente Conde-Pumpido). Sentencia de la amnistía **26-6-2025, 6 votos a 4**; ponente Montalbán; Campo se abstuvo (como ministro la había llamado "claramente inconstitucional"); el magistrado conservador Macías fue recusado a instancias de la Fiscalía. https://www.infobae.com/espana/2025/06/26/el-constitucional-avala-la-ley-de-amnistia-con-los-seis-votos-a-favor-de-la-mayoria-progresista/
- **10-3-2026:** caduca el mandato de cuatro magistrados (Conde-Pumpido, Balaguer, Enríquez, Macías); renovación corresponde al Senado (3/5); el PP tiene 145 senadores y le faltan 11 votos para hacerlo solo; estrategia de esperar a las generales; el Gobierno estudia un "conflicto de atribuciones". https://www.moncloa.com/2026/10/02/renovacion-tribunal-constitucional-bloqueo-pp-3441711 · https://www.legaltoday.com/actualidad-juridica/noticias-de-derecho/conde-pumpido-avisa-al-senado-de-que-debera-activar-la-renovacion-del-tc-ante-su-salida-y-la-de-otros-tres-magistrados-2025-08-04/
- Patrón (C): los dos grandes partidos bloquean el órgano cuando la renovación les perjudica (PP con el CGPJ 2018–24 y el TC 2026; PSOE/Podemos con el TC en 2022 hasta la reforma de la LOPJ). Es un rasgo de "juego duro constitucional" (Levitsky & Ziblatt), no de captura unilateral.

### 10.8 Ley de Amnistía — Nivel A/B
- LO 1/2024, en vigor **11-6-2024**; pactada en el acuerdo de investidura PSOE–Junts (nov-2023) para el 1-O, Tsunami Democràtic y CDR. https://en.wikipedia.org/wiki/2023_Spanish_government_formation
- Aplicada a >300 personas (CE 2025). TC la avala 26-6-2025 (6–4). TJUE, **16-7-2026**: compatible con el Derecho de la UE (terrorismo y malversación: "no menoscaba" la directiva antiterrorista ni los intereses financieros de la UE; fin legítimo de "reducir tensiones institucionales y facilitar la reconciliación"). El Supremo mantiene la orden de detención contra Puigdemont por malversación con "beneficio patrimonial personal". https://www.publico.es/politica/tribunales/sentencia-tjue-sobre-ley-amnistia-puigdemont-directo.html · Comisión de Venecia (mar-2024) y Comisión Europea la calificaron de "controvertida".

### 10.9 Acuerdos con partidos independentistas — Nivel A/B
- 23-J 2023: PP 137, PSOE 121 (350). Investidura 16-11-2023: **179–171** con Sumar, ERC, Junts, EH Bildu, PNV, BNG y abstención de CC. Contenidos: amnistía (Junts, ERC), "mecanismos para resolver el conflicto político" y mediador internacional (Junts), traspaso de Rodalies y condonación parcial de deuda autonómica (ERC), peajes AP-9/AP-53 (BNG). https://www.newtral.es/pactos-investidura-sanchez/20231111/
- Jul-2024 (PSC–ERC): "financiación singular" para Cataluña (recaudación por la Agencia catalana), origen del conflicto con las demás CC. AA. https://s1.elespanol.com/2024/07/30/actualidad/Acuerdo_PSC_ERC_Espanol.pdf
- **27-10-2025: Junts rompe con el PSOE** (incumplimientos: amnistía no aplicada a Puigdemont, catalán en la UE, competencias de inmigración); sin moción de censura. https://www.esdiario.com/nacional/251027/170761/puigdemont-sanchez-junts-rompe-psoe.html
- 4-10-2026: el Congreso deroga dos decretos-ley de vivienda (voto de Junts); **5-10-2026: Sánchez convoca elecciones para el 29-11-2026** ("doblegar a las élites"; "en el Parlamento se pisan los intereses de la gente"). https://theobjective.com/espana/politica/2026-10-05/sanchez-elecciones-decretos/ · https://www.elespanol.com/espana/politica/20261005/sanchez-convoca-elecciones-doblegar-elites-parlamento-pisan-intereses-gente/1003744408309_0.html

### 10.10 Polarización afectiva — Nivel B (encuesta con metodología publicada) / A (artículos académicos)
- **CEMOP, V Encuesta Nacional de Polarización Política (mayo–junio 2025, n=1.110):** índice agregado de polarización afectiva **5,20 (2024) → 4,94 (2025)**; rechazo: Abascal 67,9 % (quinto año como líder más polarizante), Feijóo 55,8 % (+6,9), Sánchez 54,2 % (+3,4); 70,1 % percibe más tensión que el año anterior; confianza en medios 4,1/10; 82 % percibe alta manipulación en los medios del bloque contrario. https://www.cemopmurcia.es/estudios/v-encuesta-nacional-de-polarizacion-politica-2025/ · Síntesis de cuatro años: https://www.maspoderlocal.com/index.php/mpl/article/view/270
- Literatura comparada: Reiljan (2020, EJPR, "Fear and loathing across party lines (also) in Europe") sitúa a España entre los sistemas de partidos con mayor polarización afectiva de Europa occidental, junto a los del sur; Torcal & Comellas (2022, South European Society and Politics, "Affective Polarisation in Times of Political Instability and Conflict. Spain from a Comparative Perspective") documentan un aumento sostenido 2008–2019 y nivel comparable al de EE. UU. https://onlinelibrary.wiley.com/doi/abs/10.1111/1475-6765.12351 · https://www.tandfonline.com/doi/full/10.1080/13608746.2022.2044236 · Análisis de series 1993–2023: https://revistas.ucm.es/index.php/POSO/en/article/view/96233 (no se pudieron extraer los valores numéricos de estos artículos: acceso bloqueado; nivel de evidencia de la afirmación "entre los más altos de Europa": B).

### 10.11 Corrupción percibida y casos (contexto) — Nivel A/B
- CPI 61 (2021) → 55 (2025), puesto 49. 92 % percibe corrupción generalizada (Eurobarómetro, vía Hay Derecho). 40 % de empresas: la corrupción les impidió ganar licitaciones (CE 2025). Casos Koldo/Ábalos/Cerdán (2024–2026) citados en el informe CE 2025 como "investigaciones de corrupción de alto nivel" (B).

---

## 11. Huecos y advertencias para el JSON

1. **No obtenido:** puntuaciones numéricas por factor del WJP 2025 (sólo rankings) y serie histórica WJP; LDI rank de España; RSF 2025 para LatAm; serie FMI de inflación de Venezuela 2017–2024; reservas BCV 2025–26; componentes EIU 2025; valores de Reiljan/Torcal.
2. **Verificar antes de graficar:** serie PDE de deuda de España 2018–2023 (celdas marcadas); déficit España según FMI (incoherente con IGAE; usar IGAE); PIB per cápita PPA de México (anómalo); crecimiento España 2024–2025 (usar INE 3,2 % / 2,8 %).
3. **Cuba** no tiene WJP, FMI ni PIB per cápita PPA del BM; usar sólo V-Dem, FH, CPI, RSF, EIU y las cifras ONEI/CEEC/HRW/Prisoners Defenders con nivel B.
4. **EIU 2025**: la EIU no publicó la tabla completa; los valores país proceden de reproducciones (B). Los de 2024 y anteriores son A.
5. Las cifras de decretos-ley difieren según la fuente (200 vs 168 para Sánchez): mostrar la de Electomanía por legislatura y citar la discrepancia.
6. Todo lo que aparece en la tabla de señales (§9.3) como 0–3 es **codificación mía (C)** a partir de los datos A/B anteriores; conviene mostrarla en la web como "lectura" y no como dato.

## 12. Índice de URLs (fuentes primarias)

- V-Dem DR 2026: https://www.v-dem.net/documents/75/V-Dem_Institute_Democracy_Report_2026_lowres.pdf
- V-Dem DR 2025: https://www.v-dem.net/documents/60/V-dem-dr__2025_lowres.pdf
- OWID LDI: https://ourworldindata.org/grapher/liberal-democracy-index · EDI: https://ourworldindata.org/grapher/electoral-democracy-index · FH: https://ourworldindata.org/grapher/freedom-score-fh
- WJP 2025: https://worldjusticeproject.org/rule-of-law-index/downloads/WJPIndex2025.pdf · WJP 2024: https://worldjusticeproject.org/rule-of-law-index/downloads/WJPIndex2024.pdf
- Freedom House 2026: https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy
- TI CPI 2025: https://www.transparency.org/en/news/cpi-2025-findings-insights-corruption · tabla: https://www.transparency.de/fileadmin/Redaktion/Aktuelles/2026/CPI_2025/Tabelle_-_Kopie.pdf
- RSF 2026: https://rsf.org/en/index · https://rsf.org/en/country/spain
- EIU 2025: https://www.prnewswire.com/news-releases/eiu-democracy-index-2025-democracy-stabilises-after-eight-years-of-decline-302734863.html · EIU 2024 PDF: https://d1qqtien6gys07.cloudfront.net/wp-content/uploads/2025/03/Democracy_INDEX_2024.pdf
- FMI DataMapper API: https://www.imf.org/external/datamapper/api/v1/ (indicadores GGXWDG_NGDP, GGXCNL_NGDP, PCPIPCH, LUR, PPPPC, NGDP_RPCH)
- Banco Mundial API: https://api.worldbank.org/v2/country/{ISO3}/indicator/{código}?format=json
- Banco de España deuda 2025: https://www.bde.es/wbe/en/noticias-eventos/actualidad-banco-espana/notas-banco-espana/deuda-aapp-2025t4.html
- INE EPA 4T2025: https://www.ine.es/dyngs/Prensa/EPA4T25.htm · 2T2026: https://www.ine.es/dyngs/Prensa/EPA2T26.htm · IPC: https://www.ine.es/prensa/ipc_tabla.htm
- Comisión Europea, Estado de Derecho 2026 España: https://commission.europa.eu/document/download/82ce1391-cde5-49e9-9d1b-3f14f4975eb7_es?filename=13_2_coun_chap_spain_es.pdf · 2024: https://commission.europa.eu/document/download/2bd09a6f-ef56-494a-8303-e0de808ee981_en?filename=23_1_58063_coun_chap_spain_en_0.pdf
- EU Justice Scoreboard 2026: https://commission.europa.eu/document/download/d1367f58-9eed-4ebd-8eb3-68646b7c7ddc_en?filename=2026_eu_justice_scoreboard.PDF
- GRECO España 2025: https://www.coe.int/es/web/portal/-/greco-publishes-two-reports-assessing-spain-s-progress-in-implementing-its-anti-corruption-recommendations
- HRW Cuba 2026: https://www.hrw.org/es/world-report/2026/country-chapters/cuba · Prisoners Defenders: https://www.prisonersdefenders.org/ · Foro Penal: https://foropenal.com/
