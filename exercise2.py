__author__ = 'Hana'

#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = 'Hana Nagel, Liana Sukaisyan and Katherine Ing'
__email__ = "hana.nagel@mail.utoronto.ca; liana.sukiasyan@mail.utoronto.ca; k.ing@mail.utoronto.ca"
__copyright__ = "2015 Hana Nagel, Liana Sukaisyan and Katherine Ing"
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
    statuses = []
    for traveller in travellers:
        status = ''
    # If more than one distinct immigration decision, status priority: 1) quarantine 2) reject 3) accept

        # 1. check to see if required fields were provided / are correct
        if not has_validated_fields(traveller):
            status = 'Reject'

        if not valid_passport_format(traveller['passport']):
            status = "Reject"

        if not valid_date_format(traveller['birth_date']):
            status = "Reject"

        # 2. ensure locations are known & valid
        # check from & home locations
        if not known_country(traveller['from']) or not known_country(traveller['home']) or ('via' in traveller and not known_country(traveller['via'])) or ('visa' in traveller and not known_country(traveller['visa'])):
            status = 'Reject'

        # 3. accept KAN
        if traveller['home']['country'] == 'KAN' and status != 'Reject':
            status = 'Accept'

        # 4. if traveller is visiting, check if home country needs passport, then check if have visa, then check visa
        if traveller['entry_reason'] == 'visiting' and valid_visitor(traveller) and status != 'Reject':
            status = 'Accept'
        else:
            status = 'Reject'

        # 5. first checks if traveller is travelling through a quarantine country ...
        # second checks if traveller is coming from a quarantine country.
        if ('via' in traveller and COUNTRIES[traveller['via']['country']]['medical_advisory'] == 1) or COUNTRIES[traveller['from']['country']]['medical_advisory'] == 1:
            status = 'Quarantine'

        statuses.append(status)

    return statuses

# Add str.lower so that no entry is rejected if there is a mismatch between uppercase and lowercase


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

    visa_regex = re.compile(r'\w{5}-\w{5}')
    visa_match = visa_regex.search(visa_code)
    if visa_match is None:
        return False
    else:
        return True

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

def valid_visa(visa):
    return valid_visa_format(visa['code']) and valid_date_format(visa['date']) and not is_more_than_x_years_ago(2, visa['date'])

def has_validated_fields(traveller):
    for required_field in REQUIRED_FIELDS:
        try:
            if len(traveller[required_field]) <= 0:
                is_valid_record = False
                break
        except:
            is_valid_record = False
            break

    return is_valid_record


def known_country(country):
    return country['country'] in COUNTRIES

def valid_visitor(traveller):
    visa_required = COUNTRIES[traveller['home']['country']]['visitor_visa_required'] == 1
    if visa_required and ('visa' not in traveller or not valid_visa(traveller['visa'])):
        return False
    else:
        return True