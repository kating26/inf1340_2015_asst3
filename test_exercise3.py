#!/usr/bin/env python

""" Assignment 3, Exercise 1, INF1340, Fall, 2015. DBMS
Test module for exercise3.py
"""

__author__ = 'Hana Nagel, Liana Sukaisyan and Katherine Ing'
__email__ = "hana.nagel@mail.utoront.ca; liana.sukiasyan@mail.utoronto.ca; k.ing@mail.utoronto.ca"
__copyright__ = "2015 Hana Nagel, Liana Sukaisyan and Katherine Ing"
__license__ = "MIT License"

from exercise1 import selection, projection, cross_product


###########
# TABLES ##
###########

STUDENTS = [["Surname", "FirstName", "Age", "Tuition"],
             ["Xio", "Anna", 24, 22000],
             ["Black", "Lucy", 28, 35000],
             ["Sara", "Maria", 36, 45000],
             ["Smith", "Mark", 29, 39000]]
             

R1 = [["Student", "Department"],
      ["Xio", "iSchool"],
      ["Black", "Rotman"],
      ["White", "Rotman"]]

R2 = [["Department", "Head"],
      ["Rotman", "Mori"],
      ["iSchool", "Brown"]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):

    t1.sort()
    t2.sort()

    return t1 == t2


#####################
# FILTER FUNCTIONS ##
#####################
def filter_students(row):
    """
    Check if student represented by row
    is AT LEAST 30 years old and pays MORE THAN
    34000 for tuition.
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Tuition}]
    :return: True if the row satisfies the condition.
    """
    return row[-2] >= 25 and row[-1] > 34000


###################
# TEST FUNCTIONS ##
###################

def test_selection():
    """
    Test selection operation.
    """

    result = [["Surname", "FirstName", "Age", "Tuition"],
             ["Black", "Lucy", 28, 35000],
             ["Sara", "Maria", 36, 45000],
             ["Smith", "Mark", 29, 39000]]
    assert is_equal(result, selection(STUDENTS, filter_students))


def test_projection():
    """
    Test projection operation.
    """

    result = [["Surname", "FirstName"],
              ["Xio", "Anna"],
              ["Black", "Lucy"],
              ["Sara", "Maria"],
              ["Smith", "Mark"]]
         
    assert is_equal(result, projection(STUDENTS, ["Surname", "FirstName"]))


def test_cross_product():
    """
    Test cross product operation.
    """

    result = [["Student", "Department", "Department", "Head"],
              ["Xio", "iSchool", "Rotman", "Mori"],
              ["Xio", "iSchool", "iSchool", "Brown"],
              ["Black", "Rotman", "Rotman", "Mori"],
              ["Black", "Rotman", "iSchool", "Brown"],
              ["White", "Rotman", "Rotman", "Mori"],
              ["White", "Rotman", "iSchool", "Brown"]]
              
    assert is_equal(result, cross_product(R1, R2))
