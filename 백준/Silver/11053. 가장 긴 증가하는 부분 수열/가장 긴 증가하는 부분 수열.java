import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer> nums = new ArrayList<>();
		
		StringTokenizer stk = null;
		stk = new StringTokenizer(br.readLine(), " ");
		for(int a=0; a<n; a++) {
			nums.add(Integer.parseInt(stk.nextToken()));
		}
		
		int[] dp = new int[n+1];
		// int result = 0;
		int result = 1;
		
		for(int i=0; i<n+1; i++) {
			dp[i] = 1;
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<i; j++) {
				if(nums.get(i) > nums.get(j)) {
					dp[i] = Math.max(dp[i], dp[j] + 1);
					
				}
			}
			result = Math.max(dp[i], result);
		}
        /*
		for(int i=0; i<n+1; i++) {
			System.out.print(dp[i]+" ");
		}
        */
		System.out.print(result);
	}
}