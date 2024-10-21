def printFibonacciNumbers(n):
    f1 = 0
    f2 = 1
    if n < 1:
        return
    print(f1, end=" ")
    for x in range(1, n):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next

printFibonacciNumbers(7)
