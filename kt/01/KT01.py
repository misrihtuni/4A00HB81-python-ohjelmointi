###############################################################################
# 4A00HB81 Python-ohjelmoitni (TAMK 2025)
# =============================================================================
# KT01.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-09-12
#
###############################################################################
# Tehtävänanto:
#
# Annin kotitehtävän palautus on myöhässä. Tee Python-ohjelma, joka laatii
# Annin käyttöön uskottavan selityksen siitä. Kysy ohjelmassa käyttäjältä
# seuraavat tiedot:
# - aloitus,
# - opettaja,
# - kotitehtävän tyyppi (esim. essee / raportti tms.),
# - lemmikkieläimesi laji,
# - lemmikkieläimesi nimi,
# - mitä lemmikki teki.
#
# Esimerkki ohjelman kehittelemästä selityksestä:
#   "Voi että, lehtori Staattinen, en tiedä mihin se raportti oikein joutui.
#   Lemmikkimarsuni Jooseppi varmaankin söi sen!"
#
# Tässä tehtävässä tarvitset input-funktiota sekä f-merkkijonoa, jolla
# muodostetaan print-funktiolla tulostettava teksti. Käytä omaa muuttujaansa
# jokaiselle tekstissä esiintyvälle muuttuvalle asialle, joka kysytään
# käyttäjältä.
#
# Palautusohje: laadi ohjelma, testaa se, liitä oppimispäiväkirjaan
# ohjelmateksti (eli lähdekoodi) ja lisää lyhyt kuvaus siitä miten päädyit
# tällaiseen ratkaisuun.
#
###############################################################################

aloitus = input("Anna selityksen aloitus: ")
opettaja = input("Anna opettajan nimi: ")
tehtava_tyyppi = input("Anna tehtävän tyyppi (essee, raportti, tms.): ")
lemmikki_laji = input("Anna lemmikkisi laji (esim. marsu, koira, tms.): ")
lemmikki_nimi = input("Anna lemmikkisi nimi: ")
lemmikki_tekeminen = input("Kerro, mitä lemmikkisi teki: ")

print(f"{aloitus}, {opettaja}, en tiedä mihin se {tehtava_tyyppi} oikein joutui. Lemmikki{lemmikki_laji}ni {lemmikki_nimi} varmaankin {lemmikki_tekeminen} sen!")

###############################################################################
# EOF
