###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# KT10.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-11-20
#
###############################################################################
# Tehtävänanto:
#
# Tee Python-moduuli nimeltä paikat, joka sisältää määrityksen luokalle nimeltä
# Paikka. Luokan tietojäseninä ovat paikan nimi ja kuvaus (molemmat
# merkkijonoja).
#
# Tee sitten testiohjelma, joka lukee kaikki paikat JSON-muotoisesta
# tiedostosta nimeltä paikat.json, ja tekee niistä Paikka-olioita. (Tätä varten
# pitää tuoda Paikka-luokka yllä olevan mukaisesti tehdystä paikat-moduulista.)
#
# JSON-tiedostossa paikat ovat seuraavassa muodossa:
#
# [
#     {"nimi": "Sisäpiha", "kuvaus": "TAMKin Teiskontien puoleinen sisäpiha."},
#     {"nimi": "Teiskontien aula", "kuvaus": "TAMKin Teiskontien aula."},
#     {"nimi": "Palvelukatu", "kuvaus": "Palvelukatu. Tämän käytävän varrella sijaitsevat opintopalvelut."},
#     {"nimi": "Tietotalon aula", "kuvaus": "Aulatila, josta pääsee C-taloon ja juhlasaliin."},
#     {"nimi": "Juhlasali", "kuvaus": "TAMKin juhlasali."},
#     {"nimi": "Kuntokadu aula", "kuvaus": "Kuntokadun puoleinen eteisaula."}
# ]
#
# Ole tarkkana JSON-tiedoston kanssa. Se sisältää taulukon, joka vastaa
# Pythonin listaa. Taulukon sisällä on olioita, jotka vastaavat Pythonin
# sanakirjoja. Paikka-oliot tehdään hakemalla näistä sanakirjoista arvot
# käyttämällä avaimina luokan tietojäsenien nimiä.
#
# JSON-tiedoston voi lukea käyttämällä json-moduulin load-funktiota, jolle
# annetaan lukemista varten avatun tiedoston nimi. Tarkista parametrit funktion
# dokumentaatiosta. Kannattaa käyttää with-käskyä tiedoston avaamiseen, niin ei
# tarvitse huolehtia tiedoston sulkemisesta.
#
# Tulosta lopuksi lista paikoista muodossa "nimi: kuvaus".
#
###############################################################################

import json

from KT10_places import Place


def read_places_from_file(filepath: str) -> list[Place]:
    """Reads a JSON file containing a list of places.

    The file should be in format [{"name": str, "description": str},...]
    :param filepath: path to the JSON file to read
    :return: list of Place objects
    """
    places: list[Place] = []
    with open(filepath, "r", encoding="utf-8") as f:
        json_content = json.load(f)
        for item in json_content:
            places.append(Place(item["name"], item["description"]))
    return places.copy()


def print_places(places: list[Place]) -> None:
    """Prints the places in the given list.
    :param places: list of Place objects to print
    """
    for place in places:
        print(place)


places = read_places_from_file("KT10_places.json")
print_places(places)


###############################################################################
# EOF
