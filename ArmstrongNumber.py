def is_armstrong_number(num):
    # Find the number of digits in the number
    original_num = num
    power = len(str(num))  # The number of digits in the number (this step can't be avoided)
    
    total = 0
    while num > 0:
        digit = num % 10  # Get the last digit
        total += digit ** power  # Add the digit raised to the power of number of digits
        num //= 10  # Remove the last digit

    # Check if the total is equal to the original number
    return total == original_num

#  Take use input and Continuous loop to check multiple numbers
if __name__ == "__main__":
    while True:
        number = input("Enter a number to check if it's an Armstrong number (or 'q' to quit): ")
        
        if number.lower() == 'q':  
            print("Exiting the program.")
            break

        try:
            number = int(number)
            if is_armstrong_number(number):
                print(f"{number} is an Armstrong number.")
            else:
                print(f"{number} is not an Armstrong number.")
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")