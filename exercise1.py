#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Hana Nagel, Liana Sukaisyan and Katherine Ing'
__email__ = "hana.nagel@mail.utoront.ca; liana.sukiasyan@mail.utoronto.ca; k.ing@mail.utoronto.ca "
__copyright__ = "2015 Hana Nagel, Liana Sukaisyan and Katherine Ing"
__license__ = "MIT License"

#####################
# HELPER FUNCTIONS ##
#####################

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def selection(t, f):
    """
    Perform select operation on table t that satisfy condition f.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True if
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]

    """

    new_table = []
    new_table.append(t[0])
    for a in xrange(1, len(t)):
        if f(t[a]):
            new_table.append(t[a])
    return new_table


def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """
    projection_table = []
    new_table = []
    for a in xrange(len(t[0])):
        for n in xrange(len(r)):
            if r[n] == t[0][a]:
                projection_table.append(a)
    for x in xrange(len(t)):
        new_table.append([t[x][index] for index in projection_table])
    return new_table
    

def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]


    """
    new_table = []
    for n in xrange(1, len(t1)):
        for a in xrange(1, len(t2)):
            new_table.append(t1[n]+t2[a])
    new_table.insert(0, t1[0] + t2[0])
    return new_table

