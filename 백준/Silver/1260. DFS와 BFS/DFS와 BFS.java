
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N,M,V;
	static boolean table[][];
	static boolean visited[];
	
	public static void DFS(int k) {
		System.out.print(k + " ");
		visited[k] = true;
		
		for(int i=0; i<= N; i++) {
			if(!visited[i] && table[k][i]) {
				DFS(i);
			}
		}
	}
	
	
	public static void BFS() {
		Queue<Integer> q = new LinkedList<>();
		q.add(V);
		visited[V] = true;
		
		while(!q.isEmpty()) {
			int now = q.poll();
			System.out.print(now + " ");
			for(int i=1; i<=N; i++) {
				if(!visited[i] && table[now][i]) {
					q.add(i);
					visited[i] = true;
				}
			}
		}
		
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		V = Integer.parseInt(stk.nextToken());
		
		table = new boolean[N+1][N+1];
		visited = new boolean[N+1];
		
		for(int i=0; i<M; i++) {
			stk = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(stk.nextToken());
			int b = Integer.parseInt(stk.nextToken());
			table[a][b] = true;
			table[b][a] = true;
			// 양방향
		}
		visited = new boolean[N+1];
		DFS(V);
		System.out.println();
		visited = new boolean[N+1];
		BFS();
	}
}
