def double(n):  # function to multiply the number N times
    return lambda a: a * n  # a times n

func = double(2)  # multiplying number 2, a times
print(func(4))  # giving number of times to multiply