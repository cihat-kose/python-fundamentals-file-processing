"""Compare a callable's return value with an expected result."""


def check_function_result(function, arguments, expected_result):
    """Call function with positional arguments; let its exceptions propagate."""
    return function(*arguments) == expected_result


def add(first, second):
    return first + second


if __name__ == "__main__":
    print(check_function_result(add, [3, 4], 7))
    print(check_function_result(add, [3, 4], 8))
