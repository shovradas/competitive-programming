/**
* problem: https://www.hackerrank.com/challenges/java-static-initializer-block
*
* @author Shovra Das
*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static int B;
    static int H;
    static boolean flag = true;

    static {        
        Scanner in = new Scanner(System.in);
        Solution.B = in.nextInt();
        Solution.H = in.nextInt();
        
        try{
            if(Solution.B<=0 || Solution.H <=0)        
                throw new Exception("Breadth and height must be positive");            
        } catch(Exception ex){
            System.out.print(ex);
            Solution.flag = false;
        }
    }

    public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}		
	}//end of main
}//end of class