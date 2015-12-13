#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia
Computer-based immigration office for Kanadia
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import re
import datetime
import json

######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
## global variables ##
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''
COUNTRIES = None


"""
importing and making json files readable, naming different parts so that different functions can access them
"""

with open("test_jsons/test_returning_citizen.json", "r") as file_reader:
    file_contents = file_reader.read()
    json_citizens = json.loads(file_contents)
with open("test_jsons/countries.json", "r") as file_reader2:
    file_contents2 = file_reader2.read()
    json_countries = json.loads(file_contents2)

#print json.dumps(json_citizens, indent=1)
#print json.dumps(json_countries, indent=1)



incoming_foreigners = "test_jsons/test_incoming_foreigner.json"

"""
WRITING TO JSON FILES
# to overwrite the existing "test_incoming_foreigner.json" file:
with open(incoming_foreigners, "w") as output:
    json.dump(VISA_HAVERS, output, sort_keys=True, indent=1)
with open(incoming_foreigners[0], mode='w') as feeds:
    for item in VISA_HAVERS:
        json.dump(item, feeds, sort_keys=True, indent=1)
"""

#####################
# HELPER FUNCTIONS ##
#####################
def is_more_than_x_years_ago(x, date_string):
    """
    Checks if date is less than x years ago.
    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() > 0

def decide(input_file, countries_file):
    """
     Assess whether entry into Kanadia is accepted
    :param input_file: JSON formatted file with contains cases to decide
    :param countries_file: JSON formatted file with country data (for example, details regarding whether transit visa is necessary); also details if there is medical advisory
    :return: List of accepted strings are:
        "Accept", "Reject", and "Quarantine"
    """

    citizen_no = 0
    valid = False
    for citizen in json_citizens:
        passport_validity = valid_passport_format(citizen['passport'])
        if passport_validity is True:
            print("valid")
        else:
            print("False")
        date_validity = valid_date_format(citizen['birth_date'])
        if date_validity is True:
            print("valid")
        else:
            print("False")

def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes. Imports passport
    number from json file and tests passport number against regex.
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """

    passport_regex = re.compile(r'(\w{5}-){4}\w{5}')
    passport_match = passport_regex.search(passport_number)
    if passport_match is None:
        return False
    else:
        return True


def valid_visa_code_format(visa_code):
    """
    Checks visa regex against visa code, ensuring visa code has two groups of five alphanumerical characters
    :param visa_code: alpha-numberic string
    :return: Boolean; True if the format is valid, False otherwise
    """

    visa_regex = re.compile(r'\w{5}-\w{5}-\w{5}-\w{5}-\w{5}')
    visa_match = visa_regex.search(visa_code)
    if visa_match is None:
        return False
    else:
        return True


def valid_date_format(date_string):
    """
    Checks date regex against date string, ensuring whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean; True if the format is valid, False otherwise
    """

    date_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    date_match = date_regex.search(date_string)
    if date_match is None:
        return False
    else:
        return True


def valid_visa_pls(traveler):
    """
    Checks whether the entire visa format is valid
    :param traveler: visa code & visa date
    :return: Boolean; True if valid, False otherwise
    """

    valid = False
    visa_code = traveler['visa']['code']
    visa_date = traveler['visa']['date']
    valid_visa_code = valid_visa_code_format(visa_code)
    valid_visa_date = check_visa_date(2, visa_date)
    if (valid_visa_code and valid_visa_date) is True:
        valid = True
    else:
        valid = False
    return valid


def check_visa_date(x, visa_date):
    """
    :param x:
    :param visa_date:
    :return: Boolean; True if valid, False otherwise
    """

    valid = False
    visa_formatted = valid_date_format(visa_date)
    visa_expired = is_more_than_x_years_ago(x, visa_date)
    if (visa_formatted and visa_expired) is True:
        return True
    else:
        return False


def check_visa(traveler, valid_visa_format):
    """
    :param traveler:
    :param valid_visa_format:
    :return:
    """

    if traveler['home']['country'] == "KAN":
        return True
    else:



def quarantine_traveler(traveler, country):
    """
    :param traveler:
    :param country:
    :return:
    """
    for a in json_citizens:
        b = a['from']['country']
        if (json_countries[b]['medical_advisory']) == "":
            print("None")
        else:
            print("Quarantine")
