def utils_func_1(name):
    """Utils Function 1

    Args:
    name (str): The name of the person to greet.
    """
    print(f"Hello {name}!")


def utils_func_2(name, password):
    """Utils Function 2

    Args:
    name (str): The name of the person to greet.
    password (str): The password of the person to greet.
    """
    print(f"Hello {name}!")
    
def function_with_types_in_docstring(param1, param2):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """