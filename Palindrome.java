import java.util.Scanner;

public class PalindromeNumber {
    public static boolean isPalindrome(int number) {
        if (number < 0) {
            return false; // Negative numbers are not palindromes
        }

        int originalNumber = number;
        int reversedNumber = 0;

        while (number != 0) {
            int digit = number % 10;
            // Build the reversed number digit by digit
            reversedNumber = reversedNumber * 10 + digit;
            // Remove the last digit from the original number
            number /= 10;
        }

        // Check if the original number is equal to its reverse
        return originalNumber == reversedNumber;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number to check if it's a palindrome: ");
        int userNumber = scanner.nextInt();

        boolean result = isPalindrome(userNumber);

        if (result) {
            System.out.println(userNumber + " is a palindrome.");
        } else {
            System.out.println(userNumber + " is not a palindrome.");
        }

        scanner.close();
    }
}