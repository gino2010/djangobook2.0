__author__ = 'Gino'
#chapter 09 Creating a Template Library
from django import template
register = template.Library()


def cut(value, arg):
    #"Removes all values of arg from the given string"
    return value.replace(arg, '')


def lower(value):  # Only one argument."Converts a string into all lowercase"
    return value.lower()

register.filter('cut', cut)
register.filter('lower', lower)