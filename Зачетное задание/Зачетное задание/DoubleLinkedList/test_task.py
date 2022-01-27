import unittest

from task import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_del_first_node(self):
        ll = LinkedList([1, 2, 3])

        del ll[0]

        self.assertEqual(2, ll.len, msg="Не правильная длина результирующего списка")

        self.assertEqual("[2, 3]", str(ll))
