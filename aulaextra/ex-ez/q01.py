"""
Find numbers Divisible by 7, not by 5
Create a Python program that identifies all numbers between 100 and 300 (inclusive) that are divisible by 7 but not multiples of 5. The identified numbers should be displayed in a single line, separated by commas.

Level: Beginner

Input: find_numbers(100, 200)

Expected Output: 112,119,126,133,147,154,161,168,182,189,196

Hints:Use the range(#start, #stop) function to iterate over the specified range.
"""

def find_numbers(start, end):
    result = []
    for num in range(start, end + 1):
        if num % 7 == 0 and num % 5 != 0:
            result.append(str(num))
    return ','.join(result)

# Example usage:
print(find_numbers(100, 200))