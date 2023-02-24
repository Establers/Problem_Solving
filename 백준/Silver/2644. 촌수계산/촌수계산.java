import java.awt.Frame;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.concurrent.CountDownLatch;

public class Main {
	static int n;
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
	static int a,b;
	static Queue<Integer> q = new ArrayDeque<>();
	static boolean[] visited;
	static int count;
	static int answer;
	
	public static void bfs(int start) {
		q.add(start);
		visited[start] = true;
		
		while(!q.isEmpty()) {
			
			int q_size = q.size();
			
			// 하나의 사이클 마다 돌리기 위해 
			while(q_size-- > 0) {
				int now = q.poll();
				
				if(now == b) {
					answer = count;
					return;
				}
				
				for(int a : graph.get(now)) {
					if(!visited[a]) {
						visited[a] = true; 
						q.add(a);
					}			
				}
			}
		
//			System.out.print(count+" ");
			count += 1;
		}
		

		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(stk.nextToken());
		
		stk = new StringTokenizer(br.readLine());
		a = Integer.parseInt(stk.nextToken());
		b = Integer.parseInt(stk.nextToken());
		visited = new boolean[n+1];
		
		int e = Integer.parseInt(br.readLine());
		
		for(int i=0; i<=n+1; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		for(int i=0; i<e; i++) {
			stk = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(stk.nextToken());
			int y = Integer.parseInt(stk.nextToken());
			
			graph.get(x).add(y);
			graph.get(y).add(x);
		}
		
		bfs(a);
		
		if(answer == 0) {
			answer = -1;
		}

		System.out.println(answer);
		
		
		
	}
}