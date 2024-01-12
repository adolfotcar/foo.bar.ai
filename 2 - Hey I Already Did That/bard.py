def solution(n, b):
    """
    Returns the length of the ending cycle of the algorithm for a given minion ID
    """
    seen_ids = set()  # Set to store previously seen minion IDs
    curr_id = n
    cycle_length = 0

    while True:
        if curr_id in seen_ids:
            # Found the cycle
            return len(seen_ids) - cycle_length

        seen_ids.add(curr_id)
        x = curr_id
        y = ""

        # Convert the minion ID to a base-b string
        for i in range(len(curr_id) - 1, -1, -1):
            y = str(curr_id[i]) + y

        z = int(x, b) - int(y, b)
        curr_id = z
        cycle_length += 1


