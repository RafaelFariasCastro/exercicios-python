"""Sequence to List and Tuple
Create a Python function that takes a sequence of comma-separated numbers as input and generates both a list and a tuple containing those numbers.

Level: Beginner

Input: convert_input_to_list_and_tuple("3,6,5,3,2,8")

Expected Output:(['3', '6', '5', '3', '2', '8'], ('3', '6', '5', '3', '2', '8'))


Hints:The input will be provided as a string.
Use the split(",") method to convert the string into a list.
The tuple() method can convert a list into a tuple."""

def convert_input_to_list_and_tuple(input_string):
    values = input_string.split(",")
    return values, tuple(values)

convert_input_to_list_and_tuple("3,6,5,3,2,8")