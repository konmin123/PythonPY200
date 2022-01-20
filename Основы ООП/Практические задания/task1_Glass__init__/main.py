from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if not occupied_volume >= 0:
            raise ValueError
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass_1 = Glass(500, 100)
    glass_2 = Glass(500, 50)

    glass_3 = Glass(100, 0)
