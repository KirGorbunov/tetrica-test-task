from solution import sum_two


assert sum_two(2, 3) == 5

try:
    sum_two(2, "3")
except TypeError as e:
    assert str(e) == "Аргумент 2 имеет тип <class 'str'>, что не соответствует аннотации"

try:
    sum_two("2", 3)
except TypeError as e:
    assert str(e) == "Аргумент 1 имеет тип <class 'str'>, что не соответствует аннотации"

assert sum_two(b=2, a=3) == 5

try:
    sum_two(b=2, a="3")
except TypeError as e:
    assert str(e) == "Аргумент a имеет тип <class 'str'>, что не соответствует аннотации"

try:
    sum_two(b="2", a=3)
except TypeError as e:
    assert str(e) == "Аргумент b имеет тип <class 'str'>, что не соответствует аннотации"

assert sum_two(2, b=3) == 5

try:
    sum_two("2", b=3)
except TypeError as e:
    assert str(e) == "Аргумент 1 имеет тип <class 'str'>, что не соответствует аннотации"

try:
    sum_two(2, b="3")
except TypeError as e:
    assert str(e) == "Аргумент b имеет тип <class 'str'>, что не соответствует аннотации"
