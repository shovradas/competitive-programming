/**
 * problem: https://www.hackerrank.com/challenges/java-lambda-expressions
 *
 * @author Shovra Das
 */
import java.io.*;
import java.util.*;

interface PerformOperation {
    boolean check(int a);
}

class MyMath {
    public static boolean checker(PerformOperation p, int num) {
        return p.check(num);
    }
    
    public PerformOperation isOdd() {
        return (int num) - > (num & 1) == 1;
    }

    public PerformOperation isPrime() {
        return (int num) - > {
            boolean prime = true;
            for (int i = 2; i < Math.sqrt(num); ++i)
                if (num % i == 0) {
                    prime = false;
                    break;
                }
            return prime;
        };
    }

    public PerformOperation isPalindrome() {
        return (int num) - > {
            String numString = String.valueOf(num);
            String reversedNumString = new StringBuilder(numString).reverse().toString();
            return numString.equals(reversedNumString);
        };
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        MyMath ob = new MyMath();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        PerformOperation op;
        boolean ret = false;
        String ans = null;
        while (T-- > 0) {
            String s = br.readLine().trim();
            StringTokenizer st = new StringTokenizer(s);
            int ch = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            if (ch == 1) {
                op = ob.isOdd();
                ret = ob.checker(op, num);
                ans = (ret) ? "ODD" : "EVEN";
            } else if (ch == 2) {
                op = ob.isPrime();
                ret = ob.checker(op, num);
                ans = (ret) ? "PRIME" : "COMPOSITE";
            } else if (ch == 3) {
                op = ob.isPalindrome();
                ret = ob.checker(op, num);
                ans = (ret) ? "PALINDROME" : "NOT PALINDROME";

            }
            System.out.println(ans);
        }
    }
}
