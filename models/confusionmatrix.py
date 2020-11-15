#!/usr/bin/python3
# -*- coding: utf-8 -*-

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "nov/09/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class ConfusionMatrix:
    """This class represents the confusion matrix."""

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, matrix: list, classes: tuple) -> None:
        """Initializes the attributes matrix, classes, precision, recall, and
        accuracy."""
        self.__matrix = matrix
        self.__classes = tuple(classes)
        self.__precision = list()
        self.__recall = list()
        self.__accuracy = 0.0

    def __len__(self):
        """Returns the total number of columns or rows in the matrix."""
        return len(self.__classes)

    def __str__(self):
        """Method description  (DocString)"""
        aux_str = str(self.__classes)
        for i in range(self.__classes.__len__()):
            aux_str += '\n' + self.__classes[i] + str(self.__matrix[i]) +\
                       str(self.__precision[i])

        aux_str += '\n' + str(self.__recall) + str(self.__accuracy)
        return aux_str

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def matrix(self) -> list:
        """Returns the attribute matrix."""
        return self.__matrix

    @property
    def classes(self) -> tuple:
        """Returns the attribute classes."""
        return self.__classes

    @property
    def precision(self) -> list:
        """Returns the attribute precision."""
        return self.__precision

    @property
    def recall(self) -> list:
        """Returns the attribute recall."""
        return self.__recall

    @property
    def accuracy(self) -> float:
        """Returns the attribute accuracy."""
        return self.__accuracy

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    @matrix.setter
    def matrix(self, matrix: list):
        """Sets the attribute matrix."""
        self.__matrix = matrix

    @classes.setter
    def classes(self, classes: tuple):
        """Sets the attributes classes."""
        self.__classes = tuples(classes)

    # _________________________________Setters_________________________________

    # _____________________________Public methods______________________________

    def calculate_precision(self) -> None:
        """Calculate the value of precision."""
        self.__precision = list()
        i = 0

        for row in self.__matrix:
            sum = 0
            for j in row:
                sum += j
            self.__precision.append(row[i] / sum)
            i += 1

    def calculate_recall(self) -> None:
        """Calculates the value of recall."""
        self.__recall = list()

        for i in range(self.__classes.__len__()):
            sum = 0
            for j in range(self.__classes.__len__()):
                sum += self.__matrix[j][i]
            self.__recall.append(self.__matrix[i][i] / sum)

    def calculate_accuracy(self) -> None:
        """Calculates the value of accuracy."""
        numerator = 0
        denominator = 0
        i = 0
        for row in self.__matrix:
            numerator += row[i]
            i += 1
            for val in row:
                denominator += val

        self.__accuracy = numerator / denominator

    def calculate_all(self) -> None:
        """Calculates precision, recall, and accuracy values."""
        self.calculate_precision()
        self.calculate_recall()
        self.calculate_accuracy()

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class ConfusionMatrixError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________


if __name__ == "__main__":
    def confusion_matrix_test():
        """
        >>> data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> matrix = ConfusionMatrix(data, ("Yes", "No", "Sometimes"))

        >>> print(matrix.__len__())
        3
        >>> matrix.calculate_all()
        >>> print(matrix.precision)
        [0.16666666666666666, 0.3333333333333333, 0.375]
        >>> print(matrix.recall)
        [0.08333333333333333, 0.3333333333333333, 0.5]
        >>> print(matrix.accuracy)
        0.3333333333333333
        """
        pass

    import doctest
    doctest.testmod()