
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {

	static int t, n, k, max_value;
	static int[][] board;
	static boolean[][] visited;
	static ArrayList<int[]> start_point;
	
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	static int answer;
		
	public static void dfs(int x, int y, boolean cut, int length) {
		// 깎는 것,
		// 깎지 않는 것 두개의 DFS를 생성해야함
		answer = Math.max(answer, length);
		
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			
			if(0<= nx && nx < n && 0<= ny && ny < n
					&& !visited[nx][ny]) 
			{	// 조건에 만족하는 경우
				if(board[nx][ny] < board[x][y]) {
					//System.out.println("보드값 " + board[nx][ny] +" " + board[x][y]);
					// 나보다 낮은 곳 방문
					//System.out.println("now " + nx + " " + ny + " " + (length+1));
					visited[nx][ny] = true; 
					dfs(nx, ny, cut, length + 1);
					visited[nx][ny] = false;
					
				} else if(!cut){ // 깎은적이 없다면
					// 깍기
					if(board[nx][ny] - board[x][y] < k) {
						// 깎아서 갈 수 있는 길이라면
						int temp = board[nx][ny] - board[x][y]+1;
						if(temp <= k) {
							//System.out.println("temp <= k " + nx + " " + ny + " "+(length+1)+ "깎는량 " + temp);
							board[nx][ny] = board[nx][ny] - temp;
							visited[nx][ny] = true;
							dfs(nx, ny, true, length + 1);
							visited[nx][ny] = false;
							board[nx][ny] = board[nx][ny] + temp;
						} 
					}
				}
			} 
		}
	}
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			StringTokenizer stk = new StringTokenizer(br.readLine());
			n = Integer.parseInt(stk.nextToken());
			k = Integer.parseInt(stk.nextToken());
			board = new int[n][n];
			visited = new boolean[n][n];
			start_point = new ArrayList<>();
			answer = 0;
			max_value = 0;
			
			for(int i=0; i<n; i++) {
				stk = new StringTokenizer(br.readLine());
				for(int j=0; j<n; j++) {
					int temp = Integer.parseInt(stk.nextToken());
					max_value = Math.max(temp, max_value);
					board[i][j] = temp;
				}
			}
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(board[i][j] == max_value) {
						start_point.add(new int[] {i, j});
					}
				}
			}
			
			for(int[] go : start_point) {
//				System.out.print(go[0] +" "+ go[1]+ "  ");
				visited[go[0]][go[1]] = true;
				dfs(go[0], go[1], false, 1);
				visited[go[0]][go[1]] = false;
			}
			
			System.out.println("#" + tc + " " + answer);
			
		}
	}
}
