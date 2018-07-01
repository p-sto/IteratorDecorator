"""Iterator attribute module"""

import collections
import inspect
from typing import Any, Union, Iterable, Callable


def iter_attribute(iterable_name) -> Union[Iterable, Callable]:
    """Decorator implementing Iterator interface with nicer manner.

    Example
    -------

    @iter_attribute('my_attr'):
    class DecoratedClass:
        ...

    Warning:
    ========

    When using PyCharm or MYPY you'll probably see issues with decorated class not being recognized as Iterator.
    That's an issue which I could not overcome yet, it's probably due to the fact that interpretation of object
    is being done statically rather than dynamically. MYPY checks for definition of methods in class code which
    changes at runtime. Since __iter__ and __next__ are added dynamically MYPY cannot find those
    defined in objects before object of a class is created. Possible workarounds for this issue are:

        1. Define ``dummy`` __iter__ class like:

            @iter_attribute('attr')
            class Test:
                def __init__(self) -> None:
                    self.attr = [1, 2, 3]

                def __iter__(self):
                    pass

        2. After creating object use cast or assert function denoting that particular instance inherits
            from collections.Iterator:

            assert isinstance(my_object, collections.Iterator)


    :param iterable_name: string representing attribute name which has to be iterated
    :return: DecoratedClass with implemented '__iter__' and '__next__' methods.
    """

    def create_new_class(decorated_class) -> Union[Iterable, Callable]:
        """Class extender implementing __next__ and __iter__ methods.

        :param decorated_class: class to be extended with iterator interface
        :return: new class
        """
        assert inspect.isclass(decorated_class), 'You can only decorate class objects!'
        assert isinstance(iterable_name, str), 'Please provide attribute name string'

        decorated_class.iterator_attr_index = 0

        def __iter__(instance) -> Iterable:
            """Implement __iter__ method

            :param instance: __iter__ uses instance of class which is being extended
            :return: instance of decorated_class
            """
            return instance

        def __next__(instance) -> Any:
            """Implement __next__ method

            :param instance: __next__ uses instance of class which is being extended
            :return: instance of decorated_class
            """
            assert hasattr(instance, iterable_name), \
                'Decorated object does not have attribute named {}'.format(iterable_name)
            assert isinstance(getattr(instance, iterable_name), collections.Iterable), \
                '{} of object {} is not iterable'.format(iterable_name, instance.__class__.__name__)
            ind = instance.iterator_attr_index
            while ind < len(getattr(instance, iterable_name)):
                val = getattr(instance, iterable_name)[ind]
                instance.iterator_attr_index += 1
                return val
            raise StopIteration

        dct = dict(decorated_class.__dict__)
        dct['__iter__'] = __iter__
        dct['__next__'] = __next__
        dct['iterator_attr_index'] = decorated_class.iterator_attr_index
        return type(decorated_class.__name__, (collections.Iterable,), dct)

    return create_new_class
