""" 
Utility functions
"""


def get_integer(instruction: str, min_value: int, max_value: int) -> int:
    """Get valid integer from the user

    Args:
        instruction (str): the instruction(prompt) to the user
        min_value (int): the minimum value expected
        max_value (int): the maximum value expected

    Returns:
        int: the valid input from the user
    """
    while True:
        try:
            print()
            value = int(input(instruction))

            if value < min_value or value > max_value:
                print(f"Invalid input received. Expecting values between {min_value} to {max_value}")
            else:
                return value
        except Exception as ex:
            print(f"Invalid input received. Expecting values between {min_value} to {max_value}")
            print(f"Error occured [{ex}]")


def get_float(instruction: str, min_value: float, max_value: float) -> float:
    """Get valid floating point value from the user

    Args:
        instruction (str): the instruction(prompt) to the user
        min_value (float): the minimum value expected
        max_value (float): the maximum value expected

    Returns:
        float: the valid input from the user
    """
    while True:
        try:
            print()
            value = float(input(instruction))

            if value < min_value or value > max_value:
                print(f"Invalid input received. Expecting values between {min_value} to {max_value}")
            else:
                return value
        except Exception as ex:
            print(f"Invalid input received. Expecting values between {min_value} to {max_value}")
            print(f"Error occured [{ex}]")