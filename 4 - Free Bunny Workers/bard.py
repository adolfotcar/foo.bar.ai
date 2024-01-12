def solution(buns, required):
    # Check input validity
    if buns < 1 or buns > 9:
        raise ValueError("Invalid number of bunnies: {} (should be between 1 and 9)".format(buns))
    if required < 0 or required > 9:
        raise ValueError("Invalid number of bunnies needed to open: {} (should be between 0 and 9)".format(required))

    # Initialize lists for distributing keys
    bunny_keys = [[] for _ in range(buns)]

    # Create a list of available keys
    available_keys = list(range(required))

    # Prioritize assigning keys to bunnies with fewer keys
    while available_keys:
        # Find the bunny with the fewest keys
        least_keys_bunny_idx = min(range(buns), key=lambda i: len(bunny_keys[i]))

        # Assign the next available key to the bunny with the fewest keys
        bunny_keys[least_keys_bunny_idx].append(available_keys.pop(0))

    # Return the lexicographically least key distribution
    return sorted(bunny_keys)


