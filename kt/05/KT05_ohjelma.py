###############################################################################
# 4A00HB81 Python-ohjelmoitni (TAMK 2025)
# =============================================================================
# KT05_ohjelma.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-09-18
#
###############################################################################

# Tämä funktio muuntaa annetun asteluvun lähtöyksiköstä tavoiteyksikköön ja
# palauttaa saadun asteluvun. Asteluku (degrees) on liukuluku, lähtö- ja
# tavoiteyksiköt (unit_from ja unit_to) ovat merkkijonoja. Paluuarvo on
# liukuluku.
def convert_temperature(degrees, unit_from, unit_to):
    temp_c = 0
    temp_out = 0

    # Tarkistetaan, ovatko lähtö- ja määräyksiköt samat. Mikäli näin on,
    # palautetaan alkuperäinen arvo ilman muunnosta.
    if (unit_from == unit_to):
        return degrees

    # Muunnetaan annettu astemäärä Celsius-asteiksi.
    if (unit_from == "c"):
        # C -> C: arvo ei muutu
        temp_c = degrees
    elif (unit_from == "k"):
        # K -> C: tC = tK - 273.15
        temp_c = degrees - 273.15
    elif (unit_from == "f"):
        # F -> C: tC = 5/9 * (tF - 32)
        temp_c = 5/9 * (degrees - 32)
    else:
        print(f"Tuntematon yksikkö: {unit_from}")

    # Muunnetaan Celcius-asteet annettuun yksikköön.
    if (unit_to == "c"):
        # C -> C: arvo ei muutu
        temp_out = temp_c
    elif (unit_to == "k"):
        # C -> K: tK = tC + 273.15
        temp_out = temp_c + 273.15
    elif (unit_to == "f"):
        # C -> F: tF = 9/5 * tC + 32
        temp_out = 9/5 * temp_c + 32
    else:
        print(f"Tuntematon yksikkö: {unit_to}")

    return temp_out


print("Tämä ohjelma muuntaa lämpötiloja eri asteikkojen välillä.")
degrees_in = float(input("Anna asteluku: "))
unit_from = input("Anna lähtöyksikkö (c/f/k): ")
unit_to = input("Anna tavoiteyksikkö (c/f/k): ")
degrees_out = convert_temperature(degrees_in, unit_from, unit_to)
print(f"{degrees_in} {unit_from}-astetta on {degrees_out:.2f} {unit_to}-astetta.")
print("Kiitos ohjelman käytöstä.")

###############################################################################
# EOF
