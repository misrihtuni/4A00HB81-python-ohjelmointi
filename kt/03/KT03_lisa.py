###############################################################################
# 4A00HB81 Python-ohjelmoitni (TAMK 2025)
# =============================================================================
# KT03_lisa.py
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


# Tämä aliohjelma ottaa vastaan parametrina promptin, joka tulostetaan
# konsoliin käyttäjälle nähtäväksi (esim. "Anna vuotuinen ajomatka"), muuttaa
# käyttäjältä saadun merkkijonon liukuluvuksi ja palauttaa sen.
#
# Huomaa, että kaksoispiste lisätään tässä automaattisesti promptin perään eikä
# sitä tarvitse enää kirjoittaa aliohjelmakutsuun. Huomaa myös, että arvoa ei
# tarvitse tallentaa muuttujaan ennen sen palauttamista.
def read_float_input(prompt):
    return float(input(f"{prompt}: "))


# Aliohjelma laskee polttoaineen kustannukset kolmen arvon pohjalta: ajettu
# matka (km), kulutus (l/100km) ja polttoaineen hinta (€/l) ja tallentaa sen
# muuttujaan expenses. Tämän jälkeen aliohjelma palauttaa lasketun arvon.
#
# Huomaa, että laskettua arvoa ei ole pakko tallentaa muuttujaan ennen sen
# palauttamista! Tässä on vain esitelty toinen tapa tietojen käsittelyyn.
def calculate_fuel_expenses(distance, fuel_consumption_100km, fuel_price):
    expenses = distance * (fuel_consumption_100km / 100) * fuel_price
    return expenses


print("Tämä ohjelma vertailee bensiini- ja dieselmoottoriauton vuotuisia matkakuluja.")

# Nyt tietoja kysyttäessä voidaan käyttää luomaamme read_float_input-aliohjelmaa.
# Tämä helpottaa toiminnan muuttamista tarvittaessa.
#
# Huomaa tässä, että kaksoispiste jätetään pois, sillä aliohjelmamme lisää sen
# automaattisesti!
driven_distance = read_float_input("Anna vuotuinen ajomatka (km)")
price_gas = read_float_input("Anna bensiinin litrahinta (€/l)")
price_diesel = read_float_input("Anna dielesin litrahinta (€/l)")
consumption_gas_100km = read_float_input("Anna bensiiniauton kulutus (l/100km)")
consumption_diesel_100km = read_float_input("Anna dieselauton kulutus (l/100km)")
tax_diesel = read_float_input("Dieselveron määrä (€/vuosi)")

# Voimme laskea kulutukset helposti calculate_fuel_expenses-aliohjelman avulla:
expenses_gas = calculate_fuel_expenses(
    driven_distance, consumption_gas_100km, price_gas
)
expenses_diesel = (
    calculate_fuel_expenses(driven_distance, consumption_diesel_100km, price_diesel)
    + tax_diesel
)


# Formatoinnin kanssa oli perustehtävän puolella hieman haasteita silloin, kun
# tuloksena on tasaluku. Tällöin toinen desimaalinollista jäi pois. Tämä
# voidaan korjata käyttämällä formatointia. Tässä muuttujan lopussa oleva :.2f
# kertoo, että arvo halutaan esittää desimaalilukuna (float -> f), jossa on 2
# desimaalia.
print(f"Bensiiniauton vuotuiset matkakulut ovat {expenses_gas:.2f} €.")
print(f"Dieselauton vuotuiset matkakulut ovat {expenses_diesel:.2f} €.")

if expenses_gas < expenses_diesel:
    # Huomaa, että formatointi toimii myös laskutoimituksissa, kun
    # laskutoimitus laitetaan sulkeisiin.
    print(
        f"Bensiiniauton vuotuiset matkakulut ovat "
        f"{(expenses_diesel - expenses_gas):.2f} € halvemmat."
    )
elif expenses_diesel < expenses_gas:
    print(
        f"Dieselauton vuotuiset matkakulut ovat "
        f"{(expenses_gas - expenses_diesel):.2f} € halvemmat."
    )
else:
    print("Molempien autojen vuotuiset matkakulut ovat yhtä suuret.")

print("Kiitos ohjelman käytöstä.")

###############################################################################
# EOF
