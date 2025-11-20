###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# KT09.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-11-14
#
###############################################################################
# Tehtävänanto:
#
# teksti tähän
#
###############################################################################

from KT09_Pizza import Pizza

pizza_dict = {
    1: Pizza("Margherita", ["mozzarella", "tomaatti"]),
    2: Pizza("Bolognese", ["jauhelihakastike"]),
    3: Pizza("Americana", ["kinkku", "ananas", "aurajuusto"]),
}

# Lisätään pizzoja listaan
pizza_dict[1].set_prices(10.5, 18, 15)
pizza_dict[2].set_prices(11, 18, 15)
pizza_dict[3].set_prices(11, 20, 16)


# Tulostaa listan yhden rivin.
def print_menu_row(number, name, price_normal, price_family, price_pan):
    print(
        f"{number:3}"
        f" {name:30}"
        f" {price_normal:^8}"
        f" {price_family:^8}"
        f" {price_pan:^8}"
    )


# Tulostaa ruokalistan.
def print_menu(pizza_dict):
    print_menu_row("Nro", "Nimi", "Normaali", "Perhe", "Pannu")
    for number, pizza in pizza_dict.items():
        prices = pizza.get_prices()
        print_menu_row(
            number,
            pizza.name,
            f"{prices[0]:.2f}",
            f"{prices[1]:.2f}",
            f"{prices[2]:.2f}",
        )
        print_menu_row("", pizza.get_toppings(), "", "", "")
        print()


print_menu(pizza_dict)

###############################################################################
# EOF
