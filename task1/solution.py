def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        annotations_types = list(annotations.values())
        args_list = list(args)
        for i in range(len(args_list)):
            if type(args_list[i]) is not annotations_types[i]:
                raise TypeError(f"Аргумент {i+1} имеет тип {type(args_list[i])}, а ожидается {annotations_types[i]}")
        for j in kwargs:
            if type(kwargs[j]) is not annotations[j]:
                raise TypeError(f"Аргумент {j} имеет тип {type(kwargs[j])}, а ожидается {annotations[j]}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

print(sum_two(b=1, a=2))