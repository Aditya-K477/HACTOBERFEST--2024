def evalRPN(tokens):
    stack = []

    # Define the valid operators and corresponding operations
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            # Pop the last two operands from the stack
            b = stack.pop()
            a = stack.pop()

            # Perform the operation based on the token (operator)
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Perform division and truncate towards zero
                stack.append(int(a / b))  # int() truncates towards zero for Python

        else:
            # It's an operand, push it onto the stack
            stack.append(int(token))

    # The last remaining element in the stack is the result
    return stack[0]

# Example usage:
tokens1 = ["2", "1", "+", "3", "*"]
tokens2 = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens1))  # Output: 9
print(evalRPN(tokens2))  # Output: 6
