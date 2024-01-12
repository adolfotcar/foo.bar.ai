def solution(str_n):
    if int(str_n) <= 0:
        raise ValueError("n must be a positive integer")
    if int(str_n) > pow(10, 100):
        raise ValueError("n must be less than or equal to 10^100")

    # Calculate the maximum number of digits in the sum
    max_digits = int(str_n) * int(math.log10(sqrt(2))) + 1

    # Create a list to store the digits of the sum
    sum_digits = []

    # Initialize the running total of the sum
    running_sum = 0

    # Iterate over numbers from 1 to n
    for num in range(1, int(str_n) + 1):
        # Calculate the partial sum of i * sqrt(2)
        partial_sum = int(num * math.sqrt(2))

        # Add the integer part of the partial sum to the running total
        running_sum += partial_sum

        # Convert the running total to a string and append it to the sum_digits list
        sum_digits.append(str(running_sum)[-max_digits:])

        # Truncate the running total to remove the integer part
        running_sum = int(running_sum / 10)

    # Join the sum_digits list into a string and return it
    return ''.join(sum_digits)



