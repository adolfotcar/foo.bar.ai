def solution(banana_list):
    # Sort the list of bananas in ascending order
    banana_list.sort()

    # Initialize a set to track the remaining trainers
    remaining_trainers = set()

    # Iterate through the sorted list of bananas
    for i in range(len(banana_list) - 1):
        # Check if the current pair leads to an infinite thumb wrestling loop
        if banana_list[i] + banana_list[i + 1] in remaining_trainers:
            # If yes, add the pair to the set and continue
            remaining_trainers.add((banana_list[i], banana_list[i + 1]))
            continue

        # If no, add the current trainer to the set
        remaining_trainers.add(banana_list[i])

        # Remove the current trainer and its opponent from the list
        banana_list[i:i + 2] = []

    # Count the number of remaining trainers
    remaining_trainers_count = len(remaining_trainers)

    # Return the fewest trainers left to watch the workers
    return remaining_trainers_count


