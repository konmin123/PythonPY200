from typing import Iterable
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Iterable:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Iterable) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def read(self) -> Iterable:
        with open(self.filename, "r", encoding="utf8") as f:
            return [line.rstrip() for line in f]
        pass

    def write(self, data: Iterable) -> None:
        with open(self.filename, "w", encoding="utf8") as f:
            for value in data:
                f.write(str(value) + "\n")

    def __init__(self, filename: str):
        self.filename = filename


    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


if __name__ == '__main__':
    write_data = [1, 2, 3]
    driver = SimpleFileDriver('output.txt')
    driver.write(write_data)

    read_data = driver.read()
    print(read_data)
