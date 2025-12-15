"""
TAMK 4A00HB81 Python Programmin - Final Project

In this project the goal was to make a simple text adventure game using Python.

Copyright (c) 2025 Miska Rihu <miska.rihu@tuni.fi>
License: MIT License (see LICENSE for details)
"""

import datetime as dt
import sys
import textwrap as tw
from typing import Any

##############################################################################################
# TEXTS
##############################################################################################

MSG_COMMAND_TOO_FEW_WORDS = "Komennossa on liian vähän sanoja!"
MSG_COMMAND_TOO_MANY_WORDS = "Komennossa on liikaa sanoja!"
MSG_COMMAND_UNKNOWN = "Tuntematon komento!"
MSG_DIRECTION_CANNOT_GO = "En minä tuollaiseen suuntaan voi mennä..."
MSG_ITEM_NOT_HERE = "Ei täällä ole mitään sellaista..."
MSG_ITEM_NOT_WITH_ME = "Ei minulla ole mitään tuollaista mukana..."
MSG_ITEM_PICKED_UP = "Poimit esineen '{item}'."
MSG_ITEM_DROPPED = "Pudotit esineen '{item}'."
MSG_ITEM_PLACED = "{item} asetettu paikoilleen."
MSG_ITEM_NEED_NOT_PLACE = "En usko, että tätä tarvitsee viedä paikoilleen..."
MSG_ITEM_CANNOT_PLACE = "Ei tämä tänne kuulu..."
MSG_ITEM_CANNOT_DRINK = "Ei tätä voi juoda..."
MSG_QUIT = "Kiitos pelin pelaamisesta!"

ERR_ITEM_INVALID = "Invalid item"
ERR_INVENTORY_ADD_ITEM = "Cannot add '{0}' to inventory"
ERR_INVENTORY_REMOVE_ITEM = "Cannot remove '{0}' from inventory"
ERR_DESTROY_ITEM = "Cannot destroy '{0}'"


INTRO_TEXT = (
    "Olet opiskelijana TAMKin pääkampuksella. "
    "Tehtävänäsi on löytää kadonneet esineet ja viedä ne takaisin "
    "paikalleen.\n\n"
    "Peli toimii suomenkielisellä komentotulkilla, joka ymmärtää "
    "yksi- ja kaksisanaisia komentoja muotoa 'verbi' 'objekti'. "
    "Komennot voit saada näkyviin milloin tahansa komennolla "
    "'apua'.\n\n"
    "Onnea matkaan.\n\n"
    "(Paina [ENTER] aloittaaksesi pelin.)"
)

OUTRO_TEXT = (
    "Hienoa! Pääsit pelin läpi!\n"
    "Pisteet: {points} / {total_points}\n"
    "Käytetty aika: {time_m:.0f}m {time_s:02.0f}s\n"
    "Esineitä löydetty: {items_found} / {items_max}"
)

##############################################################################################
# SETTINGS
##############################################################################################

STARTING_PLACE = "teiskontien sisäpiha"
SCREEN_WIDTH = 70


##############################################################################################
# DATA
##############################################################################################

# Keys
KEY_DESCRIPTION = "description"
KEY_TARGET_PLACE = "target_place"
KEY_POINTS = "points"
KEY_INVENTORY = "inventory"
KEY_DIRECTIONS = "directions"
KEY_DIRECTION_N = "pohjoiseen"
KEY_DIRECTION_S = "etelään"
KEY_DIRECTION_E = "itään"
KEY_DIRECTION_W = "länteen"
KEY_CURRENT_PLACE = "current_place"
KEY_COUNT_ITEMS_FOUND = "count_items_found"

global_items = {
    "mikrofoni": {
        KEY_DESCRIPTION: "Mikrofonissa on tarra 'TAMK Juhlasali'.",
        KEY_TARGET_PLACE: "juhlasali",
        KEY_POINTS: 20,
    },
    "energiajuoma": {
        KEY_DESCRIPTION: "Halpa mutta tehokas piriste",
        KEY_POINTS: 5,
    },
    "opiskelijakortti": {
        KEY_DESCRIPTION: "Perinteinen opiskelijakortti, jonka haltijaksi on merkitty Sami Mäkinen.",
        KEY_TARGET_PLACE: "kuntokadun aula",
        KEY_POINTS: 10,
    },
}

