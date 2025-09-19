def find_difference_sum(a,b):  ## function to find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

    sum_of_squares = 0

    for i in range(a,b+1):
        sum_of_squares += i**2  ## get the sum of squares
    
    total = 0

    for i in range(a,b+1):
        total += i
    
    square_of_sum = total**2  ## calculate the square of sum

    difference_sum = square_of_sum - sum_of_squares  ## get the difference

    return difference_sum

print(find_difference_sum(1,100))  ## print the difference