import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.PrimitiveIterator.OfDouble;

import org.w3c.dom.css.ElementCSSInlineStyle;

public class Main {
	
	static int n, r, c, count;
	static int[][] board;
	static int answer = 0;
	static boolean flag = false;
	
	public static void divide(int n, int x_idx, int y_idx) { // 3일때  8
		if(n == 1) return;		
		
		if(x_idx < n/2 && y_idx < n/2) {
			divide(n/2, x_idx, y_idx);
		} else if (x_idx < n/2 && y_idx >= n/2) {
			answer += ((int)Math.pow(n, 2))/4;
			divide(n/2, x_idx, y_idx - n/2);
					
		} else if (x_idx >= n/2 && y_idx < n/2) {
			answer += ((int)Math.pow(n, 2))/4 * 2;
			divide(n/2, x_idx - n/2, y_idx);
					
		} else if (x_idx >= n/2 && y_idx >= n/2){
			answer += ((int)Math.pow(n, 2))/4 * 3;
			divide(n/2, x_idx - n/2, y_idx - n/2); 
		}	
		
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
				
		n = Integer.parseInt(stk.nextToken());
		r = Integer.parseInt(stk.nextToken());
		c = Integer.parseInt(stk.nextToken());
		int temp = (int)Math.pow(2, n);
		
		divide(temp, r, c);
		System.out.println(answer);
	}
	
}