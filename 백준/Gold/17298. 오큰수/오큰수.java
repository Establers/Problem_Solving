
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		int[] nums = new int[n];
		
		Stack<Integer> stack = new Stack<Integer>();
		StringTokenizer stk = new StringTokenizer(br.readLine());
				
		for(int i=0; i<n; i++) {
			nums[i] = Integer.parseInt(stk.nextToken()); 
		}
		
		for(int i = 0; i<n; i++) {
			while(!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
				nums[stack.pop()] = nums[i];
			}
			
			stack.push(i);
		}
		
		while(!stack.isEmpty()) {
			nums[stack.pop()] = -1;
		}
		
		for(int i = 0; i < n; i++) {
			sb.append(nums[i]).append(' ');
		}
		
		
		System.out.println(sb.toString());
	}
}
