#!/usr/bin/python3
# -*- coding: utf-8 -*-

from models.table import Table
from models.algorithms.algorithm import Algorithm

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "nov/07/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class ZeroR(Algorithm):
    """This class has the method Zero-r."""

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, table: Table) -> None:
        """Initializes the attribute rule."""
        super().__init__(table)
        self.__rule = None

    def __str__(self):
        """Returns the rule in str"""
        return self.__rule


    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def rule(self) -> str:
        """Returns the attribute rule."""
        return self.__rule

    # _________________________________Getters_________________________________

    # _____________________________Public methods______________________________

    def run(self) -> None:
        """Calculates the rule to predict."""
        # Calculates the frequency of classes
        classes = dict()
        col_target = self._table.target
        for i in self._table.data:
            if classes.get(i[col_target]):
                classes[i[col_target]] += 1
            else:
                classes[i[col_target]] = 1
        #

        # Sets the class more frequently
        max_val = 0
        max_class = None
        for c in classes.keys():
            if classes[c] > max_val:
                max_class = c
                max_val = classes[c]

        self.__rule = max_class
        #

    def predict(self, table: Table) -> list:
        """Uses the data set in the table to predict based on the rule, and
        returns a list with the predictions.
        The table parameter is the test set."""
        aux_list = list()
        for i in range(table.__len__()):
            aux_list.append(self.__rule)
        return aux_list

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class ZeroRError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________


if __name__ == "__main__":
    def zeror_test():
        """
        >>> header = {"Play": Table._nominal, "Temperature": Table._numeric}
        >>> data = [["Si", 30], ["No", 32], ["No", 40], ["Si", 20], ["Si", 21], ["No", 32], ["No", 40]]
        >>> table = Table(data, header, 0)
        >>> zero = ZeroR(table)

        >>> zero.run()
        >>> print(zero.rule)
        No
        >>> print(zero)
        No

        >>> zero.predict(table)
        ['No', 'No', 'No', 'No', 'No', 'No', 'No']
        """

    import doctest
    doctest.testmod()
