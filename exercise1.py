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


def selection(table, function):
    """
    Perform select operation on table t that satisfy condition f.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]

    """
#Probable solution for selection
    new_table = []
    new_table.append(table[0])
    for a in xrange(1, len(table)):
        if function(table[a]):
            new_table.append(table[a])
    return new_table


#From Assignment 2
def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    new_table = []

    # Schema match check:
    if table1[0] == table2[0]:
        # Append header row
        new_table.append(table1[0])

        # Matching table1 rows to table2
        for t1_row in table1[1:]:
            if t1_row not in table2 or t1_row not in new_table:
                new_table.append(t1_row)

        # Matching table2 rows to table1
        for t2_row in table2[1:]:
            if t2_row not in table1 or t2_row not in new_table:
                new_table.append(t2_row)
    else:
        raise MismatchedAttributesException("Bad Schema.")

    # 2015-11-06 update: if no common rows, should return nothing
    if len(new_table) < 2:
        # new_table = []
        return None

    return new_table
# End of Assignment 2

# Work from inforum
t = EMPLOYEES = [["Surname", "FirstName", "Age", "Salary"],
             ["Smith", "Mary", 25, 2000],
             ["Black", "Lucy", 40, 3000],
             ["Verdi", "Nico", 36, 4500],
             ["Smith", "Mark", 40, 3900]]
# Define function f that returns True iff the last element in the row is greater than 30.
def f(row): row[-1] > 30
select(row, f)
[["Surname", "FirstName", "Age", "Salary"]]

def selection (t, f):
    f = {}
    result = []
    for row in t:
        if tuple(row) not in f:
            result.append(row)
            d[tuple(row)] = True

        return result

selection(t, f)
#end of work from inforum
def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """

    return []


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]


    """

    return []

