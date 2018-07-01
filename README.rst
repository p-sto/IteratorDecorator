.. image:: https://travis-ci.org/stovorov/IteratorDecorator.svg?branch=master
    :target: https://travis-ci.org/stovorov/IteratorDecorator

.. image:: https://codecov.io/gh/stovorov/IteratorDecorator/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/stovorov/IteratorDecorator

IteratorDecorator
=================

Implementing iterator in Python is nothing complicated though what's missing is possibility to make it even
easier. This small library adds ``iter_attribute`` decorator allowing to quickly choose iterable for which
iterator would be implemented.

Requirements
------------

    Python3.5+


Example
-------

.. code:: python


    from IteratorDecorator import iter_attribute


    @iter_attribute('number')
    class CaseClass:
        def __init__(self):
            self.number = [1, 2, 3, 4]
            self.attr = ['attr1', 'attr2', 'attr3']

    obj = CaseClass()

    for num in obj:
        print(num)


Installing
----------

In your virtualenv just call:

::

    $ pip install IteratorDecorator


Warning
-------

When using PyCharm or MYPY you'll probably see issues with decorated class not being recognized as Iterator.
That's an issue which I could not overcome yet, it's probably due to the fact that interpretation of object
is being done statically rather than dynamically. MYPY checks for definition of methods in class code which
changes at runtime. Since ``__iter__`` and ``__next__`` are added dynamically MYPY cannot find those
defined in objects before object of a class is created. Possible workarounds for this issue are:

1. Define ``__iter__`` method in class:

.. code:: python

    @iter_attribute('attr')
    class Test:
        def __init__(self) -> None:
            self.attr = [1, 2, 3]

        def __iter__(self) -> 'Test':
            return self

Actually it does not have to be "real" ``__iter__`` since it'll be replaced by decorator implementation, but
the definition is only needed for static checkers.


2. After creating object use cast or assert function denoting that particular instance inherits

.. code:: python

    from collections.Iterator:

    assert isinstance(my_object, collections.Iterator)
