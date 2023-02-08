
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int m;
	static int[][] arr;
	static int[][] preSum;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(stk.nextToken());
		m = Integer.parseInt(stk.nextToken()); // test case
		
		arr = new int[n][n];
		
		for(int i=0; i<n; i++) {
			stk = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<n; j++) {
				arr[i][j] = Integer.parseInt(stk.nextToken());
			}
		}
				
		
		preSum = new int[n+1][n+1];
		
		for(int i=1; i<=n; i++) {
			preSum[i][1] = arr[i-1][0];
			for(int j=1; j<n; j++) {
				preSum[i][j+1] = preSum[i][j] + arr[i-1][j];
			}
		}
		
		for(int i=0; i<=n; i++) {
			for(int j=1; j<=n; j++) {
				preSum[j][i] = preSum[j-1][i] + preSum[j][i];
			}
		}

		// 구간합 구현 완료

		// 구간합 확인용 출력
//		for(int[] a : preSum) {
//			for(int b : a) {
//				System.out.print(b+" ");
//			}
//			System.out.println();
//		}
//		System.out.println();
		
		// test case
		for(int i=0; i<m; i++) {
			stk = new StringTokenizer(br.readLine(), " ");
		
			int x1 = Integer.parseInt(stk.nextToken());
			int y1 = Integer.parseInt(stk.nextToken());
			int x2 = Integer.parseInt(stk.nextToken());
			int y2 = Integer.parseInt(stk.nextToken());
			int result = 0;
//			if(x1 == 0 && y1 == 0) {
//				result = preSum[x2][y2];
//			} else if(x1 == x2 && y1 == y2){
//				result = arr[x1][y1]; 
//			} else{
//				result = 
//						preSum[x2][y2] 
//								- preSum[x1-1][y2] 
//								- preSum[x2][y1-1]
//								+ preSum[x1-1][y1-1];
//			}
			
			result = 
					preSum[x2][y2] 
							- preSum[x1-1][y2] 
							- preSum[x2][y1-1]
							+ preSum[x1-1][y1-1];
			System.out.println(result);
			
		}
	}
}
