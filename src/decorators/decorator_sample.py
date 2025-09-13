class NonIntegerArgumentError(Exception):
    message = "All arguments must be integers."


def require_int_args(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            # isinstance(arg, int) returns True for instances of int and its subclasses.
            # type(arg) is int returns True only if arg is exactly of type int, not a subclass.
            # isinstance is more flexible and recommended for type checking in Python.
            if not isinstance(arg, int):
                raise NonIntegerArgumentError
        return func(*args, **kwargs)

    return wrapper


@require_int_args
def sum_nums(a, b, c):
    return a + b + c


if __name__ == "__main__":
    try:
        print(sum_nums(1, 2, 3))
        print(sum_nums(1, 2, "3"))
    except NonIntegerArgumentError as e:
        print(f"Error: {e.message}")
