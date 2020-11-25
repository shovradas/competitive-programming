/**
* problem: https://www.hackerrank.com/challenges/tree-top-view
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

	public static void topView(Node root) {
        class XNode extends Node{            
            int vlevel;

            XNode(Node node, int vlevel){
                super(node.data);
                super.left = node.left;
                super.right = node.right;
                this.vlevel = vlevel;
            }
        }

        TreeMap<Integer, XNode> topView = new TreeMap<>();

        Queue<XNode> queue = new LinkedList<>();
        queue.add(new XNode(root, 0));
        while(!queue.isEmpty()){
            XNode curr = queue.poll();

            if(!topView.containsKey(curr.vlevel))
                topView.put(curr.vlevel, curr);
            
            if(curr.left != null)
                queue.add(new XNode(curr.left, curr.vlevel-1));

            if(curr.right != null)
                queue.add(new XNode(curr.right, curr.vlevel+1));
        }

        for(Map.Entry entry: topView.entrySet()){
            XNode node = (XNode)entry.getValue();
            System.out.print(node.data + " ");            
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
        topView(root);
    }	
}