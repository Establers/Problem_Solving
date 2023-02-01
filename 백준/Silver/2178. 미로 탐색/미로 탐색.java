
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[] dx = {1, -1, 0, 0};
	static 	int[] dy = {0, 0, 1, -1};
	static int[][] graph;
	static int n;
	static int m;
	static boolean[][] visited;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader
				(new InputStreamReader(System.in));
		StringTokenizer stk = null;
		
		stk = new StringTokenizer(br.readLine());
		n = Integer.parseInt(stk.nextToken());
		m = Integer.parseInt(stk.nextToken());
		
		graph = new int[n][m];

		for(int i=0; i<n; i++) {
			String s = br.readLine();
			for (int a=0; a<m; a++) {
				graph[i][a] = (s.charAt(a) - '0');
			}
		}
		
		// graph 입력완료
		
		visited = new boolean[n][m];	
		// Arrays.fill(visited, Boolean.FALSE);
		visited[0][0] = true; // 출발지
		bfs(0,0);
		System.out.println(graph[n-1][m-1]);
	}
	
	public static void bfs(int x, int y) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[]{x,y});
		
		while(!q.isEmpty()) {
			int now[] = q.poll();
			int now_x = now[0];
			int now_y = now[1];
			// dx dy
			for(int i=0; i<4; i++) {
				int new_x = now_x + dx[i];
				int new_y = now_y + dy[i];
				
				if (new_x < 0 || new_y < 0 || new_x >= n || new_y >= m) {
					continue;
				} else if(graph[new_x][new_y] != 0)
				{ 
					// System.out.println(visited[new_x][new_y]); // false
					if (visited[new_x][new_y] == false) {
						q.add(new int[]{new_x, new_y});
						graph[new_x][new_y] = graph[now_x][now_y]+ 1; 
						visited[new_x][new_y] = true;
					}
				}
			}
		}

	}
	
}
