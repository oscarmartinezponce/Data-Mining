#!/usr/bin/python3
# -*- coding: utf-8 -*-

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "nov/07/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class Table:
    """This class represents a table, It has header and data"""

    # ____________________________Class attributes_____________________________

    _boolean = "Boolean"
    _numeric = "Numeric"
    _nominal = "Nominal"
    _ordinal = "Ordinal"

    # ____________________________Class attributes_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, data: list=[], header: dict={}, target: int=0) -> None:
        """Initializes the attributes data and header.
        Data is a list of list, and the header is a dictionary {name: type}"""
        self.__data = data
        self.__header = header
        self.__target = target
        self.__classes = set()
        self.__set_classes()

    def __len__(self) -> int:
        """Returns the number of records the table has."""
        return len(self.__data)

    def __str__(self) -> str:
        """Returns a string with the header and data."""
        aux_str = str(list(self.__header.keys())) + "\n"
        aux_str += str(list(self.__header.values())) + "\n"
        for i in self.__data:
            aux_str += str(i) + "\n"

        return aux_str

    # _____________________________Generic methods_____________________________

    # ____________________________Arithmetic methods___________________________

    def __add__(self, other):
        """Joins the lists and returns a new Table object with the attributes
        of the first table"""
        return Table(self.__data + other.__data, self.__header, self.__target)

    # ____________________________Arithmetic methods___________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def data(self) -> list:
        """Returns the attribute data."""
        return self.__data

    @property
    def header(self) -> dict:
        """Returns the attribute header."""
        return self.__header

    @property
    def attributes(self) -> list:
        """Returns a list with the name of the attributes."""
        return list(self.__header.keys())

    @property
    def types(self) -> list:
        """Returns a list with the type of the attributes."""
        return list(self.__header.values())

    @property
    def target(self) -> int:
        """Returns the column number of the target."""
        return self.__target

    @property
    def classes(self) -> set:
        """Returns the attribute classes"""
        return self.__classes

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    @data.setter
    def data(self, data: list) -> None:
        """Sets the attribute data."""
        self.__data = data
        self.__set_classes()

    @header.setter
    def header(self, header: dict) -> None:
        """Sets the attribute header."""
        self.__header = header

    @target.setter
    def target(self, target: int) -> None:
        """Sets the attribute target."""
        self.__target = target

    # _________________________________Setters_________________________________

    # _____________________________Public methods______________________________

    def insert(self, record: list) -> None:
        """Inserts a record in the data."""
        self.__classes.add(record[self.__target])
        self.__data.append(record)

    # _____________________________Public methods______________________________

    # _____________________________Private methods_____________________________

    def __set_classes(self):
        """Finds all the classes in the target attribute."""
        self.__classes = set()
        for i in self.__data:
            self.__classes.add(i[self.__target])

    # _____________________________Private methods_____________________________

    # ______________________________Inner classes______________________________

    class TableError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________


if __name__ == "__main__":
    def table_test():
        """
        >>> header = {"Play": Table._nominal, "Temperature": Table._numeric}
        >>> data = [["Yes", 30], ["No", 32], ["No", 40], ["Yes", 20]]

        >>> table = Table(data, header, 0)
        >>> table.target = 0

        >>> table.insert(["Yes", 35])

        >>> print(table.__len__())
        5
        >>> print(table.target)
        0
        >>> print(table)
        ['Play', 'Temperature']
        ['Nominal', 'Numeric']
        ['Yes', 30]
        ['No', 32]
        ['No', 40]
        ['Yes', 20]
        ['Yes', 35]
        <BLANKLINE>

        >>> table_2 = Table()
        >>> table_2.header = {'Work': Table._nominal, 'Score': Table._ordinal}
        >>> table_2.data = [["Yes", 'A'], ["No", 'E']]

        >>> print(table_2.header)
        {'Work': 'Nominal', 'Score': 'Ordinal'}
        >>> print(table_2.data)
        [['Yes', 'A'], ['No', 'E']]
        >>> print(table_2.attributes)
        ['Work', 'Score']
        >>> print(table_2.types)
        ['Nominal', 'Ordinal']
        >>> print(table_2.classes.difference({'No', 'Yes'}))
        set()

        >>> print(table + table_2)
        ['Play', 'Temperature']
        ['Nominal', 'Numeric']
        ['Yes', 30]
        ['No', 32]
        ['No', 40]
        ['Yes', 20]
        ['Yes', 35]
        ['Yes', 'A']
        ['No', 'E']
        <BLANKLINE>
        """
        pass

    import doctest
    doctest.testmod()
