def solution(pegs):
    # Check if the input is valid
    if not pegs or len(pegs) < 2 or len(pegs) > 20:
        return [-1, -1]
    for peg in pegs:
        if peg < 1 or peg > 10000:
            return [-1, -1]
    
    # Calculate the sum of the distances between the pegs
    # with alternating signs
    sum = -pegs[0] - pegs[-1]
    if len(pegs) > 2:
        for i in range(1, len(pegs) - 1):
            sum += 2 * (-1)**i * pegs[i]
    
    # Calculate the first gear radius
    # If the number of pegs is even, the radius is 2 * sum / (len(pegs) - 1)
    # If the number of pegs is odd, the radius is 2 * sum / (len(pegs) - 1) / 3
    # The radius should be an integer or a fraction with denominator 3
    if len(pegs) % 2 == 0:
        num = 2 * sum
        den = len(pegs) - 1
        # Simplify the fraction
        gcd = get_gcd(num, den)
        num //= gcd
        den //= gcd
    else:
        num = 2 * sum
        den = 3 * (len(pegs) - 1)
        # Simplify the fraction
        gcd = get_gcd(num, den)
        num //= gcd
        den //= gcd
    
    # Check if the radius is valid
    # The radius should be greater than or equal to 1
    # and the gears should not overlap
    if num < den or num < 1:
        return [-1, -1]
    radius = num / den
    for i in range(len(pegs) - 1):
        distance = pegs[i + 1] - pegs[i]
        next_radius = distance - radius
        if next_radius < 1:
            return [-1, -1]
        radius = next_radius
    
    # Return the solution as a list of two integers
    return [num, den]

# Helper function to find the greatest common divisor of two numbers
def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


