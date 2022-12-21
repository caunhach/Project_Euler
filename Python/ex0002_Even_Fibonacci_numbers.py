def fibonacci (n):
    if n == 1: return 1
    elif n == 2:return 2
    return fibonacci (n - 1) + fibonacci (n - 2)
def sum_even_fibonacci (max_value):
    i = 1
    sum = 0
    while (fibonacci (i) < 4000000):
        if (fibonacci (i) % 2 == 0):
            sum += fibonacci (i)
        i += 1
    return sum
print("the sum of the even-valued fibonacci that does not exceed four million is {}".format(sum_even_fibonacci (4000000)))