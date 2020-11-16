// https://www.hackerrank.com/challenges/java-strings-introduction
/**
* problem: 
*
* @author  Shovra Das
*/
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        
        System.out.println(A.length() + B.length());
        
        if(A.compareTo(B)>0)
            System.out.println("Yes");
        else
            System.out.println("No");
        
        A = (char)((int)(A.charAt(0))-32) + A.substring(1);
        B = (char)((int)(B.charAt(0))-32) + B.substring(1);
        System.out.println(A + " " + B);
    }
}