global_places = {
    "teiskontien sisäpiha": {
        KEY_DESCRIPTION: (
            "Seisot Teiskontien sisäpihalla. Ympärilläsi on kolme rakennusta: "
            "lännessä Tietotalo, pohjoisessa päärakennus ja idässä A-talo. "
            "Vain päärakennuksen ovi näyttää olevan auki."
        ),
        KEY_INVENTORY: ["opiskelijakortti"],
        KEY_DIRECTIONS: {
            KEY_DIRECTION_N: "teiskontien aula",
        },
    },
    "teiskontien aula": {
        KEY_DESCRIPTION: (
            "Teiskontien aulassa ei näy ketään eikä vahtimestarienkaan "
            "huoneessa ole valoja. Palvelukadulta kuuluu opiskelijoiden "
            "puhetta. Tietotalon suunnalta kuuluu ääniä..."
        ),
        KEY_INVENTORY: [],
        KEY_DIRECTIONS: {
            KEY_DIRECTION_N: "palvelukatu",
            KEY_DIRECTION_S: "teiskontien sisäpiha",
            KEY_DIRECTION_W: "tietotalon aula",
        },
    },
    "palvelukatu": {
        KEY_DESCRIPTION: (
            "Saavut palvelukadulle, jossa on muutamia opiskelijoita ja juoma-"
            "automaatti. Mitään muuta erikoista täällä ei näy. Kuulet ohimennen "
            "jonkun sanovan, että Kuntokadun aulassa olisi jotakin ylimääräistä "
            "tavaraa..."
        ),
        KEY_INVENTORY: ["energiajuoma"],
        KEY_DIRECTIONS: {
            KEY_DIRECTION_N: "kuntokadun aula",
            KEY_DIRECTION_S: "teiskontien aula",
        },
    },
    "kuntokadun aula": {
        KEY_DESCRIPTION: (
            "Kuntokadun aulan infopiste näyttää olevan auki. Ainakin jos "
            "kadottaisin jotakin, voisin vielä käydä kysymässä sitä tiskiltä..."
        ),
        KEY_INVENTORY: ["mikrofoni"],
        KEY_DIRECTIONS: {
            KEY_DIRECTION_N: "",
            KEY_DIRECTION_S: "palvelukatu",
        },
    },
    "tietotalon aula": {
        KEY_DESCRIPTION: (
            "Tietotalon aulassa huomaat Juhlasalin oven olevan auki ja kuulet "
            "sisältä turhautunutta juputusta. Mitäköhän siellä tapahtuu..."
        ),
        KEY_INVENTORY: [],
        KEY_DIRECTIONS: {
            KEY_DIRECTION_N: "juhlasali",
            KEY_DIRECTION_E: "teiskontien aula",
        },
    },
    "juhlasali": {
        KEY_DESCRIPTION: (
            "Juhlasalissa näet päätään pudistelevan vahtimestarin. Hän kertoo "
            "sinulle etsineensä toista juhlasalin mikrofoneista kaikkialta "
            "ilman tulosta..."
        ),
        KEY_INVENTORY: [],
        KEY_DIRECTIONS: {
            KEY_DIRECTION_S: "tietotalon aula",
        },
    },
}


##############################################################################################
# HELPER METHODS
##############################################################################################


def print_err(text: str) -> None:
    """Prints the given text prefixed with \"ERROR: \"."""
    print(f"ERROR: {text}")


def print_wrapped(text: str, max_width: int = SCREEN_WIDTH) -> None:
    """Wraps the given text to fit the given width.

    Parameters
    ----------
    text
        The text to print on the screen.
    max_width
        The maximum with for a line in characters.
    """
    print(tw.fill(text, width=max_width, replace_whitespace=False))


def read_command() -> list[str]:
    """Displays the command prompt and returs the user input tokens.

    Converts the user input to lower case and splits it at any whitespace
    character.
    """
    return input("> ").lower().split()


def print_inventory(
    inventory: list[str], description: str = "", text_empty: str = ""
) -> None:
    """Prints the given ``inventory`` in readable format.

    Parameters
    ----------
    inventory
        The inventory to print.
    description
        The description text shown before the item listing, for examle "You
        have these items". If NOT specified (or set to an empty string),
        only the listing of items will be shown.
    text_empty
        The text that will be displayed if the ``inventory`` has no items in
        it. If NOT specified (or set to an empty string), prints nothing.
    """
    if len(inventory) == 0:
        if text_empty != "":
            print_wrapped(text_empty)
        return
    message = ""
    if len(description) > 0:
        message = description + ": "
    for item in inventory:
        message += f"{item}, "
    print_wrapped(message[:-2])


def add_item_to_inventory(inventory: list[str], item: str) -> None:
    """Adds the given item to the given inventory and sorts the inventory.

    Note: If the item does not exists in ``global_items``, terminates the
    program.

    Note: If the item already exists in the ``inventory``, prints an error
    message and returns.

    Parameters
    ----------
    inventory
        Where the item should be added to.
    item
        Name of the item to add.
    """
    global global_items
    if item not in global_items.keys():
        sys.exit(f"{ERR_INVENTORY_ADD_ITEM.format(item)}: {ERR_ITEM_INVALID}")
    if item in inventory:
        print_err(f"{ERR_INVENTORY_ADD_ITEM.format(item)}: Already added!")
        return
    inventory.append(item)
    inventory.sort()


def remove_item_from_inventory(inventory: list[str], item: str) -> None:
    """Removes the given item from the given inventory.

    Note: If the item does not exists in ``global_items``, terminates the
    program.

    Note: If the item does not exists in the ``inventory``, prints an error
    message and returns.

    Parameters
    ----------
    inventory
        Where the item should be removed from.
    item
        Name of the item to remove.
    """
    global global_items
    if item not in global_items.keys():
        sys.exit(f"{ERR_INVENTORY_REMOVE_ITEM.format(item)}: {ERR_ITEM_INVALID}")
    if item not in inventory:
        print_err(f"{ERR_INVENTORY_REMOVE_ITEM.format(item)}: Not found!")
        return
    inventory.remove(item)
    return


def destroy_item(item: str, player: dict[str, Any]) -> None:
    """Removes the given item from the game and grants points to ``player``.

    Note: If the item does not exists in ``global_items``, terminates the
    program.

    Parameters
    ----------
    item
        Name of the item to remove from the game.
    """
    global global_items
    if item not in global_items.keys():
        sys.exit(f"{ERR_DESTROY_ITEM.format(item)}: {ERR_ITEM_INVALID}")
    player[KEY_POINTS] += global_items[item][KEY_POINTS]
    player[KEY_COUNT_ITEMS_FOUND] += 1
    global_items.pop(item)


def check_winning_condition() -> bool:
    """Checks if the goal has been fullfilled."""
    global global_items
    is_fullfilled = "mikrofoni" not in global_items
    return is_fullfilled


def calculate_max_points() -> int:
    """Calculates the maximum available points."""
    global global_items
    total_points = 0
    for _, v in global_items.items():
        total_points += v[KEY_POINTS]
    return total_points


##############################################################################################
# COMMANDS
##############################################################################################

CMD_QUIT = "lopeta"
CMD_EXPLORE = "katsele"
CMD_INVENTORY = "mukana"
CMD_HELP = "apua"
CMD_INSPECT = "tutki"
CMD_GO = "mene"
CMD_TAKE = "ota"
CMD_DROP = "pudota"
CMD_DRINK = "juo"
CMD_PLACE = "aseta"

