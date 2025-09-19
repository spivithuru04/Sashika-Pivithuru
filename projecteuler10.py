def sum_of_primes(limit):  ## function to find the sum of all the primes below two million.

    total = 0

    for number in range(2,limit):
        for div in range(2,int(number**0.5)+1):  ## check, is the number prime or not
            if number % div == 0:
                break
        else:
            total += number  ## calculate the sum
    
    return total

print(sum_of_primes(2000000))  ## print the sum of primes