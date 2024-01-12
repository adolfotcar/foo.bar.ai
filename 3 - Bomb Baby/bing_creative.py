def solution(M, F):
    # Convert the inputs to integers
    M = int(M)
    F = int(F)
    # Initialize the number of generations to zero
    generations = 0
    # Loop until either M or F is equal to 1
    while M != 1 or F != 1:
        # If both M and F are equal or less than zero, return "impossible"
        if M <= 0 or F <= 0:
            return "impossible"
        # If M is greater than F, subtract the largest multiple of F from M
        # and increment the generations by the same multiple
        elif M > F:
            multiple = M // F
            M -= multiple * F
            generations += multiple
        # If F is greater than M, do the same but with F and M swapped
        elif F > M:
            multiple = F // M
            F -= multiple * M
            generations += multiple
    # Return the number of generations as a string
    return str(generations)