COMMANDS_1 = [CMD_QUIT, CMD_EXPLORE, CMD_INVENTORY, CMD_HELP]
COMMANDS_2 = [CMD_INSPECT, CMD_GO, CMD_TAKE, CMD_DROP, CMD_DRINK, CMD_PLACE]


### One-Word Command Handlers ===


def on_cmd_explore(place) -> None:
    """Describes the given place to the player.

    Parameters
    ----------
    place
        Name of the place to describe.
    """
    global global_places
    description = global_places[place][KEY_DESCRIPTION]
    inventory = global_places[place][KEY_INVENTORY]
    print_wrapped(description)
    print_inventory(inventory, description="Ympärilläsi näet seuraavia asioita")


def on_cmd_inventory(player) -> None:
    """Describes the contents of the given player's inventory."""
    inventory = player[KEY_INVENTORY]
    if len(inventory) == 0:
        print_wrapped("Minulla ei ole mitään mukana...")
        return
    print_inventory(inventory, "Minulla on tällaisia asioita mukana")


def on_cmd_help() -> None:
    """Lists all available commands to the player."""
    text = "Käytettävissä olevat komennot: "
    for c1 in sorted(COMMANDS_1):
        text += f"{c1}, "
    for c2 in sorted(COMMANDS_2):
        text += f"{c2} ..., "
    print_wrapped(text[:-2])


### Two-Word Command Handlers ###


def on_cmd_inspect(player: dict[str, Any], item: str) -> None:
    """Prints the description of the given item.

    Note: Only prints the description if the item is in the player's inventory
    or in the current place.
    """
    global global_places
    player_inventory = player[KEY_INVENTORY]
    place_inventory = global_places[player[KEY_CURRENT_PLACE]][KEY_INVENTORY]
    inspectable_items = player_inventory + place_inventory
    if item not in inspectable_items:
        print_wrapped(MSG_ITEM_NOT_HERE)
        return
    print_wrapped(global_items[item][KEY_DESCRIPTION])


def on_cmd_go(player: dict[str, Any], direction: str) -> None:
    """Moves the player to the place in the given direction if possible."""
    global global_places
    place = global_places[player[KEY_CURRENT_PLACE]]
    possible_directions = place[KEY_DIRECTIONS]
    if direction not in list(possible_directions.keys()):
        print_wrapped(MSG_DIRECTION_CANNOT_GO)
        return
    new_place = place[KEY_DIRECTIONS][direction]
    player[KEY_CURRENT_PLACE] = new_place
    on_cmd_explore(new_place)


def on_cmd_take(player: dict[str, Any], item: str) -> None:
    """Moves the ``item`` from the ``player``'s current location to the ``player``'s inventory."""
    global global_places
    player_inventory = player[KEY_INVENTORY]
    place_inventory = global_places[player[KEY_CURRENT_PLACE]][KEY_INVENTORY]
    if item not in place_inventory:
        print_wrapped(MSG_ITEM_NOT_HERE)
        return
    remove_item_from_inventory(place_inventory, item)
    add_item_to_inventory(player_inventory, item)
    print_wrapped(MSG_ITEM_PICKED_UP.format(item=item))


def on_cmd_drop(player: dict[str, Any], item: str) -> None:
    """Moves the ``item`` from the ``player``'s inventory to the ``player``'s current location."""
    global global_places
    player_inventory = player[KEY_INVENTORY]
    place_inventory = global_places[player[KEY_CURRENT_PLACE]][KEY_INVENTORY]
    if item not in player_inventory:
        print_wrapped(MSG_ITEM_NOT_WITH_ME)
        return
    remove_item_from_inventory(player_inventory, item)
    add_item_to_inventory(place_inventory, item)
    print_wrapped(MSG_ITEM_DROPPED.format(item=item))


def on_cmd_drink(player: dict[str, Any], item: str) -> None:
    """Drinks the given item if possible."""
    inventory = player[KEY_INVENTORY]
    drinkable_items = ["energiajuoma"]
    if item not in inventory:
        print_wrapped(MSG_ITEM_NOT_WITH_ME)
        return
    if item not in drinkable_items:
        print_wrapped(MSG_ITEM_CANNOT_DRINK)
        return
    print_wrapped("Energiajuoma toi sinulle lisää energiaa.")
    remove_item_from_inventory(inventory, item)
    destroy_item(item, player)


