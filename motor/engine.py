#!/usr/bin/env python3
"""Motor electoral en Python, réplica del de site/app.js (D'Hondt provincial con swing proporcional
desde 2023 + Monte Carlo). Lo usa build.py para guardar el histórico diario (data/historico/) sin
necesitar un navegador. Los parámetros son los mismos que en app.js; las cifras pueden diferir en
±1-2 escaños por el azar del Monte Carlo."""
import math, random

PARTIES = ['PP', 'PSOE', 'VOX', 'SUMAR', 'PODEMOS', 'SALF', 'ERC', 'JUNTS', 'BILDU', 'PNV', 'BNG', 'CC', 'UPN']
SD = {'PP': 2.2, 'PSOE': 2.2, 'VOX': 2.0, 'SUMAR': 1.3, 'PODEMOS': 0.9, 'SALF': 0.6, 'ERC': 0.35, 'JUNTS': 0.3,
      'BILDU': 0.25, 'PNV': 0.25, 'BNG': 0.2, 'CC': 0.12, 'UPN': 0.06}
BLOQUE23 = ['PSOE', 'SUMAR', 'PODEMOS', 'ERC', 'BILDU', 'PNV', 'BNG', 'JUNTS']


def dhondt(votes, seats, validos, thr=0.03):
    elig = [(p, v) for p, v in votes.items() if p != 'OTROS' and v >= thr * validos]
    got = {p: 0 for p, _ in elig}
    for _ in range(seats):
        best, bq = None, -1
        for p, v in elig:
            q = v / (got[p] + 1)
            if q > bq:
                bq, best = q, p
        if best:
            got[best] += 1
    return got


class Base:
    def __init__(self, prov):
        self.prov = prov['circunscripciones']
        share = {}
        V = 0
        for c in self.prov:
            V += c['validos']
            for p, v in c['votos'].items():
                share[p] = share.get(p, 0) + v
        self.share2023 = {p: 100 * v / V for p, v in share.items()}

    def simulate(self, targets, joint=False, noise=None):
        s23 = self.share2023
        total = {}
        tS, tP = targets.get('SUMAR', 0), targets.get('PODEMOS', 0)
        for c in self.prov:
            v = {}
            for p, n in c['votos'].items():
                if p == 'SUMAR':
                    base = n / s23['SUMAR']
                    if joint:
                        v['SUMAR'] = base * (tS + tP)
                    else:
                        v['SUMAR'] = base * tS
                        v['PODEMOS'] = base * tP
                elif p in ('OTROS', 'CUP'):
                    v[p] = n
                elif targets.get(p) is not None and s23.get(p):
                    v[p] = n * (targets[p] / s23[p])
                else:
                    v[p] = n
            if targets.get('SALF'):
                v['SALF'] = (targets['SALF'] / 100) * c['validos']
            if noise:
                for p in v:
                    v[p] *= noise.get(p, 1)
            validos = sum(v.values()) + c['blancos']
            for p, n in dhondt(v, c['escanos'], validos).items():
                total[p] = total.get(p, 0) + n
        return total

    def monte_carlo(self, mean, N=1500, joint=False, scale=1.0, seed=None):
        rnd = random.Random(seed)
        results = []
        tally = {p: [] for p in PARTIES}
        for _ in range(N):
            z = rnd.gauss(0, 1)
            t = {}
            for p in PARTIES:
                e = rnd.gauss(0, 1) * SD.get(p, 0.3) * scale
                bs = scale * 1.4
                if p in ('PP', 'VOX', 'SALF'):
                    e += bs * z * (1 if p == 'PP' else .65 if p == 'VOX' else .2)
                if p in ('PSOE', 'SUMAR', 'PODEMOS'):
                    e -= bs * z * (1 if p == 'PSOE' else .45 if p == 'SUMAR' else .2)
                t[p] = max(0, (mean.get(p) or 0) + e)
            noise = {p: math.exp(rnd.gauss(0, 1) * 0.05) for p in PARTIES}
            r = self.simulate(t, joint, noise)
            results.append(r)
            for p in PARTIES:
                tally[p].append(r.get(p, 0))
        q = {}
        for p in PARTIES:
            a = sorted(tally[p])
            q[p] = [pct(a, .05), pct(a, .5), pct(a, .95)]
        return results, q

    @staticmethod
    def probs(results):
        N = len(results)
        out = {'pp_vox': 0, 'pp_solo': 0, 'psoe_bloque': 0, 'bloqueo': 0}
        anyv = {'ppvox': 0, 'bloque': 0, 'bloque_sin_junts': 0, 'pp_first': 0}
        for s in results:
            ppvox = s.get('PP', 0) + s.get('VOX', 0) >= 176
            ppsolo = sum(s.get(p, 0) for p in ('PP', 'PNV', 'CC', 'UPN')) >= 176
            bloque = sum(s.get(p, 0) for p in BLOQUE23) >= 176
            if ppsolo: out['pp_solo'] += 1
            elif ppvox: out['pp_vox'] += 1
            elif bloque: out['psoe_bloque'] += 1
            else: out['bloqueo'] += 1
            anyv['ppvox'] += ppvox
            anyv['bloque'] += bloque
            anyv['bloque_sin_junts'] += sum(s.get(p, 0) for p in BLOQUE23 if p != 'JUNTS') >= 176
            anyv['pp_first'] += s.get('PP', 0) > s.get('PSOE', 0)
        return {k: round(100 * v / N, 1) for k, v in out.items()}, {k: round(100 * v / N, 1) for k, v in anyv.items()}


def pct(a, q):
    i = (len(a) - 1) * q
    lo, hi = int(math.floor(i)), int(math.ceil(i))
    return round(a[lo] + (a[hi] - a[lo]) * (i - lo))
