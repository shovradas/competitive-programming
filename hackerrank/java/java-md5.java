/**
* problem: https://www.hackerrank.com/challenges/java-md5
*
* @author Shovra Das
*/
import java.util.Scanner;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Solution {
    public static void main(String[] argh) throws NoSuchAlgorithmException{
        Scanner in = new Scanner(System.in);
        String s = in.next();        

        MessageDigest md5 = MessageDigest.getInstance("MD5");
        md5.update(s.getBytes());
        
        StringBuilder encodedString = new StringBuilder();
        for(byte b : md5.digest())
            encodedString.append(String.format("%02x", b));
        
        System.out.print(encodedString);
    }
}
