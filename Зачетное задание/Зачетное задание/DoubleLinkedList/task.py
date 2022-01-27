from typing import Any, Iterable, Optional, Iterator
from collections.abc import MutableSequence

from node import Node
from node import Dln


class LinkedList(MutableSequence):
    CLASS_NODE = Node
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index):
        if index == 0:
            self.head = LinkedList.step_by_step_on_nodes(self, 1)
        if 0 < index < self.len - 1:
            left_node = LinkedList.step_by_step_on_nodes(self, index - 2)
            right_node = LinkedList.step_by_step_on_nodes(self, index)
            self.linked_nodes(left_node, right_node)
        if index == self.len - 1:
            current_node = LinkedList.step_by_step_on_nodes(self, index - 1)
            current_node.next = None
            self.tail = current_node
        self.len -= 1

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def insert(self, index: int, value) -> None:
        pass

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = self.CLASS_NODE(value)

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


    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def nodes_iterator(self) -> Iterator[Node]:
        current_node = self.head
        for _ in range(self.len):
            yield current_node
            current_node = current_node.next

    def clear(self):
        self.head = None
        self.tail = None

        self.len = 0


# class Dllist(LinkedList):
    #CLASS_NODE =Dll

if __name__ == "__main__":
    list_ = [1, 2, 3]

    ll = LinkedList(list_)
    print(ll.len)
