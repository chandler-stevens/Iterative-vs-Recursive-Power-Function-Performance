from timeit import timeit


# Purpose: Measure execution time of function
# Parameters: Function to test
# Returns: Average execution time of function in nanoseconds
# Usage: measurePerformance(lambda: functionName(parameters))
def measurePerformance(function):
    # Return average adjusted from seconds to nanoseconds
    return timeit(lambda: function()) * (10**3)
