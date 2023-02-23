import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int R, C;
	static int[][] board;
	static boolean[] visited; 
	static int answer;
	
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	public static void dfs(int x, int y, int length) {
		answer = Math.max(answer, length);
		visited[board[x][y]] = true; 
		for(int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if(0<= nx && nx < R && 0<= ny && ny < C) {
				if(!visited[board[nx][ny]]) {
					visited[board[nx][ny]]=true;
					dfs(nx, ny, length+1);
					visited[board[nx][ny]]=false;
				}
			}
			
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(stk.nextToken());
		C = Integer.parseInt(stk.nextToken());
		
		board = new int[R][C];
		visited = new boolean[27]; // A~Z
		
		for(int i=0; i<R; i++) {
			String temp = br.readLine();
			for(int j=0; j<C; j++) {
				board[i][j] = temp.charAt(j) - 'A'; 
			}
		}
		// Input end
		
		dfs(0, 0, 1);
		System.out.println(answer);
	
	}
}