def find_prime_num(position):  ## function to find the 10001st prime number

    count = 0
    number = 2

    while True:
        for div in range(2,int(number**0.5)+1):
            if number % div == 0:  ## check , is number prime or not
                break
        else:
            count += 1
        if count == position:
            break
        number += 1
    return number

print(find_prime_num(10001))  ## print relevent position prime number