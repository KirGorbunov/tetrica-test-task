from solution import sum_two

assert sum_two(2, 3) == 5

try:
    sum_two(2, "3")
except TypeError as e:
    assert str(e) == ""

try:
    sum_two("2", 3)
except TypeError as e:
    assert str(e) == ""
