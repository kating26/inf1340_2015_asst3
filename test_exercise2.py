#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Hana Nagel, Liana Sukaisyan and Katherine Ing'
__email__ = "hana.nagel@mail.utoront.ca; liana.sukiasyan@mail.utoronto.ca; k.ing@mail.utoronto.ca"

__copyright__ = "2015 Hana Nagel, Liana Sukaisyan and Katherine Ing"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
import os
from exercise2 import decide

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]

