/**
* problem: https://www.hackerrank.com/challenges/sha-256
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

        MessageDigest sha256 = MessageDigest.getInstance("SHA-256");
        sha256.update(s.getBytes());

        StringBuilder encodedString = new StringBuilder();
        for(byte b : sha256.digest())
            encodedString.append(String.format("%02x", b));

        System.out.print(encodedString);
    }
}