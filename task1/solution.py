from inspect import get_annotations


def strict(func):
    def wrapper(*args, **kwargs):
        annotations = get_annotations(func)
        for (param, value) in zip(annotations.keys(), args):
            if type(value) is not annotations.get(param):
                raise TypeError(f"Аргумент {param} имеет тип {type(value)}, что не соответствует аннотации")
        for kwarg in kwargs:
            if type(kwargs[kwarg]) is not annotations[kwarg]:
                raise TypeError(f"Аргумент {kwarg} имеет тип {type(kwargs[kwarg])}, что не соответствует аннотации")
        result = func(*args, **kwargs)
        return result
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
