""" 
String Manipulation Class
Define a class that contains at least two methods: get_string to retrieve a string from console input and print_string to display the string in uppercase. Additionally, include a simple test function to validate the class methods.

Difficulty: Level 1

Input:str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()

Expected Output: If the input string is "hello world", the output will be:
HELLO WORLD

Hints: Utilize the __init__ method to initialize the class parameters."""

class InputOutString:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Enter a string: ")

    def print_string(self):
        print(self.s.upper())

# Test function

str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()