"""Test of source file"""
import collections

from IteratorDecorator import iter_attribute


@iter_attribute('number')
class CaseClass:
    def __init__(self):
        self.number = [1, 2, 3, 4]
        self.attr = ['attr1', 'attr2', 'attr3']

    def __iter__(self):
        pass


def test_iterator():
    tested = CaseClass()
    res = []
    for elmn in tested:
        res.append(elmn)

    assert res == [1, 2, 3, 4]
    assert isinstance(tested, collections.Iterator)
