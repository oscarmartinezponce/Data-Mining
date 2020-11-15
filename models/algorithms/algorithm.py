#!/usr/bin/python3
# -*- coding: utf-8 -*-

from models.table import Table

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "nov/07/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class Algorithm:
    """This is an abstract class for algorithms used in data mining."""

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, table: Table) -> None:
        """Initializes the attribute table, and it sets the classes in the
        target attribute.
        The table attribute is the training set."""
        self._table = table

    def __str__(self):
        """This is a method overrides."""
        return "Override"

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def table(self) -> Table:
        """Returns the attribute table."""
        return self._table

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    @table.setter
    def table(self, table: Table):
        """Sets the attribute table."""
        self._table = table

    # _________________________________Setters_________________________________

    # _____________________________Private methods_____________________________

    # _____________________________Private methods_____________________________

    def predict(self, table: Table) -> list:
        """This is a method overrides."""
        return list()

    # _____________________________Public methods______________________________

    '''def public_method(self):
        """Method description (DocString)
        >>> 2 + 3
        5
        """
        pass'''

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class AlgorithmError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________


if __name__ == "__main__":
    def algorithm_test():
        """
        >>> header = {"Play": Table._nominal, "Temperature": Table._numeric}
        >>> data = [["Yes", 30], ["No", 32]]
        >>> table = Table(data, header, 0)
        >>> algorithm = Algorithm(table)

        >>> print(algorithm.table)
        ['Play', 'Temperature']
        ['Nominal', 'Numeric']
        ['Yes', 30]
        ['No', 32]
        <BLANKLINE>

        >>> data_1 = [["Yes", 30], ["No", 32], ['No', 31]]
        >>> algorithm.table.data = data_1
        >>> print(algorithm.table)
        ['Play', 'Temperature']
        ['Nominal', 'Numeric']
        ['Yes', 30]
        ['No', 32]
        ['No', 31]
        <BLANKLINE>

        >>> print(algorithm.predict([]))
        []
        """

    import doctest
    doctest.testmod()
