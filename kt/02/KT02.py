###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# KT02.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-09-12
#
# Muokkaukset
# 2025-10-03: Tyyli päivitetty (PEP 8 compliant)
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

arvonimi = "Raivokkaan Asiallinen, Utelias Näkemykselline Onnistuja"
print(
    f"Sudenpentukenraaliarvonimesi on: "
    f"{arvonimi[0]}.{arvonimi[11]}.{arvonimi[23]}.{arvonimi[31]}.{arvonimi[46]}."
)

# Generaattori, jolla pystyy luomaan sudenpentukenraaliarvonimen mistä tahansa
# selityksestä, löytyy tiedostosta KT02_lisa.py.

###############################################################################
# EOF
