###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# KT09_Pizza.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-11-14
#
###############################################################################


class Pizza:
    name: str
    _toppings: list[str]
    _prices: dict[str, float]

    def __init__(self, name: str, toppings: list[str]):
        self.name = name
        self._toppings = toppings
        self._prices = {"normal": 0.0, "family": 0.0, "pan": 0.0}

    def get_toppings(self) -> str:
        toppings_str = ""
        for topping in self._toppings[:-1]:
            toppings_str += f"{topping}, "
        toppings_str += f"{self._toppings[-1]}"
        return toppings_str

    def has_topping(self, topping: str) -> bool:
        return topping in self._toppings

    def set_prices(
        self,
        price_normal: float | int,
        price_family: float | int,
        price_pan: float | int,
    ) -> None:
        self._prices["normal"] = float(price_normal)
        self._prices["family"] = float(price_family)
        self._prices["pan"] = float(price_pan)

    def get_prices(self) -> tuple[float, ...]:
        return tuple(
            [self._prices["normal"], self._prices["family"], self._prices["pan"]]
        )


###############################################################################
# EOF
