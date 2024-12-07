def strict(func):
    def wrapper(*args, **kwargs):
        annotation_types = list(func.__annotations__.values())
        vars_list = list(args)
        for i in range(len(args)):
            print(i, type(vars_list[i]), annotation_types[i])
            if type(vars_list[i]) is not annotation_types[i]:
                raise TypeError
        result = func(*args, **kwargs)
        return result
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b