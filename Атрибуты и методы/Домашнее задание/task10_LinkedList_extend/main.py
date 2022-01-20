from typing import Iterable, Optional, Any

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def __len__(self):
        return self.len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

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

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:
            raise IndexError()
        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            noda = self.step_by_step_on_nodes(index-1)
            noda.next = None
        else:
            left_node = self.step_by_step_on_nodes(index - 1)
            right_node = self.step_by_step_on_nodes(index + 1)
            self.linked_nodes(left_node, right_node)
        self.len -= 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __index__(self, value: Any, start: int = 0, end: Optional[int] = None) -> int:
        """Метод находит первый индекс совпадения по введённому значению"""
        current_index = 0  # добавил из-за ошибки PEP8 ( работало и без)
        if not isinstance(start, int):
            raise TypeError()
        if start >= self.len:
            raise ValueError()
        if not isinstance(end, int):
            end = self.len
        for current_index in range(start, end):
            if self.__getitem__(current_index) == value:
                current_index = current_index  # добавил из-за ошибки PEP8 ( работало и без)
                break
        return current_index

    def count(self, value: Any, start: int = 0, end: Optional[int] = None) -> int:
        count = 0  # добавил из-за ошибки PEP8 ( была написана 111 строкой)
        if not isinstance(start, int):
            raise TypeError()
        if start >= self.len:
            raise ValueError()
        if not isinstance(end, int):
            end = self.len
        for current_index in range(start, end):
            if self.__getitem__(current_index) == value:
                count += 1
        return count

    def extend(self, iterable_obj: Iterable):
        if not isinstance(iterable_obj, Iterable):
            raise TypeError()
        for value in iterable_obj:
            self.append(value)


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"


if __name__ == '__main__':
    list_ = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    linked_list = LinkedList(list_)
    print(linked_list)
    linked_list.extend("str")
    print(linked_list)
    list_.extend("str")
    print(list_)

