class Glass:  # TODO написать класс Glass согласно условию
    def __init__(self, material: str):
        self.material = material

    def get_material(self):
        return self.material


if __name__ == "__main__":
    glass1 = Glass("wood")
    print(glass1.get_material())

