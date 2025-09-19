def fibonacci_even_sum(limit):  ## function to get sum of the even-valued terms in fibonacci sequence
    a = 1
    b = 2
    total = 0

    while True:
        if b > limit:  ## check, term will not exceed four million
            break

        if b % 2 == 0:
            total += b  ## get the sum of even terms
        a , b = b , b + a

    return total  ## return the total 

print(fibonacci_even_sum(4000000))  ## print the sum of all even terms