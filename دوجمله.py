def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def symbolic_expansion(n):
    expansion = ""
    for k in range(n + 1):
        coefficient = binomial_coefficient(n, k)
        if coefficient != 1:
            expansion += str(coefficient)
        expansion += "x"
        if n - k > 1:
            expansion += "^{" + str(n - k) + "}"
        elif n - k == 1:
            expansion += ""
        if k > 0:
            expansion += "y"
            if k > 1:
                expansion += "^{" + str(k) + "}"
            elif k == 1:
                expansion += ""
        if k < n:
            expansion += " + "
    return expansion

n = int(input("Enter the value of n: "))
print(symbolic_expansion(n))
