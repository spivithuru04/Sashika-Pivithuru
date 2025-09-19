def find_largest_palindrome(a,b):  ## function to find the largest palindrome

    largest_palindrome = 0

    if a > b:
        a , b = b , a

    for i in range(10**a):
        for j in range(i,10**b):
            if i*j == int(str(i*j)[::-1]):  ## check the palindrome qaulities
                if i*j > largest_palindrome:
                    largest_palindrome = i*j  ## save the largest palindrome
    
    return largest_palindrome

print(find_largest_palindrome(3,3))  ## print the largest palindrome