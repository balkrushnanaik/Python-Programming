def divide(a, b):
    """Divide two numbers and return the result.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
print(divide.__doc__)
print(divide(10,20))