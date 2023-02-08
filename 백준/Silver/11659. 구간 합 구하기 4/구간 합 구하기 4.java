
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int m;
	static int[] arr;
	static int[] preSum;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(stk.nextToken());
		m = Integer.parseInt(stk.nextToken());
		arr = new int[n];
		preSum = new int[n+1];
		arr = Arrays.stream(br.readLine().split(" "))
				.mapToInt(x -> Integer.parseInt(x))
				.toArray();
		
		preSum[1] = arr[0];
		
		for(int i=1; i<n; i++) {
			preSum[i+1] += preSum[i] + arr[i]; 
		}
		
		// System.out.println(Arrays.toString(preSum));
		
		for(int t=0; t<m; t++) { // from to
			stk = new StringTokenizer(br.readLine(), " ");
			int from = Integer.parseInt(stk.nextToken());
			int to = Integer.parseInt(stk.nextToken());
			
			int result = preSum[to] - preSum[from-1]; 
			sb.append(result+ "\n");
		}
		
		System.out.print(sb.toString());
	}
}
