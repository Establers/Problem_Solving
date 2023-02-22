import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int t;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static int[][] board;
	static ArrayList<Integer> answers = new ArrayList<>();
	static boolean[][] visited;
	static int m,n;
	
	public static void dfs(int x, int y) {
		
		for(int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if(0 <= nx && nx < n && 0 <= ny && ny < m) {
				// 경계안
				if(!visited[nx][ny] && board[nx][ny] != 0) {
					visited[nx][ny] = true;
					dfs(nx, ny);
				} 
			} 
		}
	}
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		
		for(int tc = 0; tc < t; tc++) {
			StringTokenizer stk = new StringTokenizer(br.readLine());
			m = Integer.parseInt(stk.nextToken());
			n = Integer.parseInt(stk.nextToken());
			int k = Integer.parseInt(stk.nextToken()); // 배추 개수
			
			board = new int[n][m]; 
			visited = new boolean[n][m];
			
			for(int i=0; i<k; i++) {
				stk = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(stk.nextToken());
				int b = Integer.parseInt(stk.nextToken());
				board[b][a] = 1; 
			}
			int count = 0;
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					if(!visited[i][j] && board[i][j] != 0) {
						dfs(i,j);
						count++;
					}
				}
			}
			
			System.out.println(count);
		}
		
		
		
	}
}