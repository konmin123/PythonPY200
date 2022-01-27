from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (type(None), cls)):
            raise TypeError


class Dln(Node):
    """Класс, который описывает узел двусвязанного списка."""
    def __init__(self, value: Any, prev: Optional["Dln"] = None, next_: Optional["Dln"] = None):
        super().__init__(value, next_)
        self._prev = prev

    def __repr__(self) -> str:
        next_ = None if self.next is None else f"Dln({repr(self.next.value)})"
        prev = None if self._prev is None else f"Dln({repr(self._prev.value)})"
        return f"Dln({repr(self.value)}, {prev}, {next_})"