def on_cmd_place_item(player: dict[str, Any], item: str) -> None:
    """Places the given item if possible and removes it from the game."""
    global global_items
    inventory = player[KEY_INVENTORY]
    if item not in inventory:
        print_wrapped(MSG_ITEM_NOT_WITH_ME)
        return
    if KEY_TARGET_PLACE not in list(global_items[item].keys()):
        print_wrapped(MSG_ITEM_NEED_NOT_PLACE)
        return
    target_place = global_items[item][KEY_TARGET_PLACE]
    current_place = player[KEY_CURRENT_PLACE]
    if current_place != target_place:
        print_wrapped(MSG_ITEM_CANNOT_PLACE)
        return
    print_wrapped(MSG_ITEM_PLACED.format(item=item.capitalize()))
    remove_item_from_inventory(player[KEY_INVENTORY], item)
    destroy_item(item, player)


##############################################################################################
# MAIN LOOP
##############################################################################################


def main():
    TOTAL_POINTS = calculate_max_points()
    TIME_START = dt.datetime.now()
    ITEMS_MAX = len(global_items)

    player = {
        KEY_CURRENT_PLACE: STARTING_PLACE,
        KEY_INVENTORY: [],
        KEY_POINTS: 0,
        KEY_COUNT_ITEMS_FOUND: 0,
    }

    print_wrapped(INTRO_TEXT)
    input()
    print()
    on_cmd_explore(player[KEY_CURRENT_PLACE])

    while True:
        print()
        command = read_command()
        command_len = len(command)
        command_verb = ""
        command_target = ""
        if command_len == 0:
            continue
        if command_len > 2:
            print_wrapped(MSG_COMMAND_TOO_MANY_WORDS)
            continue
        command_verb = command[0]
        if command_len == 2:
            command_target = command[1]

        # One-word commands.
        if command_verb in COMMANDS_1:
            if command_target != "":
                print_wrapped(MSG_COMMAND_TOO_MANY_WORDS)
                continue
            elif command_verb == CMD_QUIT:
                break
            elif command_verb == CMD_EXPLORE:
                on_cmd_explore(player[KEY_CURRENT_PLACE])
            elif command_verb == CMD_INVENTORY:
                on_cmd_inventory(player)
            elif command_verb == CMD_HELP:
                on_cmd_help()
        # Two-word commands.
        elif command_verb in COMMANDS_2:
            if command_target == "":
                print_wrapped(MSG_COMMAND_TOO_FEW_WORDS)
                continue
            if command_verb == CMD_INSPECT:
                on_cmd_inspect(player, item=command_target)
            elif command_verb == CMD_GO:
                on_cmd_go(player, direction=command_target)
            elif command_verb == CMD_TAKE:
                on_cmd_take(player, item=command_target)
            elif command_verb == CMD_DROP:
                on_cmd_drop(player, item=command_target)
            # Special commands
            elif command_verb == CMD_DRINK:
                on_cmd_drink(player, item=command_target)
            elif command_verb == CMD_PLACE:
                on_cmd_place_item(player, item=command_target)
        # Unknown commands.
        else:
            print_wrapped(MSG_COMMAND_UNKNOWN)
        if check_winning_condition():
            print()
            time_end = dt.datetime.now() - TIME_START
            total_seconds = time_end.total_seconds()
            print_wrapped(
                OUTRO_TEXT.format(
                    points=player[KEY_POINTS],
                    total_points=TOTAL_POINTS,
                    time_m=total_seconds / 60,
                    time_s=total_seconds % 60,
                    items_found=player[KEY_COUNT_ITEMS_FOUND],
                    items_max=ITEMS_MAX,
                )
            )
            break

    print_wrapped(MSG_QUIT)


if __name__ == "__main__":
    main()
