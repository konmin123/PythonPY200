from typing import Any, Iterable, Optional

from node import Node
from node import Dln


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"


class DoubleLinkedList(LinkedList):
    def __init__(self, data: Iterable = None):
        """Конструктор двусвязного списка"""
        self.len = 0
        self.head: Optional[Dln] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def step_by_step_on_dln(self, index: int) -> Dln:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_dln = self.head
        for _ in range(index):
            current_dln = current_dln.next

        return current_dln

    @staticmethod
    def linked_nodes(left_dln: Dln, right_dln: Optional[Dln] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_dln: Левый или предыдущий узел
        :param right_dln: Правый или следующий узел
        """
        left_dln.next = right_dln
        right_dln.prev = left_dln


dls1 = DoubleLinkedList([1, 2, 3, 4, 5])
print(repr(dls1))
dls1.append(6)
print(dls1)
print(dls1.__getitem__(2))
print(dls1.tail)
print(dls1.head)
print(type(dls1))