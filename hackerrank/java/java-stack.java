/**
* problem: https://www.hackerrank.com/challenges/java-stack
*
* @author Shovra Das
*/
import java.util.*;

class Solution{
	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);		
		while (sc.hasNext()) {
			String expr = sc.next();
            
            Stack<Character> stack = new Stack<>();            
            for(char ch: expr.toCharArray()){
                if(stack.empty()){
                    stack.push(ch);
                    continue;
                }                    
                if(ch==']' && stack.peek()=='[')
                    stack.pop();
                else if(ch=='}' && stack.peek()=='{')
                    stack.pop();
                else if (ch==')' && stack.peek()=='(')
                    stack.pop();
                else
                    stack.push(ch);
            }
            System.out.println(stack.empty());
		}
	}
}
