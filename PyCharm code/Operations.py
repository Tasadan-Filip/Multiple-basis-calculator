"""
Author: Tasadan Filip
"""


class NumberOperations:
    """
    This class contains all the required number operations in bases from 2 to 16
    """
    def __init__(self):
        pass

    @staticmethod
    def convert_result_from_list_to_string(result_as_list):
        """
        This function will convert a list of digits into a number as a string
        :param result_as_list: list of digits ( type: list)
        :return: a string which will represent the number made out of those digits from the given list of digits
        """
        result_as_string = ''
        digits_dictionary = {
            '0': '0',
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '10': 'A',
            '11': 'B',
            '12': 'C',
            '13': 'D',
            '14': 'E',
            '15': 'F'
        }
        i = 0
        while result_as_list[i] == 0:
            i += 1
            if i == len(result_as_list):
                result_as_list[0] = 0
                i = len(result_as_list) - 1
                break

        result_as_list = result_as_list[i:]
        for digit in result_as_list:
            result_as_string += digits_dictionary[str(digit)]

        return result_as_string

    def add_two_numbers_in_base(self, number_1, number_2, given_base):
        """
        This is the function which will add two numbers in a given base
        :param number_1: the first number represented as a list of digits (type: list of digits in the given_base)
        :param number_2: the second number represented as a list of digits (type: list of digits in the given_base)
        :param given_base: the base in which the addition will be performed (type: natural number between 2 and 16)
        :return: the result of the two number addition as a list of digits (type: list of digits in the given_base)
        """
        carries = []
        result = []

        if len(number_1) > len(number_2):
            longest_length = len(number_1)
            first_operand = number_1
            second_operand = number_2
        else:
            longest_length = len(number_2)
            first_operand = number_2
            second_operand = number_1

        for i in range(longest_length + 1):
            carries.append(0)

        for i in range(longest_length + 1):
            result.append(0)

        """
        I reverse the two operands because I want to start the addition from the least important digit (located on the last position initially)
        to the most important one (located on the first position initially.
        """

        first_operand.reverse()
        second_operand.reverse()

        for i in range(len(second_operand), longest_length):
            second_operand.append(0)

        for i in range(longest_length):
            s10 = carries[i] + first_operand[i] + second_operand[i]
            carries[i + 1] += s10 // given_base
            result[i] = s10 % given_base
        result[longest_length] = carries[longest_length]
        """
        The result is reversed so that the digits are in the correct order now 
        (the most significant one in on the first position, ... , the least significant one will be on the last position) 
        """
        result.reverse()

        return self.convert_result_from_list_to_string(result)

    def subtract_two_numbers_in_base(self, number_1, number_2, given_base):
        """
        This is the function which will subtract two numbers in a given base
        :param number_1: the first number represented as a list of digits (type: list of digits in the given_base)
        :param number_2: the second number represented as a list of digits (type: list of digits in the given_base)
        :param given_base: the base in which the subtraction will be performed (type: natural number between 2 and 16)
        :return: the result of the two number subtraction as a list of digits (type: list of digits in the given_base)
        """
        borrows = []
        result = []

        longest_length = len(number_1)
        first_operand = number_1
        second_operand = number_2

        for i in range(longest_length + 1):
            borrows.append(0)

        for i in range(longest_length):
            result.append(0)

        """
        I reverse the two operands because I want to start the subtraction from the least important digit (located on the last position initially)
        to the most important one (located on the first position initially).
        """

        first_operand.reverse()
        second_operand.reverse()

        for i in range(len(second_operand), longest_length):
            second_operand.append(0)

        for i in range(longest_length):
            d10 = first_operand[i] - second_operand[i] - borrows[i]
            if d10 < 0:
                d10 = d10 + given_base
                borrows[i + 1] = 1
            result[i] = d10
        if borrows[longest_length] == 1:
            raise ValueError("The first number is smaller than the second one")

        """
        The result is reversed so that the digits are in the correct order now 
        (the most significant one in on the first position, ... , the least significant one will be on the last position) 
        """
        result.reverse()

        return self.convert_result_from_list_to_string(result)

    def multiply_two_numbers_in_base(self, number_1, number_2, given_base):
        """
        This is the function which will multiply two numbers in a given base
        :param number_1: the first number represented as a list of digits (type: list of digits in the given_base)
        :param number_2: the second number represented as a list of digits (type: list of digits in the given_base)
        :param given_base: the base in which the multiplication will be performed (type: natural number between 2 and 16)
        :return: the result of the two number multiplication as a list of digits (type: list of digits in the given_base)
        """
        carries = []
        result = []
        if len(number_1) != 1 and len(number_2) != 1:
            raise ValueError("One of operands must have exactly one digit")

        if len(number_1) > len(number_2):
            longest_length = len(number_1)
            first_operand = number_1
            second_operand = number_2
        else:
            longest_length = len(number_2)
            first_operand = number_2
            second_operand = number_1

        for i in range(longest_length + 1):
            carries.append(0)

        for i in range(longest_length + 1):
            result.append(0)

        """
        I reverse the first operand because I want to start the multiplication from the least important digit (located on the last position initially)
        to the most important one (located on the first position initially).
        """
        first_operand.reverse()

        for i in range(longest_length):
            p10 = first_operand[i] * second_operand[0] + carries[i]
            result[i] = p10 % given_base
            carries[i + 1] = p10 // given_base
        result[longest_length] = carries[longest_length]
        """
        The result is reversed so that the digits are in the correct order now 
        (the most significant one in on the first position, ... , the least significant one will be on the last position) 
        """
        result.reverse()

        return self.convert_result_from_list_to_string(result)

    def divide_two_numbers_in_base(self, number_1, number_2, given_base):
        """
        This is the function which will divide two numbers in a given base
        :param number_1: the first number represented as a list of digits (type: list of digits in the given_base)
        :param number_2: the second number represented as a list of digits (type: list of digits in the given_base)
        :param given_base: the base in which the division will be performed (type: natural number between 2 and 16)
        :return: the result of the two number division as a list of digits (type: list of digits in the given_base)
        """
        division_quotient = []
        if len(number_2) != 1:
            raise ValueError("The second operand must have exactly one digit")


        longest_length = len(number_1)
        first_operand = number_1
        second_operand = number_2

        for i in range(longest_length + 1):
            division_quotient.append(0)

        division_remainder = 0
        for i in range(longest_length):
            p10 = division_remainder * given_base + first_operand[i]
            division_quotient[i] = p10 // second_operand[0]
            division_remainder = p10 % second_operand[0]

        """
        The result is reversed so that the digits are in the correct order now 
        (the most significant one in on the first position, ... , the least significant one will be on the last position) 
        """
        division_quotient.pop()
        division_quotient = self.convert_result_from_list_to_string(division_quotient)
        return [division_quotient, division_remainder]
