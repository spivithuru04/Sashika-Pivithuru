def multiple_sum(n):  ## create a function to get the sum of all the multiples of 3 or 5 below 1000

    total = 0

    for num in range(1,1000):
        if num % 3 == 0 or num % 5 == 0:  ## check , can num divide by 3 or 5
            total += num  ## get the sum
    
    return total  ## get total from the function

print(multiple_sum(1000))  ## print the sum

