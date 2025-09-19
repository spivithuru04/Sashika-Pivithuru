def multiple_sum(n):

    total = 0

    for num in range(1,1000):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    
    return total

print(multiple_sum(1000))

