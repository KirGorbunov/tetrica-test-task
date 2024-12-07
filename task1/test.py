from solution import sum_two


assert sum_two(2, 3) == 5

try:
    sum_two(2, "3")
except TypeError as e:
    assert str(e) == "Аргумент 2 имеет тип <class 'str'>, а ожидается <class 'int'>"

try:
    sum_two(2, 3)
except TypeError as e:
    assert str(e) == "Аргумент 1 имеет тип <class 'str'>, а ожидается <class 'int'>"
