# Implement a python program to calculate the square root of a number by Newton's Method

def squareRoot(n, l):
    x = n
    count = 0
    while True:
        count += 1
        root = 0.5 * (x + (n / x))
        if abs(root - x) < 1:
            break

        x= root
    return root

if __name__== "__main__":
    n = 378
    l = 0.00001

    print("Square root of", n,":", squareRoot(n, 1))
