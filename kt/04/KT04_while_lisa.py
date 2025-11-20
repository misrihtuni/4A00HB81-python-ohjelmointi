###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# KT04_while_lisa.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-09-18
#
# Muokkaukset
# 2025-10-03: Tyyli päivitetty (PEP 8 compliant)
#
###############################################################################

# Tässä tuomareiden lukumäärä on tallennettu kiintoarvoon.
COUNT_JUDGES = 5

style_points_total = 0
distance = float(input("Hypyn pituus: "))

i = 1
while i <= COUNT_JUDGES:  # Huomaa, että koodia on nyt helpompi ymmärtää.
    style_points_total += float(input(f"Tuomarin {i} pisteet: "))
    i += 1

points_total = style_points_total + 0.9 * distance
print(f"Yhteispisteet: {points_total}")

###############################################################################
# EOF
