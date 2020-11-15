#!/usr/bin/python3
# -*- coding: utf-8 -*-

from models.table import Table
from models.algorithms.algorithm import Algorithm

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "nov/09/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class OneR(Algorithm):
    """This class has the method One-r."""

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, table: Table) -> None:
        """Initializes the attribute rule."""
        super().__init__(table)
        self.__index = None
        self.__rules = None

    def __str__(self):
        """Returns a string with the rules."""
        aux_str = ''
        for k in self.__rules.keys():
            aux_str += k + ' --> ' + self.__rules[k] + '\n'
        return aux_str

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def index(self) -> dict:
        """Returns the attribute index."""
        return self.__index

    @property
    def rules(self) -> dict:
        """Returns the attribute rule."""
        return self.__rules

    # _________________________________Getters_________________________________

    # _____________________________Public methods______________________________

    def run(self) -> None:
        """Calculates the rules to predict."""
        aux_errors = None
        table = self.table
        target = table.target

        for j in range(table.data[0].__len__()):
            if j == table.target:
                continue

            frequency_classes = dict()
            for c in self.table.classes:  # Adds the classes in the dictionary
                frequency_classes[c] = {}

            # Calculates the frequency of classes
            for i in range(table.__len__()):
                if frequency_classes[table.data[i][target]].get(table.data[i][j]):
                    frequency_classes[table.data[i][target]][table.data[i][j]] += 1
                else:
                    if frequency_classes[table.data[i][target]]:
                        frequency_classes[table.data[i][target]][table.data[i][j]] = 1
                    else:
                        frequency_classes[table.data[i][target]] = {table.data[i][j]: 1}
            #

            # Determines the rules to be used
            errors = 0
            rules = {}
            aux_max = {}

            for d in frequency_classes.keys():
                for c in frequency_classes[d].keys():
                    if rules.get(c):
                        if aux_max[c] < frequency_classes[d][c]:
                            rules[c] = d
                            errors += aux_max[c]
                            aux_max[c] = frequency_classes[d][c]
                        else:
                            errors += frequency_classes[d][c]
                    else:
                        rules[c] = d
                        aux_max[c] = frequency_classes[d][c]


            if aux_errors == None or errors < aux_errors:
                self.__rules = rules
                self.__index = j
                aux_errors = errors
            #

        #

    def predict(self, table: Table) -> list:
        """Uses the data set in the table to predict based on the rule, and
        returns a list with the predictions.
        The table parameter is the test set."""
        aux_list = list()
        for i in table.data:
            aux_list.append(self.rules[i[self.__index]])
        return aux_list

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class OneRError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________


if __name__ == "__main__":
    def oner_test():
        """
        >>> header = {"Purchase": Table._nominal, "Maintenance": Table._nominal, \
        "Doors": Table._ordinal, "People": Table._nominal, "Class": Table._nominal}
        >>> data = [['vhigh', 'med', '3', '4', 'acc'], \
                    ['vhigh', 'med', '4', '4', 'acc'], \
                    ['vhigh', 'vhigh', '3', '2', 'unacc'], \
                    ['vhigh', 'vhigh', '2', '4', 'unacc'], \
                    ['med', 'low', '2', 'more', 'good'], \
                    ['med', 'low', '2', '4', 'good'], \
                    ['vhigh', 'vhigh', '4', 'more', 'unacc'], \
                    ['vhigh', 'vhigh', '2', '4', 'unacc'], \
                    ['vhigh', 'med', '3', '4', 'acc'], \
                    ['low', 'low', '4', '4', 'good'], \
                    ['vhigh', 'med', '2', 'more', 'acc'], \
                    ['low', 'low', '4', 'more', 'good'], \
                    ['vhigh', 'vhigh', '3', '2', 'unacc'], \
                    ['low', 'low', '4', 'more', 'good'], \
                    ['med', 'low', '3', 'more', 'good']]
        >>> table = Table(data, header, 4)
        >>> one = OneR(table)

        >>> one.run()
        >>> print(one.index)
        1
        >>> print(one.rules['med'])
        acc
        >>> print(one.rules['vhigh'])
        unacc
        >>> print(one.rules['low'])
        good

        >>> one.predict(table)
        ['acc', 'acc', 'unacc', 'unacc', 'good', 'good', 'unacc', 'unacc', 'acc', 'good', 'acc', 'good', 'unacc', 'good', 'good']
        """
    import doctest
    doctest.testmod()
