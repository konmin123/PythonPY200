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
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class Dln(Node):
    """Класс, который описывает узел двусвязанного списка."""
    def __init__(self, value: Any, next_: Optional["Dln"] = None, prev: Optional["Dln"] = None):
        super().__init__(value, next_)
        self._prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["Dln"]):
        self.is_valid(prev)
        self._prev = prev

    def is_valid(self, dln: Any):
        if not isinstance(dln, (type(None), Dln)):
            raise TypeError()

    def __repr__(self) -> str:
        next_ = None if self.next is None else f"Dln({self.next.value})"
        prev_ = None if self.prev is None else f"Dln({self.prev.value})"
        return f"Dln({self.value}, {prev_}, {next_})"


dln1 = Dln(5)
dln2 = Dln(7)
dln3 = Dln(9)

dln1.next = dln2
dln2.next = dln3

dln3.prev = dln2
dln2.prev = dln1

print(repr(dln2))
print(dln2)
