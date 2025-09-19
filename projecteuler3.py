def find_largest_p_f(number):  ## function for finding largest prime factor
    largest_p_f = 0
    for factor in range(2,int(number**0.5)+1):
        if number % factor == 0:  ## check , is factor a factor of number
            for div in range(2,int(factor**0.5)+1):
                if factor % div == 0:  ## check , can factor divide from div
                    break  ## when it is true , break the loop
            else:
                if factor > largest_p_f:
                    largest_p_f = factor  ##  save the largest prime factor
    
    return largest_p_f

print(find_largest_p_f(600851475143))  ## print the largest prime factor

