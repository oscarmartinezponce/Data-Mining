#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import choice
from math import sqrt
from models.table import Table
from models.algorithms.algorithm import Algorithm

__email__ = "oscar07112009@hotmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martínez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "nov/13/2020"

__author__ = "Oscar Martínez"

__credits__ = "UDG"


class KMeans(Algorithm):
    """This class has the method K-means."""

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, table: Table, min_k: int, max_k: int, i: int=None, r: int=1, unsupervised: bool=True) -> None:
        """Initializes the attributes table,
        min_k: minimum of clusters,
        max_k: maximum of clusters,
        i: stop condition,
        r: re-runs.
        """
        super().__init__(table)
        self.__min_k = min_k
        self.__max_k = max_k
        self.__k = max_k
        self.__i = i
        self.__r = r
        self.__unsupervised = unsupervised
        self.__error = None
        self.__clusters = list()
        self.__aux_centroids = list()
        self.__centroids = list()
        self.__set_k()

    def __str__(self):
        """Returns a string with the centroids."""
        aux_str = ''
        data = self.table.data
        if self.clusters.__len__() > 0:
            for i in range(data.__len__()):
                aux_str += str(data[i]) + ' ' +str(self.clusters[i]) + '\n'
        return aux_str

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def unsupervised(self) -> bool:
        """Returns the attribute unsupervised."""
        return self.__unsupervised

    @property
    def min_k(self) -> int:
        """Returns the attribute min_k."""
        return self.__min_k

    @property
    def max_k(self) -> int:
        """Returns the attribute max_k."""
        return self.__max_k

    @property
    def i(self) -> int:
        """Returns the attribute i."""
        return self.__i

    @property
    def r(self) -> int:
        """Returns the attribute r."""
        return self.__r

    @property
    def error(self) -> float:
        """Returns the attribute error."""
        return self.__error

    @property
    def clusters(self) -> list:
        """Returns the attribute clusters."""
        return self.__clusters

    @property
    def centroids(self) -> list:
        """Returns the attribute rule."""
        return self.__centroids

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    @unsupervised.setter
    def unsupervised(self, unsupervised: bool) -> None:
        """Sets the attribute unsupervised."""
        self.__unsupervised = unsupervised

    @min_k.setter
    def min_k(self, min_k: int) -> None:
        """Sets the attribute min_k."""
        self.__min_k = min_k

    @max_k.setter
    def max_k(self, max_k: int) -> None:
        """Sets the attribute max_k."""
        self.__max_k = max_k

    @i.setter
    def i(self, i: int) -> None:
        """Sets the attribute i."""
        self.__i = i

    @r.setter
    def r(self, r: int) -> None:
        """Sets the attribute r."""
        self.__r = r

    # _________________________________Getters_________________________________

    # _____________________________Public methods______________________________

    def run(self) -> None:
        """Calculates the centroids to predict."""
        for i in range(self.__r):
            self.__re_run()
            self.__set_k()

    def predict(self, table: Table) -> list:
        """Uses the data set in the table to predict based on the rule, and"""
        pass

    # _____________________________Public methods______________________________

    # _____________________________Private methods_____________________________

    def __set_k(self) -> None:
        """Sets the attribute k and it selects the centroids."""
        if self.__k + 1 > self.__max_k:
            self.__k = self.__min_k
        else:
            self.__k += 1
        self.__aux_centroids = list()
        for i in range(self.__k):
            self.__aux_centroids.append(choice(self.table.data).copy())

    def __re_run(self) -> None:
        """This is a re-run, it has self.__re_runs."""
        aux_error = None
        aux_select_clusters = list()
        select_clusters, error = self.__iteration_run()
        i = 0

        while aux_select_clusters != select_clusters and (self.__i == None or i < self.__i):
            self.__set_mean_centroids(select_clusters)
            if aux_error == None or error < aux_error:
                aux_error = error
                aux_select_clusters = select_clusters.copy()

            select_clusters, error = self.__iteration_run()
            i += 1

        if aux_error == None or error < aux_error:
            aux_error = error
            aux_select_clusters = select_clusters.copy()

        if self.__error == None or aux_error < self.__error:
            self.__error = aux_error
            self.__clusters = aux_select_clusters
            self.__centroids = self.__aux_centroids

    def __iteration_run(self) -> tuple:
        """This is one iteration of the algorithm run."""
        select_cluster = list()
        for r in self.table.data:
            self.__select_cluster(r, select_cluster)

        return select_cluster, self.__fun_error(select_cluster)

    def __set_mean_centroids(self, clusters: list) -> None:
        """Computes the mean of the centroids and updates them."""
        data = self._table.data
        rows = data.__len__()
        columns = data[0].__len__()
        target = self.table.target
        means = list()
        for i in range(self.__aux_centroids.__len__()):
            means.append([0] * columns)

        for j in range(columns): # Calculates the sum
            if not (j == target and self.__unsupervised):
                for i in range(rows):
                    means[clusters[i]][j] += data[i][j]

        for i in range(means.__len__()): # Calculates the average
            count = clusters.count(i)
            for j in range(columns):
                if not(j == target and self.__unsupervised) and count != 0:
                    means[i][j] /= count

        self.__aux_centroids = means

    def __select_cluster(self, record: list, clusters: list) -> None:
        """Receives a record and selects the closest cluster."""
        cluster = 0
        min = None
        target = self.table.target
        for i in range(self.__aux_centroids.__len__()):
            accum = 0
            for j in range(record.__len__()):
                if not(j == target and self.__unsupervised):
                    accum += (record[j] - self.__aux_centroids[i][j]) ** 2

            if min == None or accum < min:
                min = accum
                cluster = i

        clusters.append(cluster)

    def __fun_error(self, clusters: list) -> float:
        """Returns the total error."""
        error = 0
        data = self._table.data
        len = data[0].__len__()
        target = self.table.target

        for i in range(data.__len__()):
            aux_error = 0
            for j in range(len):
                if not (j == target and self.__unsupervised):
                    aux_error += (data[i][j] - self.__aux_centroids[clusters[i]][j]) ** 2
            error += sqrt(aux_error)
        return error

    # _____________________________Private methods_____________________________

    # ______________________________Inner classes______________________________

    class OneRError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________


if __name__ == "__main__":
    def k_means_test():
        """
        >>> header = {"var1": Table._numeric, "var2": Table._numeric, "var3": Table._numeric, \
          "var4": Table._numeric, "var5": Table._numeric, "class": Table._nominal}
        >>> data = data = [ \
        [7,	8,	4,	5,	2, ''], [6,	8,	5,	4,	2, ''], [8,	9,	7,	8,	9, ''], \
        [6,	7,	7,	7,	8, ''], [1,	2,	5,	3,	4, ''], [3,	4,	5,	3,	5, ''], \
        [7,	8,	8,	6,	6, ''], [8,	9,	6,	5,	5, ''], [2,	3,	5,	6,	5, ''], \
        [1,	2,	4,	4,	2, ''], [3,	2,	6,	5,	7, ''], [2,	5,	6,	8,	9, ''], \
        [3,	5,	4,	6,	3, ''], [3,	5,	5,	6,	3, '']]
        >>> table = Table(data, header, 5)
        >>> means = KMeans(table, 2, 5, 50, 20, False)

        >>> print(means.unsupervised)
        False
        >>> print(means.min_k)
        2
        >>> print(means.max_k)
        5
        >>> print(means.i)
        50
        >>> print(means.r)
        20
        >>> print(means.error)
        None
        >>> print(means.clusters)
        []
        >>> print(means.centroids.__len__())
        0

        >>> means.unsupervised = True
        >>> means.min_k = 3
        >>> means.max_k = 4
        >>> means.i = 40
        >>> means.r = 25

        >>> print(means.unsupervised)
        True
        >>> print(means.min_k)
        3
        >>> print(means.max_k)
        4
        >>> print(means.i)
        40
        >>> print(means.r)
        25

        >>> print(means)
        <BLANKLINE>

        >>> means.run()
        >>> print(means.clusters.__len__())
        14
        """
    import doctest
    doctest.testmod()
