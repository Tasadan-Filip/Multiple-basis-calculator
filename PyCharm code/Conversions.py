"""
Author: Tasadan Filip
"""
from Operations import NumberOperations


class NumberConversions:
    """
    This class contains all the required number conversions in bases from 2 to 16
    """
    def __init__(self):
        pass

    @staticmethod
    def convert_number_from_string_to_list(number_string):
        digits_dictionary = {
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
        local_number_as_list_of_digits = []
        for digit in number_string:
            local_number_as_list_of_digits.append(digits_dictionary[digit])
        return local_number_as_list_of_digits

    @staticmethod
    def substitution_method(source_number, source_base, destination_base):
        """
        This is the function for the substitution conversion method
        :param source_number: the number we want to convert ( it is written in the source base) (type: string of digits)
        :param source_base: the source base (the base of the number we want to convert) (type: string of digits)
        :param destination_base: the destination base in which we want to convert our number (type: string of digits)
        :return: it will return the value of our number in the destination base (type: string of digits)
        """
        source_base = int(source_base)
        destination_base = int(destination_base)

        operations = NumberOperations()

        converted_number = [0]

        source_number_digits_as_list = NumberConversions.convert_number_from_string_to_list(source_number)

        source_number_digits_as_list.reverse()

        for i in range(len(source_number_digits_as_list)):
            if i == 0:
                positional_power = [1]
            else:
                positional_power = operations.multiply_two_numbers_in_base(positional_power[:], [source_base][:], destination_base)
                positional_power = NumberConversions.convert_number_from_string_to_list(positional_power)

            positional_number = operations.multiply_two_numbers_in_base(positional_power[:], [source_number_digits_as_list[i]], destination_base)
            positional_number = NumberConversions.convert_number_from_string_to_list(positional_number)

            converted_number = operations.add_two_numbers_in_base(converted_number[:], positional_number[:], destination_base)
            converted_number = NumberConversions.convert_number_from_string_to_list(converted_number)

        return operations.convert_result_from_list_to_string(converted_number)

    @staticmethod
    def successive_division_method(source_number, source_base, destination_base):
        """
        This is the function for the successive division conversion method
        :param source_number: the number we want to convert ( it is written in the source base) (type: string of digits)
        :param source_base: the source base (the base of the number we want to convert) (type: string of digits)
        :param destination_base: the destination base in which we want to convert our number (type: string of digits)
        :return: it will return the value of our number in the destination base (type: string of digits)
        """
        source_base = int(source_base)
        destination_base = int(destination_base)

        remainders_list = []
        operations = NumberOperations()
        quotient_as_list = NumberConversions.convert_number_from_string_to_list(source_number)
        while quotient_as_list != [0]:
            division_result = operations.divide_two_numbers_in_base(quotient_as_list, [destination_base][:], source_base)
            quotient_as_list = NumberConversions.convert_number_from_string_to_list(division_result[0])
            remainder_of_div = division_result[1]
            remainders_list.append(remainder_of_div)

        remainders_list.reverse()
        converted_number = operations.convert_result_from_list_to_string(remainders_list)
        return converted_number

    @staticmethod
    def convert_using_base_10_as_intermediate(source_number, source_base, destination_base):
        """
        This is the function for the intermediate base 10 conversion method
        If the source base is smaller than 10 the program will convert from source base to base 10 using successive division method
        If the source base is bigger than 10 the program will convert from source base to base 10 using substitution method

        If the destination base is smaller than 10 the program will convert from base 10 to destination base using successive division method
        If the destination base is bigger than 10 the program will convert from base 10 to destination base using substitution method

        :param source_number: the number we want to convert ( it is written in the source base) (type: string of digits)
        :param source_base: the source base (the base of the number we want to convert) (type: string of digits)
        :param destination_base: the destination base in which we want to convert our number (type: string of digits)
        :return: it will return the value of our number in the destination base (type: string of digits)
        """
        source_base = int(source_base)
        destination_base = int(destination_base)

        if source_base < 10:
            intermediate_result = NumberConversions.successive_division_method(source_number, source_base, '10')
        else:
            intermediate_result = NumberConversions.substitution_method(source_number, source_base, '10')

        if destination_base < 10:
            final_result = NumberConversions.successive_division_method(intermediate_result, '10', destination_base)
        else:
            final_result = NumberConversions.substitution_method(intermediate_result, '10', destination_base)

        return final_result

    @staticmethod
    def rapid_conversion_method(source_number, source_base, destination_base):
        """
        This is the function for the rapid conversion method
        The first step will be to convert the source number from the source base into base 2
        The second step will be to convert the number in base to obtained after the first step into the destination base
        :param source_number: the number we want to convert ( it is written in the source base) (type: string of digits)
        :param source_base: the source base (the base of the number we want to convert) (type: string of digits)
        :param destination_base: the destination base in which we want to convert our number (type: string of digits)
        :return: it will return the value of our number in the destination base (type: string of digits)
        """
        operations = NumberOperations()
        source_base = int(source_base)
        destination_base = int(destination_base)
        source_number_digits_as_list = NumberConversions.convert_number_from_string_to_list(source_number)
        source_number_digits_as_list.reverse()

        if source_base not in [2, 4, 8, 16]:
            raise ValueError("Can't use rapid conversion for the given source base")

        if destination_base not in [2, 4, 8, 16]:
            raise ValueError("Can't use rapid conversion for the given destination base")


        power_of_2_source_base = -1
        power_of_2_destination_base = -1

        aux_source = source_base
        aux_destination = destination_base

        while aux_source:
            aux_source = aux_source // 2
            power_of_2_source_base += 1

        while aux_destination:
            aux_destination = aux_destination // 2
            power_of_2_destination_base += 1

        binary_digits_list = []

        """
        Here the program converts the number from source b ase into base 2 and add unnecessary 0 at
        the end of the list ( our number is reversed so the most significant digit will be
        on the last position)
        """
        for digit in source_number_digits_as_list:
            for counter in range(power_of_2_source_base):
                binary_digits_list.append(digit % 2)
                digit = digit // 2
        while len(binary_digits_list) % power_of_2_source_base != 0:
            binary_digits_list.append(0)

        result_digits_list = []
        """
        Here the program converts the number from base 2 into the destination base by grouping the digits into
        groups of k (destination base is of the form 2^k) and converting those digits into values in the destination
        base and append them to the result digits list which is going to be converted into a string of digits
        """
        for counter_1 in range(0, len(binary_digits_list), power_of_2_destination_base):
            result_digits_list.append(sum([binary_digits_list[counter_1 + counter_2]*(2 ** counter_2) for counter_2 in range(power_of_2_destination_base)]))

        result_digits_list.reverse()
        result_as_string = operations.convert_result_from_list_to_string(result_digits_list)

        return result_as_string



