/**
* problem: https://www.hackerrank.com/challenges/java-string-reverse
*
* @author Shovra Das
*/
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {        
        Scanner sc=new Scanner(System.in);
        String s = sc.next();      
        String reversed = new StringBuilder(s).reverse().toString();          
        System.out.println(s.equals(reversed) ? "Yes" : "No");
    }
}