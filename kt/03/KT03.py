###############################################################################
# 4A00HB81 Python-ohjelmoitni (TAMK 2025)
# =============================================================================
# KT03.py
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
# Tee ohjelma, joka vertailee auton vuotuisia matkakuluja. Ohjelma laskee
# kummalla polttomoottorityypillä, bensiini- vai dieselmoottorilla, vuotuinen
# ajaminen tulee halvemmaksi.
#
# Ohjelman tulee kysyä ensin käyttäjältä seuraavat tiedot:
# -	Autolla ajettava vuotuinen kilometrimäärä
# -	Bensiinin litrahinta euroina
# -	Dieselöljyn litrahinta euroina
# -	Bensiinimoottorisen auton kulutus (litraa / 100 km)
# -	Dieselmoottorisen auton kulutus (litraa / 100 km)
# -	Dieselin käyttövoimaveron määrä
#
# Kun tiedot on kysytty, ohjelma laskee bensiinimoottorisen ja
# dieselmoottorisen auton vuotuiset matkakulut, ottaen huomioon myös
# dieselmoottorin käyttövoimaveron. Tämän jälkeen ohjelma raportoi nämä kulut
# sekä kertoo kumpi tulee halvemmaksi, ja paljonko halvemmaksi.
#
# Laskukaavat:
# - bensa-auton matkakulut = kilometrimäärä * bensan kulutus * bensan hinta
# - dieselauton matkakulut = kilometrimäärä * dieselin kulutus * dieselin hinta + dieselvero
#
# Tehtävässä tarvitset Pythonin input-funktiota sekä if-käskyä, sekä
# laskulausekkeita ja muuttujia. Kaikkia kysyttäviä tietoja voi käsitellä
# desimaalilukuina, joten voit muuntaa input-funktion palauttaman merkkijonon
# desimaaliluvuksi float-funktiolla.
#
# Tehtävässä ei tarvitse ottaa huomioon sitä, että polttoaineen litrahinta
# muuttuu vuoden aikana. Huomaa, että kulutuslukema ilmoitetaan litroina 100 km
# kohti! Jos haluat, voit lopuksi pyöristää näytettävät tulokset Pythonin
# round-funktiolla. Älä kuitenkaan pyöristä välituloksia, koska se vaikuttaa
# lopputulokseen!
#
###############################################################################

print("Tämä ohjelma vertailee bensiini- ja dieselmoottoriauton vuotuisia matkakuluja.")

driven_distance = float(input("Anna vuotuinen ajomatka (km): "))
price_gas = float(input("Anna bensiinin litrahinta (€/l): "))
price_diesel = float(input("Anna dielesin litrahinta (€/l): "))
consumption_gas_100km = float(input("Anna bensiiniauton kulutus (l/100km): "))
consumption_diesel_100km = float(input("Anna dieselauton kulutus (l/100km): "))
tax_diesel = float(input("Dieselveron määrä (€/vuosi): "))

expenses_gas = driven_distance * (consumption_gas_100km / 100) * price_gas
expenses_diesel = (
    driven_distance * (consumption_diesel_100km / 100) * price_diesel + tax_diesel
)

print(f"Bensiiniauton vuotuiset matkakulut ovat {round(expenses_gas, 2)} €.")
print(f"Dieselauton vuotuiset matkakulut ovat {round(expenses_diesel, 2)} €.")

if expenses_gas < expenses_diesel:
    print(
        f"Bensiiniauton vuotuiset matkakulut ovat "
        f"{round(expenses_diesel - expenses_gas, 2)} € halvemmat."
    )
elif expenses_diesel < expenses_gas:
    print(
        f"Dieselauton vuotuiset matkakulut ovat "
        f"{round(expenses_gas - expenses_diesel, 2)} € halvemmat."
    )
else:
    print("Molempien autojen vuotuiset matkakulut ovat yhtä suuret.")

print("Kiitos ohjelman käytöstä.")

# Huomaa!
# Tehtävässä tulee toistettua tiettyjä rivejä useaan kertaan. Tämän pystyisi
# välttämään aliohjelmia käyttämällä. Aliohjelmia hyödyntävän ratkaisun löydät
# tiedostosta KT3_lisa.py.

###############################################################################
# EOF
