import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static LinkedList<Integer>[] con;
	static Queue<Integer> que;
	static boolean[] visited;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		que = new LinkedList<>();
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		visited = new boolean[N];
		con = new LinkedList[N];
		for(int i=0;i<N;i++) {
			con[i] = new LinkedList<>();
		}
		

		int a,b;
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken())-1;
			b = Integer.parseInt(st.nextToken())-1;
			con[a].add(b); con[b].add(a);
		}
		
		int result=0;
		for(int i=0;i<N;i++) {
			if(!visited[i]) {
				bfs(i);
				result++;
			}
		}
		System.out.println(result);
		
		
	}
	
	private static void bfs(int node) {
		while(true) {
			int a;
			while(con[node].size()>0) {
				a = con[node].poll();
				if(visited[a]) continue;
				visited[a]=true;
				que.offer(a);
			}
			if(que.size()>0) {
				node = que.poll();
			} else break;
		}
	}
}
