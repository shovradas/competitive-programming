// https://www.hackerrank.com/challenges/tree-postorder-traversal/problem

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

    public static void postOrder(Node root) {
        Stack<Node> stack = new Stack<Node>();
        Stack<Node> outStack = new Stack<Node>();
        Node curr;

        stack.push(root);        
        while(!stack.empty()){
            curr = stack.pop();
            outStack.push(curr);

            if(curr.left != null)
                stack.push(curr.left);

            if(curr.right != null)
                stack.push(curr.right);
        }

        while(!outStack.empty()){
            curr = outStack.pop();
            System.out.print(curr.data + " ");
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
        postOrder(root);
    }	
}