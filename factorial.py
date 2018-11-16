import math


# The iterative function
def fact_iter(n):
    x = 1

    for i in range(n, 0, -1):
        x *= i
    return x


# The recursive function
def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n - 1)


# Using the math function

def using_library(n):
    result = math.factorial(n)
    return result


n = 5

iteratively = fact_iter(n)

recursively = fact_recur(n)

math_func = using_library(n)

# print("The iterative: \n", iteratively, "The recursive: \n", recursively,"with math function: \n",math_func)
print(f"The iterative: {iteratively} The recursive: {recursively} With math function: {math_func}")
