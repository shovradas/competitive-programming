/**
* problem: https://www.hackerrank.com/challenges/java-list
*
* @author  Shovra Das
*/
import java.util.Scanner;
import java.util.List;
import java.util.LinkedList;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);        
        List<Integer> list = new LinkedList<>();
        
        int n = in.nextInt();
        for(int i=0; i<n; ++i)
            list.add(in.nextInt());
            
        int q = in.nextInt();
        for(int i=0; i<q; ++i)
            if(in.next().equals("Insert"))
                list.add(in.nextInt(), in.nextInt());
            else
                list.remove(in.nextInt());
            
        for(int item: list)
            System.out.print(item + " ");
    }
}