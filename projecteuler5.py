def find_evenly_divisible_num(a,b):  ## function to find samllest positive number that is evenly divisible by all of the numbers from 1 to 20
    
    smallest_num = 0 
    num = 1
    while True:
        count = 0
        for div in range(a,b+1):
            if num % div == 0: ## check , can num divisible by div or not
                count += 1
            else:
                break  ## if its not , break the loop
        if count == b - a + 1:
            smallest_num = num
            break
        num += 1
    return smallest_num

print(find_evenly_divisible_num(1,20))  ## print the smallest number