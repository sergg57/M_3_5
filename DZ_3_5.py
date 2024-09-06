def get_multiplies_digits(number):
    str_number = str(number)

    if int(str_number[-1]) == 0:
        str_number = str_number[:-1]

    first = int(str_number[0])

    if len(str_number[1:]) >= 1:
        first = first * get_multiplies_digits(int(str_number[1:]))

    return first


result1 = get_multiplies_digits(40203)
result2 = get_multiplies_digits(4020300)
print(result1)
print(result2)
