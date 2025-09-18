###############################################################################
# 4A00HB81 Python-ohjelmoitni (TAMK 2025)
# =============================================================================
# KT05.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-09-18
#
###############################################################################
# Tehtävänanto:
#
# Tee Python-funktio, joka muuntaa lämpötiloja eri asteikkojen välillä:
# Celsius, Fahrenheit ja Kelvin. Sitten käytä funktiota Python-ohjelmassa, joka
# kysyy käyttäjältä lämpötilan sekä tiedon siitä, missä asteikossa se on, ja
# mihin asteikkoon se muunnetaan. Ohjelmalla pitäisi siis esimerkiksi voida
# muuntaa Celsius-asteikossa annettu lämpötila Fahrenheit-asteikolle.
#
# Funktiolla pitäisi olla kolme parametria:
# +-----------+---------------------------------------------------------------+
# | Parametri | Selitys                                                       |
# +-----------+---------------------------------------------------------------+
# | degrees   | lämpötila asteina (desimaaliluku)                             |
# +-----------+---------------------------------------------------------------+
# | unit_from | missä yksikössä annettu lämpötila on (merkkijono)             |
# |           | f – Fahrehheit                                                |
# |           | c – Celcius                                                   |
# |           | k – Kelvin                                                    |
# +-----------+---------------------------------------------------------------+
# | unit_to   | mihin yksikköön annettu lämpötila muunnetaan (merkkijono,     |
# |           | sama kuin yllä)                                               |
# +-----------+---------------------------------------------------------------+
#
# Funktion pitää palauttaa lämpötila, joka on annettu unit_from-asteikossa
# muunnettuna unit_to-asteikkoon.
#
# Funktion käyttöesimerkki:
#  degrees_in = 99.9
#  degrees_out = convert_temperature(degrees_in, 'f', 'c')
#  print(f'{degrees_in} astetta Fahrenheitia on {degrees_out} astetta Celsiusta.')
#
# Edellinen esimerkki tulostaisi:
#  99.9 astetta Fahrenheitia on 37.7 astetta Celsiusta.
#
# Voit halutessasi pyöristää lopputuloksen esimerkiksi yhteen desimaaliin
# round-funktiolla.
#
# Vinkki: voit hyödyntää funktiossa esimerkiksi sisäkkäisiä if-käskyjä, joissa
# tutkitaan unit_from- ja unit_to-parametrien arvoja. Mieti myös
# virhetilanteiden käsittelyä: Mitä tapahtuu, jos funktiolle välitetään jotain
# muita kuin c, f tai k? Entä jos lähtö- ja tavoiteyksiköt ovat samat?
#
# Vinkki: Voit ensin tehdä ohjelman, joka tekee muunnokset, ja sitten siirtää
# olennaisen osan ohjelmasta funktioksi.
#
# Tarvittavat laskukaavat löydät esimerkiksi täältä:
# https://www.thoughtco.com/temperature-conversion-formulas-609324
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

###############################################################################
# EOF
