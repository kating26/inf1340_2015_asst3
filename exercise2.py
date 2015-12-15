__author__ = 'Hana'

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


#####################
# HELPER FUNCTIONS ##
#####################
def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.

    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() < 0


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """

    # Pulls countries from JSON file
    with open(countries_file, "r") as file_reader:
        file_contents = file_reader.read()
    COUNTRIES = json.loads(file_contents)

    # Testing that countries pulled from JSON file and are in a nice list form
    # print json.dumps(COUNTRIES, indent=1)

    # Pulls traveller information from JSON file
    with open(input_file, "r") as file_reader:
        file_contents = file_reader.read()
    travellers = json.loads(file_contents)

    for traveller in travellers:
        status = 'Accept';

        #1. check to see if required fields were provided
        for required_field in REQUIRED_FIELDS:
            if(required_field not in traveller) :
                status = 'Reject'

        #2. if location is known - home & from location
        if(traveller['home']['country'] not in COUNTRIES or traveller['from']['country'] not in COUNTRIES):
            status = 'Reject'

        #3. if home country is KAN
        if(traveller['home']['country'] == 'KAN'):
            status = 'Accept'
        elif(traveller['entry_reason'] == 'visiting'):
            country = COUNTRIES[traveller['home']['country']]
            print(country['visitor_visa_required'])


        print(traveller['entry_reason'])




    return ["Reject"]


def valid_passport_format(passport_number):
    """
    Checks whether a pasport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_regex = re.compile(r'(\w{5}-){4}\w{5}')
    passport_match = passport_regex.search(passport_number)
    if passport_match is None:
        return False
    else:
        return True



def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

    date_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    date_match = date_regex.search(date_string)
    if date_match is None:
        return False
    else:
        return True



decide('./test_jsons/test_returning_citizen.json', './test_jsons/countries.json')