package Java;
public class Fibonacci {

    // Function to print the Fibonacci series up to a given number of terms
    public static void printFibonacci(int n) {
        // Edge Case: If n is less than or equal to 0, no series should be printed
        if (n <= 0) {
            System.out.println("Input should be greater than 0");
            return;
        }

        // Initialize the first two Fibonacci numbers
        int a = 0; // First Fibonacci number
        int b = 1; // Second Fibonacci number

        // Print the first Fibonacci number (a = 0)
        if (n >= 1) System.out.print(a + " ");

        // Print the second Fibonacci number (b = 1)
        if (n >= 2) System.out.print(b + " ");

        // Loop through to calculate the next Fibonacci numbers until n terms are printed
        for (int i = 3; i <= n; i++) {
            int next = a + b; // The next number is the sum of the previous two
            System.out.print(next + " "); // Print the next number
            a = b; // Move a to b
            b = next; // Move b to the new number (next)
        }

        System.out.println(); // Print a newline after the series
    }

    // Main function to test the Fibonacci function
    public static void main(String[] args) {
        // Test Case 1: Fibonacci series up to 5 terms
        // Expected output: 0 1 1 2 3
        System.out.println("Test Case 1 (n = 5):");
        printFibonacci(5);

        // Test Case 2: Fibonacci series up to 1 term
        // Expected output: 0
        System.out.println("Test Case 2 (n = 1):");
        printFibonacci(1);

        // Test Case 3: Fibonacci series up to 10 terms
        // Expected output: 0 1 1 2 3 5 8 13 21 34
        System.out.println("Test Case 3 (n = 10):");
        printFibonacci(10);

        // Test Case 4: Edge case when n is 0
        // Expected output: Input should be greater than 0
        System.out.println("Test Case 4 (n = 0):");
        printFibonacci(0);

        // Test Case 5: Edge case when n is negative
        // Expected output: Input should be greater than 0
        System.out.println("Test Case 5 (n = -3):");
        printFibonacci(-3);
    }
}
