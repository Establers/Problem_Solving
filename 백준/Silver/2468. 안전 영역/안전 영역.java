import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[][] board;
	static boolean[][] visited;
	static int[] dx = {1,-1, 0 ,0};
	static int[] dy = {0,0, -1 ,1};
	static int N;
	static Queue<int[]> q = null;
//	static int water;
	static int max_heigth;
	static int answer;
	
	public static void bfs(int x, int y, int water) {
		Queue<int[]> q = new ArrayDeque<>();
		
		q.add(new int[] {x, y});
		visited[x][y] = true; 
		while(!q.isEmpty()) {
			int[] now = q.poll();
			
			for(int i=0; i<4; i++) {
				int nx = now[0] + dx[i];
				int ny = now[1] + dy[i];
				
				if(0<= nx && nx< N && 0<=ny && ny < N) {
					if(!visited[nx][ny] && board[nx][ny] > water) { // 색칠안된 영역
						visited[nx][ny] = true;
						q.add(new int[] {nx, ny});
					}
				}
			}
		}	
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(stk.nextToken());
		board = new int[N][N];
		visited = new boolean[N][N];
		int temp = 0;
		
		for(int i=0; i<N; i++) {
			stk = new StringTokenizer(br.readLine());
			for(int j=0; j<N; j++) {
				temp = Integer.parseInt(stk.nextToken());
				board[i][j] = temp;
				max_heigth = Math.max(max_heigth, temp);
			}
		}
		
		for(int w=0; w<max_heigth; w++) {
			int count = 0;
			visited = new boolean[N][N];
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(!visited[i][j] && board[i][j] > w) {
						bfs(i, j, w);
						count += 1;
					}
				}
			}
			answer = Math.max(count, answer);
		}

		System.out.println(answer);
		
	}
}
