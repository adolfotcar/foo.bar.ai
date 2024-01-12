import math

def solution(pegs):
    # Check if the number of pegs is less than 2 or greater than 20
    if len(pegs) < 2 or len(pegs) > 20:
        return [-1, -1]

    # Initialize variables
    last_radius = -1
    gear_radius = 0
    for i, peg in enumerate(pegs):
        # Calculate the gear's speed for the current peg
        gear_speed = 2 * math.pi * gear_radius / (peg - last_radius)

        # Check if the gear's speed is valid
        if gear_speed <= 0:
            return [-1, -1]

        # Update the gear radius for the next iteration
        gear_radius = math.sqrt(peg * peg - last_radius * last_radius)
        last_radius = peg

    # Convert the gear radius to a simplified form (numerator/denominator)
    gear_radius_fraction = fraction(gear_radius)

    return gear_radius_fraction

def fraction(number):
    # Check if the number is already in a simplified form
    if number % 1 == 0:
        return [int(number), 1]

    # Initialize variables
    current_divisor = 2
    numerator = int(number)
    denominator = 1

    # Find the greatest common divisor (GCD) using Euclidean Algorithm
    while current_divisor <= numerator:
        if numerator % current_divisor == 0:
            numerator = numerator // current_divisor
            denominator = denominator * current_divisor

        current_divisor += 1

    return [numerator, denominator]


