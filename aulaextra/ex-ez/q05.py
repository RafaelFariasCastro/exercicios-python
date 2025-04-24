"""
Calculate Q Values from D
Create a Python function that computes the value of ( Q ) using the formula:

 q=√((2*c*d)/h)

where ( C ) is 50 and ( H ) is 30. The function should take only ( D ) as input, which consists of a comma-separated sequence of values. The output should be rounded to the nearest integer and printed in a single line, separated by commas.

Difficulty: Level 1

Input: calculate_q_values("100,150,180")  # 100,150,180 are possible values of D

Expected Output: 18,22,24

Hints: Use the math.sqrt() function to compute the square root.
Convert input values to float for calculation, and round the result using the round() function.
"""

import math

def calculate_q_values(d_values):
    C = 50
    H = 30
    value = []
    items = [float(x) for x in d_values.split(',')]
    for D in items:
        Q = round(math.sqrt((2 * C * D) / H))
        value.append(str(Q))
    return ','.join(value)

calculate_q_values('5,50,500')