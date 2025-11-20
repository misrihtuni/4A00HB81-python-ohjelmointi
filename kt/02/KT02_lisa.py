###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# KT02_lisa.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-09-12
#
###############################################################################
# Tehtävänanto:
#
# Tässä tehtävässä ohjelmoit Pythonilla sudenpentukenraaliarvonimigeneraattorin.
#
# Kurssin opettajan oma sudenpentukenraaliarvonimi on J.E.R.E., joka tulee
# sanoista Joustavan Energinen, Rauhallinen Esilaulaja.
#
# Erään toisen henkilön arvonimen selitys on Raivokkaan Asiallinen, Utelias
# Näkemyksellinen Onnistuja. Kirjoita ohjelma, joka tekee tämän selityksen
# perusteella hänelle arvonimen ja tulostaa sen.
#
# Käytä tehtävässä merkkijonon indeksointia hakasulkeilla, jolla saat poimittua
# yksittäisiä merkkejä. Laadi tulostamista varten f-merkkijono, joka yhdistää
# arvonimen kirjaimet ja pisteet. Lopuksi tulosta arvonimi sekä sen selitys.
#
# Huomaa, että tehtävässä tarvitsee ainoastaan käyttää tiettyjen merkkien
# indeksejä, joiden perusteella poimitaan merkkijonosta yksittäisiä merkkejä.
# Jos haluat tehdä ohjelman, jolla voi generoida mistä tahansa selitteestä
# sudenpentukenraaliarvonimigeneraattorin, niin tutki Pythonin merkkijonon
# split-funktiota esimerkiksi dokumentaation avulla. Se palauttaa listan, joita
# käsitellään vasta myöhemmin kurssilla, joten jos tämä meni yli, niin ei
# haittaa mitään!
#
###############################################################################

print("Tämä ohjelma generoi sudenpentukenraaliarvonimen antamastasi selityksestä.")

selitys = input("Anna sudenpentukenraaliarvonimen selitys: ")

# Jakaa merkkijonon selitys uusiksi merkkijonoiksi välilyöntien kohdalta ja
# lisää uudet merkkijonot listaan sanat.
sanat = selitys.split(" ")

# Alustetaan arvonimi tyhjäksi merkkijonoksi.
arvonimi = ""

# for-silmukka käy läpi kaikki sanat-listan sanat ja lisää jokaisen sanan ja
# pisteen (.) arvonimen loppuun.
for sana in sanat:
    # Huomaa! Tämä voidaan kirjoittaa myös muodossa
    # arvonimi = arvonimi + sana[0] + "."
    arvonimi += f"{sana[0]}."

print(f"Sudenpentukenraaliarvonimesi on: {arvonimi}")
print("Kiitos ohjelman käytöstä.")

###############################################################################
# EOF
