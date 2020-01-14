# Chandler Stevens
# CSC 3430: Algorithm Design and Analysis
# Dr. Arias
# Python 3 program that compares the performance between iterative and
#  recursive implementations of the power function

# Import repeat function from timeit package
from timeit import repeat

# Initialize constants
# Set number of iterations to execute
ITERATIONS = 10 ** 4
# Set conversion factor from seconds to nanoseconds accounting for averaging
NANO = 10 ** 9 / ITERATIONS
# Set maximum value of n that does not return as plus or minus "inf"
SYSTEM_MAX_EXPONENT = 620
# Set an approximated value for pi as the base
PI = 3.14159265359


# Purpose: Iteratively calculate the power of a given number
# Parameters: base which represents the base number (float)
#             exponent which represents the power to raise the base (integer)
# Returns: Calculated power of the base raised by the exponent (float)
def iterativePower(base, exponent):
    # Initialize return value to one
    retVal = 1.0
    # If exponent is negative
    if exponent < 0:
        # Return reciprocal of recursively called function and positive exponent
        return 1.0 / iterativePower(base, -exponent)
    # Otherwise
    else:
        # Iterate from zero to the exponent
        for i in range(exponent):
            # Multiply the base to the current calculated result
            retVal *= base
    # Return the final calculated result
    return retVal


# Purpose: Recursively calculate the power of a given number
# Parameters: base which represents the base number (float)
#             exponent which represents the power to raise the base (integer)
# Returns: Calculated power of the base raised by the exponent (float)
def recursivePower(base, exponent):
    # If exponent is negative
    if exponent < 0:
        # Return reciprocal of recursively called function and positive exponent
        return 1.0 / recursivePower(base, -exponent)
    # Otherwise, if exponent is zero
    elif exponent == 0:
        # Return one (base case)
        return 1.0
    # Otherwise
    else:
        # Return base multiplied by recursively called function
        #  with decremented exponent
        return base * recursivePower(base, exponent - 1)


# Purpose: Function to time performance and compile CSV file
# Parameters: None
# Returns: Nothing
def compareImplementations():
    # Initialize output to empty string
    output = ""
    # Iterate from most negative value of n to most positive value of n
    for n in range(-SYSTEM_MAX_EXPONENT, SYSTEM_MAX_EXPONENT + 1):
        # Append to output string:
        # Value of n and comma
        # Average time in ns of iterative power function for n and comma
        # Average time in ns of recursive power function for n and newline
        output += (str(n) + "," +
                   str(min(repeat(lambda: iterativePower(PI, n),
                                  number=ITERATIONS)) * NANO) + "," +
                   str(min(repeat(lambda: recursivePower(PI, n),
                                  number=ITERATIONS)) * NANO) + "\n")
        # Display value of n to track progress
        print(n)
    # Create/Overwrite CSV file and open file stream
    fout = open("Iterative-vs-Recursive-Power.csv", "w")
    # Write output string to CSV file
    fout.write(output)
    # Close CSV file stream
    fout.close()


# Execute main function
compareImplementations()
