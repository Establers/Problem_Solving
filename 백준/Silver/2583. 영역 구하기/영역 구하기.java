import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	static int[][] board;
	static boolean[][] visited;
	static int[] dx = {1,-1, 0 ,0};
	static int[] dy = {0,0, -1 ,1};
	static int M;
	static int N;
	static ArrayList<Integer> arrayList = new ArrayList<>();
	static int area;
	
	public static void dfs(int x, int y, int length) {
		area++;
		visited[x][y] = true;
		
		for(int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if(0<= nx && nx< M && 0<=ny && ny < N) {
				if(!visited[nx][ny] && board[nx][ny] == 0) { // 색칠안된 영역
					visited[nx][ny] = true;
					dfs(nx, ny, length);
				}
			}
		}
	}
	
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		M = Integer.parseInt(stk.nextToken());
		N = Integer.parseInt(stk.nextToken());
		int K = Integer.parseInt(stk.nextToken());
		board = new int[M][N];
		visited = new boolean[M][N];
		
		for(int i=0; i<K; i++) {
			stk = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(stk.nextToken());
			int b = Integer.parseInt(stk.nextToken());
			int c = Integer.parseInt(stk.nextToken());
			int d = Integer.parseInt(stk.nextToken());
			
			for(int y=b; y<d; y++) {
				for(int x=a; x<c; x++) {
					board[y][x] = 1;
				}
			}
		}
		
		int count = 0;
		
		for(int i=0; i<M; i++) {
			for(int j=0; j<N; j++) {
				if (!visited[i][j] && board[i][j] == 0) {
					area = 0;
					dfs(i, j, 1);
					arrayList.add(area);
					count += 1;
				}
			}
		}
		
		System.out.println(count);
		Collections.sort(arrayList);
		for(int i : arrayList) {
			System.out.print(i+" ");
		}
		
		
	}
}
