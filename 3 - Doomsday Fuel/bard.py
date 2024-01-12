def solution(m):
    # Initialize the visited set to track visited states
    visited = {0}

    # Initialize an empty dictionary to store probabilities for each state
    probabilities = {}

    # Perform DFS to traverse the transition matrix and calculate probabilities
    def dfs(state, probability):
        if state in visited:
            return

        # Add the current state to the visited set
        visited.add(state)

        # Update the probability for the current state
        probabilities[state] = probability

        # Iterate through the transitions for the current state
        for neighbor, weight in enumerate(m[state]):
            # Skip transitions to already visited states
            if neighbor in visited:
                continue

            # Calculate the probability of reaching the neighbor state
            next_probability = probability * weight

            # Recursively traverse the neighbor state
            dfs(neighbor, next_probability)

    # Initialize the probability for the start state (0)
    dfs(0, 1)

    # Calculate the denominator for all probabilities
    denominator = 1
    for probability in probabilities.values():
        denominator *= probability

    # Convert probabilities to simplified fractions with the denominator
    normalized_probabilities = []
    for state, probability in probabilities.items():
        numerator = probability // denominator
        normalized_probabilities.append([numerator, denominator])

    return normalized_probabilities


