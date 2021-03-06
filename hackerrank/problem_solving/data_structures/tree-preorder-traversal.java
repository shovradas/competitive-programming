/**
* problem: https://www.hackerrank.com/challenges/tree-preorder-traversal
*
* @author Shovra Das
*/
import java.util.*;
import java.io.*;

class Node {
    Node left;
    Node right;
    int data;
    
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Solution {

    public static void preOrder(Node root) {
        Stack<Node> stack = new Stack<Node>();
        stack.push(root);
        
        while(!stack.empty()){
            Node curr = stack.pop();
            System.out.print(curr.data + " ");

            if(curr.right != null)
                stack.push(curr.right);

            if(curr.left != null)
                stack.push(curr.left);
        }
    }

	public static Node insert(Node root, int data) {
        if(root == null) {
            return new Node(data);
        } else {
            Node cur;
            if(data <= root.data) {
                cur = insert(root.left, data);
                root.left = cur;
            } else {
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        Node root = null;
        while(t-- > 0) {
            int data = scan.nextInt();
            root = insert(root, data);
        }
        scan.close();
        preOrder(root);
    }	
}