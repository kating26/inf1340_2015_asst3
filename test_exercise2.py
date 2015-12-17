#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Hana Nagel, Liana Sukaisyan and Katherine Ing'
__email__ = "hana.nagel@mail.utoronto.ca; liana.sukiasyan@mail.utoronto.ca; k.ing@mail.utoronto.ca"
__copyright__ = "2015 Hana Nagel, Liana Sukaisyan and Katherine Ing"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
import os
from exercise2 import *

#DIR = "test_jsons/"
#os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ['Reject', 'Reject', 'Reject', 'Reject', 'Accept', 'Reject', 'Reject', 'Reject']

######################
# MAIN FUNCTIONS #
######################

# Accept

# Reject

# Quarantine


def test_valid_passport_formatt():
    """
    Tests whether a passport number is five sets of five alpha-number characters separated by dashes
    """
    assert (valid_passport_format('KG65G-239FM-3D9G3-4K4R3-3LFK3')) == True
    assert (valid_passport_format('kg65G-239fM-3D9G3-4k4R3-3lFK3')) == True
    assert (valid_passport_format('')) == False
    assert (valid_passport_format('@#$$#-@$#$3-@$#$@-@#$@$-^%$^%')) == False
    assert (valid_passport_format('KDSJ-SKJF3-SK234-DK12')) == False
    assert (valid_passport_format('416-444-4444')) == False
    assert (valid_passport_format('KG65G_239FM_3D9G3_DK4R3_3LFK3')) == False
    assert (valid_passport_format('1-2-3-4-5')) == False
    assert (valid_passport_format('a-b-c-d-e')) == False
    assert (valid_passport_format('!-!-!-!-!')) == False
    assert (valid_passport_format('happy')) == False

def test_valid_visa_format():
    """
    Tests whether a visa code is two groups of five alphanumeric characters
    """
    assert (valid_visa_format('ABCD1-ABCD5')) == True
    assert (valid_visa_format('abCD1-ABcd5')) == True
    assert (valid_visa_format('abcd1-abcd5')) == True
    assert (valid_visa_format('')) == False
    assert (valid_visa_format('!! !!')) == False
    assert (valid_visa_format('123123123123')) == False
    assert (valid_visa_format('abcabcabcabc')) == False
    assert (valid_visa_format('a1b2c3d4e5f6'))  == False
    assert (valid_visa_format('1234 abcd')) == False
    assert (valid_visa_format('12345 abcde')) == False
    assert (valid_visa_format('12ab3 abcd4')) == False
    assert (valid_visa_format('abc12 123ab')) == False


def test_valid_date_format():
    """
    Tests whether a date has the format YYYY-mm-dd in numbers
    """
    assert (valid_date_format('1967-30-04')) == True
    assert (valid_date_format('2016-30-04')) == True
    assert (valid_date_format('April 30, 2020')) == False
    assert (valid_date_format('')) == False
    assert (valid_date_format("Happy!")) == False
    assert (valid_date_format('13-13-13')) == False
    assert (valid_date_format('30-04-1967')) == False
    assert (valid_date_format('1967.30.04')) == False
    assert (valid_date_format('1967/30/04')) == False
    assert (valid_date_format('-7/+7/*7')) == False


def test_valid_visitor():
    result = [["passport", "first_name", "last_name", "birth_date"],
              ["JMZ0S-89IA9-OTCLY-MQILJ-P7CTY", "ELIZABETH", "WENDT", "1958-08-22"],
              ["I7LWE-N5O9P-HDNAG-1JGF1-WR44S", "VENITA", "CULP", "1936-03-25"]]
