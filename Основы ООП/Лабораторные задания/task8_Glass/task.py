from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.add_capacity(capacity_volume)

        self.occupied_volume = None
        self.add_occupied(occupied_volume)

    def add_capacity(self, capacity_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def add_occupied(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, value_water: Union[int, float]):
        if not isinstance(value_water, (int, float)):
            raise TypeError
        if value_water <= 0:
            raise ValueError
        if self.occupied_volume + value_water > self.capacity_volume:
            self.occupied_volume = self.capacity_volume
        else:
            self.occupied_volume += value_water

    def remove_water(self, value_water: Union[int, float]):
        if not isinstance(value_water, (int, float)):
            raise TypeError
        if value_water <= 0:
            raise ValueError
        if self.occupied_volume - value_water < 0:
            raise ValueError
        self.occupied_volume -= value_water


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(70)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.remove_water(50)
    print(glass.capacity_volume, glass.occupied_volume)
