from django.core.exceptions import ValidationError
import re
from Realestate4.logger import log
feeds = []

def validate_first_name(value):
    first_name = str(value)
    feeds['first_name'] = first_name
    if not re.match("^[A-Za-z]*$", first_name):
        log.debug('first_name :[' + first_name + '] validation failed')
        raise ValidationError("Enter only alphabats")
    return value

def validate_last_name(value):
    last_name = str(value)
    if not re.match("^[A-Za-z]*$", last_name):
        log.info('last_name validation')
        raise ValidationError("Enter only alphabats")
    return value

def validate_city(value):
    city = str(value)
    if not re.match("^[A-Za-z]*$", city):
        log.info('city validation')
        raise ValidationError("Enter only alphabats")
    return value

def validate_state(value):
    state = str(value)
    if not re.match("^[A-Za-z]*$", state):
        log.info('state validation ')
        raise ValidationError("Enter only alphabats")
    return value

def validate_landmark(value):
    landmark = str(value)
    if not re.match("^[A-Za-z]*$", landmark):
        log.info('landmark validation ')
        raise ValidationError("Enter only alphabats")
    return value
def validate_education(value):
    education = str(value)
    if not re.match("^[A-Za-z0-9.]*$", education):
        log.info('education validation ')
        raise ValidationError("Enter only alphabats and numbers")
    return value
def validate_specialization(value):
    specialization = str(value)
    if not re.match("^[A-Za-z\s]*$", specialization):
        log.info('specialization validation ')
        raise ValidationError("Enter only alphabats")
    return value
def validate_mobile_number(value):
    mobile_number = str(value)
    if not re.match("^[0-9]*$", mobile_number):
        log.info('mobile_no validation')
        raise ValidationError("Enter only numbers")
    return value
def validate_phone_number(value):
    phone_number = str(value)
    if not re.match("^[0-9]*$", phone_number):
        log.info('phone_number validation')
        raise ValidationError("Enter only numbers")
    return value
def validate_name(value):
    name = str(value)
    log.info('feeds:' + feeds)
    if not re.match("^[A-Za-z]*$", name):
        log.info('name validation ')
        raise ValidationError("Enter only alphabats")
    return value

