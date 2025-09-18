###############################################################################
# 4A00HB81 Python-ohjelmoitni (TAMK 2025)
# =============================================================================
# KT04_while.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-09-18
#
###############################################################################
# Tehtävänanto:
#
# Mäkihypyssä on viisi arvostelutuomaria. Kirjoita Python-ohjelmaa, joka kysyy
# ensin kunkin arvostelutuomarin yhdelle hyppääjälle antamat tyylipisteet sekä
# hypyn pituuden. Sitten tulostat hyppääjän saaman pistemäärän, joka on
# tyylipisteet + 0,9 * pituus. KÄYTÄ WHILE-RAKENNETTA!
#
# Molemmissa versioissa pyydetään erikseen kunkin tuomarin antamat pisteet, ja
# lisätään ne yhteispisteisiin. Lopuksi lisätään yhteispisteisiin vielä hypyn
# pituus painotettuna tyylipisteillä.
#
# Esimerkki ohjelman ajamisesta voisi näyttää tältä (käyttäjän syöttämät asiat
# on merkattu tähdellä):
#
# Hypyn pituus: 90.5        *
# Tuomarin 1 pisteet: 17.5  *
# Tuomarin 2 pisteet: 18    *
# Tuomarin 3 pisteet: 18.5  *
# Tuomarin 4 pisteet: 17.5  *
# Tuomarin 5 pisteet: 16    *
# Yhteispisteet: 168.95
#
# Pisteet annetaan desimaalilukuina, eli muunna input-funktiolta saatu
# merkkijono ensin desimaaliluvuksi float-funktiolla.
#
###############################################################################

# Alustetaan pistelaskurin alkuarvo nollaksi.
style_points_total = 0

# Kysytään hypyn pituus käyttäjältä.
distance = float(input("Hypyn pituus: "))

# Alustetaan askeltaja ykköseksi, koska tuomareiden numerointi alkaa ykkösestä.
# Huomaa, että tässä olisi mahdollisesti soveliasta käyttää kiintoarvoja
# (constants) minimin ja maksimin asettamiseksi. Tämä parantaisi koodin
# luettavuutta (ks. KT04_while_lisa.py).
i = 1
while (i <= 5):
    # Kysytään käyttäjältä tuomarin i antamat pisteet ja sisätään ne
    # pistekertymään.
    style_points_total += float(input(f"Tuomarin {i} pisteet: "))
    i += 1 # Muista kasvattaa askeltajaa!

# Lasketaan yhteispisteet ja tulostetaan tulos näytölle.
points_total = style_points_total + 0.9 * distance
print(f"Yhteispisteet: {points_total}")

###############################################################################
# EOF
