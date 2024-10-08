/* Input: The user inputs a number.
Reverse Calculation: The while loop extracts each digit of the input number and constructs the reversed number.
Palindrome Check: After reversing, the original number is compared to the reversed number to check if it’s a palindrome.*/


import java.util.Scanner;

public class ReverseAndCheckPalindrome {
    public static void main(String[] args) {
        int num, digit, rev = 0;

        // Input from user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a positive number: ");
        num = scanner.nextInt();
        int n = num;

        // Reverse the number
        while (num != 0) {
            digit = num % 10;
            rev = (rev * 10) + digit;
            num = num / 10;
        }

        // Output the reversed number
        System.out.println("The reverse of the number is: " + rev);

        // Check if the number is a palindrome
        if (n == rev) {
            System.out.println("The number is a palindrome.");
        } else {
            System.out.println("The number is not a palindrome.");
        }

        scanner.close();
    }
}
