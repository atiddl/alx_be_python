def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    float or str: The result of the operation, or a message if division by zero is attempted or if the operation is invalid.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Invalid operation"