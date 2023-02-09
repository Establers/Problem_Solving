
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	static int n;
	static int[][] menus;
	static boolean[] visited;
	static int result = Integer.MAX_VALUE;
	
	public static void cal(int depth, int sum1, int sum2) {
		if(depth == n) {
			if(sum1 == 0 || sum2 == 0) return;
			// System.out.println(sum1 + " " + sum2);
			int temp = Math.abs(sum1 - sum2);
			result = Math.min(result, temp);
			return;
		}
		
		visited[depth] = true;
		cal(depth+1, sum1 * menus[depth][0], sum2 + menus[depth][1]);
		
		visited[depth] = false;
		cal(depth+1, sum1 , sum2);

	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		menus = new int[n][2];
		visited = new boolean[n];
		
		for(int i=0; i<n; i++) {
			StringTokenizer stk = new StringTokenizer(br.readLine());
			menus[i][0] = Integer.parseInt(stk.nextToken());
			menus[i][1] = Integer.parseInt(stk.nextToken());
		}
		
		cal(0, 1, 0);
		System.out.println(result);
		
	}
}
