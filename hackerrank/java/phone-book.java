// https://www.hackerrank.com/challenges/phone-book

import java.util.*;
import java.io.*;

class Solution{
	public static void main(String []argh)
	{
		Scanner in = new Scanner(System.in);
		int n=in.nextInt();
		in.nextLine();
        
        Map<String,Integer> phoneBook=new HashMap<String,Integer>();
		for(int i=0;i<n;i++)
		{
			String name=in.nextLine();
			Integer phone=in.nextInt();
            phoneBook.put(name, phone);
			in.nextLine();
		}
		while(in.hasNext())
		{
			String s=in.nextLine();
            Integer phone = phoneBook.get(s);
            if(phone == null)
                System.out.println("Not found");
            else
                System.out.println(s + "=" + phone);
		}
	}
}