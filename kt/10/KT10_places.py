###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# KT10_places.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-11-20
#
###############################################################################


class Place:
    """Represents a place object in the game.

    Contains the name and the description of the place and has methods for
    setting and retrieving those attributes.
    """

    _name: str
    _description: str

    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description

    def get_name(self) -> str:
        """Returns the name of the place."""
        return self._name

    def set_description(self, description: str) -> None:
        """Sets the description of the place to the given text."""
        self._description = description.strip()

    def get_description(self) -> str:
        """Returns the description of the place as text."""
        return self._description

    def __str__(self):
        """Returns the place as text in the format <name>: <description>"""
        return f"{self.get_name()}: {self.get_description()}"


###############################################################################
# EOF
