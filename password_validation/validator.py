import re
from django.core.exceptions import ValidationError
from django.util.translation import ugettext as text


class NumValidator(object):
    """
    NumValidator checks passwords for numbers
    """

    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                text("The password must contain at least 1 number, 0-9."),
                code='password_no_number')

    def get_help_text(self):
        return text("Your password must contain at least 1 number, 0-9.")


class SymbolValidator(object):
    """
    SymbolValidator checks passwords for symbols
    """

    def validate(self, password, user=None):
        if not re.findall('["#$%&\'()*+,-./:;<=>?@\\^_`{|}~]', password):
            raise ValidationError(text(
                "The password must contain at least 1 special character: " +
                "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                                  code='password_no_symbol')

    def get_help_text(self):
        return text(
            "Your password must contain at least 1 special character: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?")


class UppercaseValidator(object):
    """
    UppercaseValidator checks passwords for uppercase letters
    """

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                text(
                    "The password must contain at least 1 capital letter, A-Z."
                ),
                code='password_no_upper',
            )

    def get_help_text(self):
        return text(
            "Your password must contain at least 1 capital letter, A-Z.")
