def sum_multiple_3or5 (n):
    sum = 0
    for i in range(1, n):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum
print( "the sum of all the multiples of 3 or 5 below 1000. is {}".format(sum_multiple_3or5(1000)) )