def solution(M, F):

    # Initialize a set to store encountered states
    seen = set()

    # Initialize current state as {M, F}
    current_state = {int(M), int(F)}

    # Implement a loop to iterate through replication cycles
    cycle = 0
    while True:
        # Check if the current state contains the target number of bombs
        if int(M) == 2 and int(F) == 1:
            return str(cycle)

        # Check if the current state has already been encountered
        if current_state in seen:
            return "impossible"

        # Apply the first replication process (Mach retrieves sync unit)
        next_state = {int(M), int(F) + int(M)}
        if next_state not in seen:
            seen.add(next_state)
            current_state = next_state
            cycle += 1

        # Apply the second replication process (Facula spontaneously creates Mach)
        next_state = {int(M) + int(F), int(F)}
        if next_state not in seen:
            seen.add(next_state)
            current_state = next_state
            cycle += 1


