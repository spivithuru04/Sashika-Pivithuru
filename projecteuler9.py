def pythagorean_triplet_product():  ## function to find the pythagorean triplet product
    x = 0
    for a in range(1,1001):
        for b in range(a,1001):
            for c in range(b,1001):
                if a**2 + b**2 == c**2 and a+b+c == 1000:  ## check pythagorean triplet and other condition
                    product = a*b*c  ## calculate the product
                    x = 1
                    break
            if x == 1:
                break
        if x == 1:
            break
    return product

print(pythagorean_triplet_product())  ## print the pythagorean triplet product