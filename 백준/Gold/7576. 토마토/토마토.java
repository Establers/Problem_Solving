import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n,m;
	static int[][] board;
	static boolean[][] visited;
	static Queue<int[]> q = new ArrayDeque<>();
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	public static void bfs() {
		// 1이 있는 위치 넣기
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(board[i][j] == 1) {
					q.add(new int[] {i, j});  
				}
			}
		}
		
		while(!q.isEmpty()) {
			int[] now = q.poll();
			int x = now[0];
			int y = now[1];
			
			for(int i=0; i<4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if(0<= nx && nx < n && 0 <= ny && ny < m) {
					// 경계안
					if(!visited[nx][ny] && board[nx][ny] == 0) {
						// 방문하지 않았고, 토마토가 들어있는 칸 일 경우
						visited[nx][ny] = true;
						board[nx][ny] = board[x][y] + 1;
						q.add(new int[] {nx, ny});
					}
				}
			}
			
		}
		
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		m = Integer.parseInt(stk.nextToken()); // 6
		n = Integer.parseInt(stk.nextToken()); // 4
		
		board = new int[n][m];
		visited = new boolean[n][m];
		
		int cnt = 0;
		int max_value = 0;
		for(int i=0; i<n; i++) {
			stk = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				int temp = Integer.parseInt(stk.nextToken());
				cnt += temp;
				board[i][j] = temp;
			}
		}
		// board 정보 다 받음
		
		bfs();
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				max_value = Math.max(max_value, board[i][j]);
				if(board[i][j] == 0) {
					System.out.println(-1);
					return;
				}
			}
		}
		
		System.out.println(max_value - 1);
		
	}
}