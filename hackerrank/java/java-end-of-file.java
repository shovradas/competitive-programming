/**
* problem: https://www.hackerrank.com/challenges/java-end-of-file
*
* @author Shovra Das
*/

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for(int i=1; in.hasNext() ;++i)
            System.out.println(i + " " + in.nextLine());
    }
}