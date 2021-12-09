"""
Author: Tasadan Filip
"""
class Number:
    def __init__(self, number_as_string, base):
        self.digits_dictionary={
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }
        self.__base = int(base)
        self.__number_as_string = number_as_string
        self.__number_as_list_of_digits = self.convert_number_from_string_to_list(number_as_string)

    @property
    def number_as_string(self):
        return self.__number_as_string

    @property
    def number_as_list_of_digits(self):
        return self.__number_as_list_of_digits

    @property
    def base(self):
        return self.__base

    @staticmethod
    def validate_base(given_base):
        try:
            base = int(given_base)
        except:
            raise ValueError("Base should be a NATURAL number between 2 and 16")
        if base < 0 or base > 16:
            raise ValueError("Base should be a natural number BETWEEN 2 and 16")
        return base

    def convert_number_from_string_to_list(self, number_string):
        local_number_as_list_of_digits = []
        for digit in number_string:
            if digit in self.digits_dictionary:
                if self.digits_dictionary[digit] < self.__base:
                    local_number_as_list_of_digits.append(self.digits_dictionary[digit])
                else:
                    raise ValueError("The given number can't be written in base " + str(self.__base))
            else:
                raise ValueError("The given number can't be written in base " + str(self.__base))
        return local_number_as_list_of_digits



