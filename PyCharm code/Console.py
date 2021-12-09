"""
Author: Tasadan Filip
"""
from number_entity import Number
from Operations import NumberOperations
from Conversions import NumberConversions


class UserInterface:

    @staticmethod
    def operations_input():
        given_base = input("Enter the base you want to compute the two numbers >> ")
        base_p = Number.validate_base(given_base)
        number_1_as_string = input("Enter the first number value in base {} >> ".format(base_p))
        number_1_as_object = Number(number_1_as_string, base_p)
        number_2_as_string = input("Enter the second number value in base {} >> ".format(base_p))
        number_2_as_object = Number(number_2_as_string, base_p)

        operand_1 = number_1_as_object.number_as_list_of_digits
        operand_2 = number_2_as_object.number_as_list_of_digits
        return [base_p, operand_1, operand_2, number_1_as_string, number_2_as_string]

    @staticmethod
    def conversions_input():
        source_number_to_convert = input("Enter the source number you want to convert >> ")
        source_base = input("Enter the source base >> ")
        Number.validate_base(source_base)
        x = Number(source_number_to_convert, source_base)
        destination_base = input("Enter the destination base >> ")
        Number.validate_base(destination_base)

        return [source_number_to_convert, source_base, destination_base]

    def add_numbers_ui(self):
        inputs_list = self.operations_input()
        base_p = inputs_list[0]
        operand_1_as_list = inputs_list[1]
        operand_1_as_string = inputs_list[3]
        operand_2_as_list = inputs_list[2]
        operand_2_as_string = inputs_list[4]

        string_result = self.__operations.add_two_numbers_in_base(operand_1_as_list, operand_2_as_list, base_p)
        print("Result: {} + {} = {} (in base {})".format(operand_1_as_string, operand_2_as_string, string_result, str(base_p)))

    def subtract_numbers_ui(self):
        inputs_list = self.operations_input()
        base_p = inputs_list[0]
        operand_1_as_list = inputs_list[1]
        operand_1_as_string = inputs_list[3]
        operand_2_as_list = inputs_list[2]
        operand_2_as_string = inputs_list[4]

        string_result = self.__operations.subtract_two_numbers_in_base(operand_1_as_list, operand_2_as_list, base_p)
        print("Result: {} - {} = {} (in base {})".format(operand_1_as_string, operand_2_as_string, string_result, str(base_p)))

    def multiply_numbers_ui(self):
        inputs_list = self.operations_input()
        base_p = inputs_list[0]
        operand_1_as_list = inputs_list[1]
        operand_1_as_string = inputs_list[3]
        operand_2_as_list = inputs_list[2]
        operand_2_as_string = inputs_list[4]

        string_result = self.__operations.multiply_two_numbers_in_base(operand_1_as_list, operand_2_as_list, base_p)
        print("Result: {} * {} = {} (in base {})".format(operand_1_as_string, operand_2_as_string, string_result, str(base_p)))

    def divide_numbers_ui(self):
        inputs_list = self.operations_input()
        base_p = inputs_list[0]
        operand_1_as_list = inputs_list[1]
        operand_1_as_string = inputs_list[3]
        operand_2_as_list = inputs_list[2]
        operand_2_as_string = inputs_list[4]

        string_result = self.__operations.divide_two_numbers_in_base(operand_1_as_list, operand_2_as_list, base_p)
        division_quotient = string_result[0]
        division_remainder = string_result[1]
        print("Result: {} / {} = {}, r {} (in base {})".format(operand_1_as_string, operand_2_as_string, division_quotient, division_remainder, str(base_p)))

    def substitution_method_ui(self):
        inputs_list = self.conversions_input()
        destination_number = NumberConversions.substitution_method(inputs_list[0], inputs_list[1], inputs_list[2])
        print("The value of {} (base {}) is {} in base {}".format(inputs_list[0], inputs_list[1], destination_number, inputs_list[2]))

    def successive_division_method_ui(self):
        inputs_list = self.conversions_input()
        destination_number = NumberConversions.successive_division_method(inputs_list[0], inputs_list[1], inputs_list[2])
        print("The value of {} (base {}) is {} in base {}".format(inputs_list[0], inputs_list[1], destination_number,inputs_list[2]))

    def intermediate_base_10_metod_ui(self):
        inputs_list = self.conversions_input()
        destination_number = NumberConversions.convert_using_base_10_as_intermediate(inputs_list[0], inputs_list[1], inputs_list[2])
        print("The value of {} (base {}) is {} in base {}".format(inputs_list[0], inputs_list[1], destination_number, inputs_list[2]))

    def rapid_conversion_method_ui(self):
        inputs_list = self.conversions_input()
        destination_number = NumberConversions.rapid_conversion_method(inputs_list[0], inputs_list[1], inputs_list[2])
        print("The value of {} (base {}) is {} in base {}".format(inputs_list[0], inputs_list[1], destination_number, inputs_list[2]))

    def __init__(self):
        self.__operations = NumberOperations()
        self.__commands_dict = {
            '1': self.add_numbers_ui,
            '2': self.subtract_numbers_ui,
            '3': self.multiply_numbers_ui,
            '4': self.divide_numbers_ui,
            '5': self.substitution_method_ui,
            '6': self.successive_division_method_ui,
            '7': self.intermediate_base_10_metod_ui,
            '8': self.rapid_conversion_method_ui
        }

    @staticmethod
    def menu_commands_ui():
        print()
        print("Here is the list of commands which you can use")
        print()
        print("exit - for exiting from the program")
        print()
        print("Operations between two numbers commands:")
        print("1 - add two numbers in a given base")
        print("2 - subtract two numbers in a given base")
        print("3 - multiply two numbers in a given base (one of them must have exactly one digit)")
        print("4 - divide two numbers in a given base (the second one must have exactly one digit)")
        print("Conversions of a number in a given base to another base commands:")
        print("5 - substitution method conversion")
        print("6 - successive division conversion")
        print("7 - intermediate base 10 conversion")
        print("8 - rapid conversion method")
        print()

    def run(self):
        print()
        print("Author of this project: Tasadan Filip")
        print("This project is made in 'Python 3' programming language")
        print()
        print("Notes")
        print("Each command has an associate number written in the beggining of the line")
        print("You have to enter the associate number of the command you want to use")

        done = False
        while not done:
            self.menu_commands_ui()
            command = input('Command number >>')
            if command == 'exit':
                print("Goodbye!")
                done = True
            else:
                try:
                    if command in self.__commands_dict:
                        self.__commands_dict[command]()

                    else:
                        raise ValueError("Invalid command!")
                except ValueError as ve:
                    print("Error: " + str(ve))

