// Class representing a node of the binary tree
class Node {
           int data;
           Node left, right;
       
           // Constructor to create a new node
           public Node(int item) {
               data = item;
               left = right = null;
           }
       }
       
       // Class representing the Binary Tree
       public class BinaryTreeByMansi {
           Node root;
       
           // Constructor to initialize the root of the tree
           public BinaryTreeByMansi() {
               root = null;
           }
       
           // Method to insert a new node in the tree
           public void insert(int data) {
               root = insertRec(root, data);
           }
       
           // Recursive method to insert a new node in the binary tree
           Node insertRec(Node root, int data) {
               if (root == null) {
                   root = new Node(data);
                   return root;
               }
       
               if (data < root.data) {
                   root.left = insertRec(root.left, data);
               } else if (data > root.data) {
                   root.right = insertRec(root.right, data);
               }
       
               return root;
           }
       
           // Method to perform inorder traversal of the tree
           public void inorder() {
               inorderRec(root);
           }
       
           // Recursive method for inorder traversal
           void inorderRec(Node root) {
               if (root != null) {
                   inorderRec(root.left);
                   System.out.print(root.data + " ");
                   inorderRec(root.right);
               }
           }
       
           // Method to perform preorder traversal of the tree
           public void preorder() {
               preorderRec(root);
           }
       
           // Recursive method for preorder traversal
           void preorderRec(Node root) {
               if (root != null) {
                   System.out.print(root.data + " ");
                   preorderRec(root.left);
                   preorderRec(root.right);
               }
           }
       
           // Method to perform postorder traversal of the tree
           public void postorder() {
               postorderRec(root);
           }
       
           // Recursive method for postorder traversal
           void postorderRec(Node root) {
               if (root != null) {
                   postorderRec(root.left);
                   postorderRec(root.right);
                   System.out.print(root.data + " ");
               }
           }
       
           // Main method to run the program
           public static void main(String[] args) {
               BinaryTreeByMansi tree = new BinaryTreeByMansi();
       
               /* Inserting nodes into the binary tree */
               tree.insert(50);
               tree.insert(30);
               tree.insert(20);
               tree.insert(40);
               tree.insert(70);
               tree.insert(60);
               tree.insert(80);
       
               // Displaying the tree using different traversal methods
               System.out.println("Inorder traversal of the binary tree:");
               tree.inorder();
               System.out.println();
       
               System.out.println("Preorder traversal of the binary tree:");
               tree.preorder();
               System.out.println();
       
               System.out.println("Postorder traversal of the binary tree:");
               tree.postorder();
           }
       }
       

