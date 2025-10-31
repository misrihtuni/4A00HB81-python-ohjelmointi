from ht_directions import Direction
from ht_items import Item


class Place:
    id: int = 0
    name: str = "<place name>"
    description: str = "<place description>"
    items: list[Item] = []
    directions: dict[Direction, str] = {
        Direction.NORTH: None,
        Direction.EAST: None,
        Direction.SOUTH: None,
        Direction.WEST: None,
    }

    def __init__(self, id: int, name: str, description: str, items: list[Item]):
        self.id = id
        self.name = name
        self.description = description
        self.items = items

    def get_target_place(self, direction: Direction):
        return self.directions[direction]
