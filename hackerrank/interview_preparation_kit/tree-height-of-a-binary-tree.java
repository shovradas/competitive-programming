/**
* problem: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree
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

	public static int height(Node root) {
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(root);

        int depth = -1;
        while(queue.size() != 0){
            ++depth;
            int breadthNodeCount = queue.size();            
            while(breadthNodeCount != 0){
                Node current = queue.peek();
                queue.remove();

                if(current.left != null)
                    queue.add(current.left);
                if(current.right != null)
                    queue.add(current.right);

                --breadthNodeCount;
            }
        }

        return depth;
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
        int height = height(root);
        System.out.println(height);
    }	
}