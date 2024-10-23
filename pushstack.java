import java.util.Stack;

class Example {
    public static void main(String[] args) {
        // Create a stack object
        Stack<Object> stack = new Stack<>();
        
        // Create an object to push
        String obj1 = "Object 1";
        Integer obj2 = 100;
        
        // Push objects into the stack
        stack.push(obj1);
        stack.push(obj2);
        
        // Display the stack
        System.out.println("Stack after pushing objects: " + stack);
    }
}
