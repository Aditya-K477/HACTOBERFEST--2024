def reverse_number(N): ##defining a function for making the reversed number
    reversed_num=0
    temp=N
    while temp!=0:
        last_digit=temp%10 ##EXTRACTION OF DIGITS ONE BY ONE
        temp=temp//10
        reversed_num=reversed_num*10+last_digit ##MAKING OF THE NEW NUMBER
    return reversed_num
def isPalindrome(N): ##DEFINING ANOTHER FUNCTION FOR CALLING FIRST FUNCTION FOR CHECKING IF THE NUMBER WAS PALINDROME OR NOT
    return(N==reverse_number(N))
a=int(input("ENTER THE NUMBER TO BE CHECKED\n")) 
if isPalindrome(a)==True:                          ##USING IF-ELSE LADDER FOR PRINTING THE OUTPUT
    print("THE GIVEN NUMBER IS A PALINDROME.")
else:
    print("THE GIVEN NUMBER IS NOT A PALINDROME.")