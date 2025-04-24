"""Generate Square Dictionary
Create a Python function that takes an integer ( n ) as input and generates a dictionary containing pairs ( (i, i^2) ) for all integers ( i ) from 1 to ( n ) (inclusive). The function should then return this dictionary.

Level: Beginner


Input:generate_square_dict(8)

Expected Output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: Use the dict() function to create an empty dictionary.
Iterate through the range from 1 to ( n ) using a loop."""


def generate_square_dict(n):
    square_dict = {}  # Create an empty dictionary
    for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
        square_dict[i] = i ** 2  # Add key-value pair (i: i²)
    return square_dict

print(generate_square_dict(8))