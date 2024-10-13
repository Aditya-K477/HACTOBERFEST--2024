def isArmstrong(N):  #defining a function for checking if the number is armstrong or not
    original = N
    k = N
    sum = 0
    count = 0
    while N != 0:
        N = N // 10
        count += 1  ##for counting the number of digits in the fivin number

    while k != 0:
        a = k % 10 #finding individual digits using mathematical technique to extract all digits one by one
        k = k // 10
        sum += a ** count

    if sum == original:
        return True
    else:
        return False
while True:  #using a while loop to check for armstrong infinite number of times
    inp = int(input("Enter the number to be checked\n"))
    if isArmstrong(inp) == True:
        print(f"{inp} is an armstrong number")
    else:
        print(f"{inp} is not an armstrong number")

