
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int v;
	static int e;
	static boolean[] visited;
	static boolean[][] graph;
	static int cnt;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		v = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		e = Integer.parseInt(st.nextToken());
		graph = new boolean[v+1][v+1];
		visited = new boolean[v+1];
		cnt = 0;
		for(int i=0; i<e; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph[a][b] = true;
			graph[b][a] = true;
		}
		
		bfs();
		System.out.println(cnt);
	}
	
	public static void bfs() {
		Queue<Integer> q = new LinkedList<>();
		// 1번부터 시작
		q.add(1);
		visited[1] = true;
		
		while(!q.isEmpty()) {
			int now = q.poll();
			
			for(int i=1; i<= v; i++) {
				if(!visited[i] && graph[now][i]) {
					q.add(i);
					visited[i] = true;
					cnt += 1;
				}
			}
		}
		
	}
}
