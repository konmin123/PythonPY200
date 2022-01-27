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
        self._next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self._next is None else f"Node({self.value}, Node({self._next}))"

    def __str__(self) -> str:
        return str(self.value)


class Dln(Node):
    """Класс, который описывает узел двусвязанного списка."""
    def __init__(self, value: Any, prev: Optional["Dln"] = None, next_: Optional["Dln"] = None):
        super().__init__(value, next_)
        self._prev = None

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        if not isinstance(prev, (type(None), Dln)):
            raise TypeError
        self._prev = prev

    def __repr__(self) -> str:
        next_ = None if self._next is None else f"Dln({repr(self._next.value)})"
        prev = None if self._prev is None else f"Dln({repr(self._prev.value)})"
        return f"Dln({repr(self.value)}, {prev}, {next_})"


