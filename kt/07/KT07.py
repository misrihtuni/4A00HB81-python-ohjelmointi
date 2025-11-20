###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# KT07.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-10-31
#
# Muokkaukset:
# 2025-10-30: Lisää tarkistus kelvollisesta pizzanumerosta.
#
###############################################################################
# Tehtävänanto:
#
# Täydennä esimerkkinä käytettyä pizzalistaa (https://github.com/coniferprod/selpy-esim/blob/ee627cf34faf924be97b0fb75e7909293202cd7d/22/pizzat-taytteet.py)
# siten, että lisäät sanakirjaan normaalikokoisen pizzan hinnan kullekin
# pizzalle.
#
# Tee sitten Pythonilla pizzatilausohjelma, jossa kysytään montako pizzaa
# tilataan ja minkälaisia. Jokaisen pizzan jälkeen tulosta välisumma. Lopuksi
# tulosta pizzatilauksen kokonaishinta.
#
# Käyttäjän syötteet pitää tarkistaa, koska pizzalistassa on aukkoja, eli voi
# olla sellaisia tilausnumeroita, joille ei löydy pizzaa. Käyttäjän ei pidä
# voida tilata pizzaa, jonka tilausnumeroa ei löydy pizzalistasta, eikä hänen
# myöskään pidä voida syöttää tilattavien pizzojen määränä negatiivista lukua
# tai nollaa, eikä tilata yli 50 kappaletta mitään pizzaa.
#
# Esimerkki ohjelman käytöstä voisi näyttää vaikka tältä:
#
# Tervetuloa Guido's Pizza Palaceen, mitä haluaisitte?
# Anna pizzan numero (0 = lopetus): 12
# Pizzan numero 12 kappalemäärä: 2
# Välisumma: 2 x 12.00 = 24.00 euroa
# Anna pizzan numero (0 = lopetus): 1000
# Virheellinen pizzan numero!
# Anna pizzan numero (0 = lopetus): 19
# Pizzan numero 19 kappalemäärä: 1
# Välisumma: 1 x 13.00 = 13.00 euroa
# Anna pizzan numero (0 = lopetus): 0
# Kiitos tilauksestanne! Kokonaishintanne on 37.00 euroa.
#
###############################################################################

# Sisällytetään pizzalistakirjastosta kaikki pizzat sisältävä sanakirja.
from pizza_list import pizzas

# Alustetaan loppusumma nollaksi.
total = 0.0
# Haetaan lista pizzanumeroista.
valid_pizza_numbers = sorted(list(pizzas.keys()))

print("Tervetuloa Guido's Pizza Palaceen, mitä haluaisitte?")

# Kysytään käyttäjältä pizzoja ja lukumääriä, kunnes käyttäjä päättää lopettaa.
while True:
    pizza_number = int(input("Anna pizzan numero (0 = lopetus): "))

    # Poistutaan silmukasta, jos lopetusehto täyttyy.
    if pizza_number == 0:
        break

    # Tarkistetaan, onko pizzanumero kelvollinen.
    if pizza_number not in valid_pizza_numbers:
        print("Virheellinen pizzan numero!")
        continue

    pizza_count = int(input(f"Pizzan numero {pizza_number} kappalemäärä: "))
    # Haetaan pizza-sanakirja kaikkien pizzojen sanakirjasta.
    pizza = pizzas[pizza_number]
    # Etsitään pizza-sanakirjasta hinta-avaimen arvo.
    pizza_price = pizza["price"]
    # Lasketaan ja tulostetaan välisumma ja lisätään se loppusummaan.
    subtotal = pizza_count * pizza_price
    total += subtotal
    print(f"Välisumma: {pizza_count} x {pizza_price:.2f} = {subtotal:.2f} euroa")

if total != 0:
    print(f"Kiitos tilauksestanne! Kokonaishintanne on {total:.2f} euroa.")
else:
    print(
        "Kiitos käynnistä, toivottavasti löydätte ensi kerralla jotakin "
        "mieluisaa tilattavaa."
    )

###############################################################################
# EOF
