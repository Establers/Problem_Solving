// n queen
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static int[] x;
	public static int n;
	public static int result = 0;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());		
		x = new int[16]; // 1~15

		backtracking(0, x);
		System.out.println(result);

	}
	
	
	public static void backtracking (int depth, int[] x) { 
		if(promising(depth, x)) {
			if(depth == n) {
				result += 1;
			} else
			{
				for(int i=1; i<n+1; i++) {
					x[depth+1] = i;
					backtracking(depth+1, x);
				}
			}
		}
	}
	
	public static boolean promising(int depth, int[] x) {
		boolean flag = true;
		int k = 1;
		while(k < depth && flag) {
			if(x[k] == x[depth] || Math.abs(x[depth] - x[k]) == (depth-k)) {
				flag = false;
			}
			k += 1;
		}
		return flag;
	}
}
