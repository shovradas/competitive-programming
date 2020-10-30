// https://www.hackerrank.com/challenges/tree-inorder-traversal/problem

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

    public static void inOrder(Node root) {
        Stack<Node> stack = new Stack<Node>();
        
        Node curr = root;
        while(curr!=null || !stack.empty()){            
            while(curr != null){
                stack.push(curr);
                curr = curr.left;                
            }
            curr = stack.pop();
            System.out.print(curr.data + " ");

            curr = curr.right;
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
        inOrder(root);
    }	
}