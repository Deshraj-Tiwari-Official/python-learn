def avg(a, b, c):
    """
    Calculate the average of three input numbers.

    Parameters:
    a (int): The first input number
    b (int): The second input number
    c (int): The third input number

    Returns:
    float: The average of the three input numbers
    """

    # Calculate the sum of the input numbers
    sum_of_numbers = a + b + c

    # Calculate the average by dividing the sum by 3
    average = sum_of_numbers / 3

    # Return the average
    return average


output = avg(10, 20, 30)
print(output)
