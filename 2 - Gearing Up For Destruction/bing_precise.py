from fractions import Fraction

def solution(pegs):
    if len(pegs) % 2 == 0:
        even = True
    else:
        even = False

    distances = [pegs[i+1] - pegs[i] for i in range(len(pegs)-1)]
    if len(distances) == 1:
        first_gear_radius = Fraction(distances[0] - 1, 1)
    else:
        first_gear_radius = Fraction((distances[0] + (-1)**(len(pegs)+1) * distances[-1])/2)

    if first_gear_radius < 1:
        return [-1, -1]

    current_radius = first_gear_radius
    for i in range(len(distances)):
        next_radius = distances[i] - current_radius
        if next_radius < 1:
            return [-1, -1]
        current_radius = next_radius

    return [first_gear_radius.numerator, first_gear_radius.denominator]


