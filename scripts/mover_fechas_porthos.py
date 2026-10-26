#!/usr/bin/env python3
"""Corre las fechas de lo que aún no se ha publicado.

  python scripts/mover_fechas_porthos.py 3          -> todo lo pendiente, 3 días más tarde
  python scripts/mover_fechas_porthos.py -1         -> un día antes
  python scripts/mover_fechas_porthos.py desde 2026-11-02   -> que el primer pendiente caiga ese día

Úsalo si apruebas el lote tarde: lo que ya venció se publicaría todo de golpe.
"""
import json, os, sys
from datetime import datetime, timedelta, date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q, D = os.path.join(ROOT, "igp", "queue.json"), os.path.join(ROOT, "igp", "published.json")
q = json.load(open(Q, encoding="utf-8"))
done = json.load(open(D, encoding="utf-8")) if os.path.exists(D) else {}
pend = [it for it in q if it["id"] not in done]
if not pend:
    sys.exit("No hay nada pendiente.")
if sys.argv[1] == "desde":
    primero = min(datetime.fromisoformat(it["fecha"]) for it in pend)
    delta = timedelta(days=(date.fromisoformat(sys.argv[2]) - primero.date()).days)
else:
    delta = timedelta(days=int(sys.argv[1]))
for it in pend:
    it["fecha"] = (datetime.fromisoformat(it["fecha"]) + delta).isoformat()
json.dump(q, open(Q, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"{len(pend)} publicaciones movidas {delta.days:+d} días. Primera: {min(it['fecha'] for it in pend)}")
