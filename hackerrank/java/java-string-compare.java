/**
* problem: https://www.hackerrank.com/challenges/java-string-compare
*
* @author Shovra Das
*/
import java.util.Scanner;

public class Solution {
    public static String getSmallestAndLargest(String s, int k) {
        String smallest, largest;
        smallest = largest = s.substring(0, k);
        for(int i=1; i<s.length()-k+1; ++i){
            String substr = s.substring(i, i+k);
            if(substr.compareTo(smallest) < 0)
                smallest = substr;
            if(substr.compareTo(largest) > 0)
                largest = substr;
        }        
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}