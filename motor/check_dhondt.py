#!/usr/bin/env python3
"""Aplica D'Hondt (barrera 3 % sobre votos válidos por circunscripción) al JSON de
resultados 2023 y compara con los escaños reales del Congreso (23-J 2023)."""
import json, os, sys
from collections import Counter

REAL = {'PP': 137, 'PSOE': 121, 'VOX': 33, 'SUMAR': 31, 'ERC': 7, 'JUNTS': 7,
        'BILDU': 6, 'PNV': 5, 'BNG': 1, 'CC': 1, 'UPN': 1}
BARRERA = 0.03

def dhondt(votos, escanos, validos, barrera=BARRERA):
    """votos: {partido: n}. Excluye OTROS (no es una candidatura real) y a quien
    no alcance la barrera sobre votos válidos (candidaturas + blancos)."""
    elegibles = {p: v for p, v in votos.items() if p != 'OTROS' and v >= barrera * validos}
    asig = Counter()
    for _ in range(escanos):
        p = max(elegibles, key=lambda p: (elegibles[p] / (asig[p] + 1), elegibles[p]))
        asig[p] += 1
    return asig

def main(path=None):
    path = path or os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/resultados_2023_provincias.json')
    data = json.load(open(path, encoding='utf-8'))
    total = Counter()
    print(f"{'Circunscripción':26s} {'esc':>3s}  reparto D'Hondt")
    for c in data['circunscripciones']:
        asig = dhondt(c['votos'], c.get('escanos_2023', c['escanos']), c['validos'])
        total.update(asig)
        print(f"{c['nombre']:26s} {c['escanos']:3d}  " + ', '.join(f'{p} {n}' for p, n in asig.most_common()))
    print('\nTotal escaños repartidos:', sum(total.values()))
    ok = True
    print(f"\n{'Partido':8s} {'D-Hondt':>8s} {'Real':>5s}  diff")
    for p in sorted(set(REAL) | set(total), key=lambda p: -REAL.get(p, 0)):
        d = total.get(p, 0) - REAL.get(p, 0)
        ok &= d == 0
        print(f"{p:8s} {total.get(p,0):8d} {REAL.get(p,0):5d}  {d:+d}" + ('' if d == 0 else '  <-- NO CUADRA'))
    print('\nRESULTADO:', 'TODO CUADRA' if ok else 'HAY DIFERENCIAS')
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
