import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = null;

		int n = Integer.parseInt(br.readLine());
		int[][] dp = new int[1001][3];
		
		// dp에 값 할당
		for(int i=0; i<n; i++) {
			stk = new StringTokenizer(br.readLine()," ");
			for(int j=0; j<3; j++) {
				dp[i][j] = Integer.parseInt(stk.nextToken());
			}			
		}
		
		// 
		for(int i=1; i<= n; i++) {
			dp[i][0] += Math.min(dp[i-1][1], dp[i-1][2]);
			dp[i][1] += Math.min(dp[i-1][2], dp[i-1][0]);
			dp[i][2] += Math.min(dp[i-1][1], dp[i-1][0]);
		}
		
		System.out.println(Arrays.stream(dp[n-1]).min().getAsInt());
	}
}