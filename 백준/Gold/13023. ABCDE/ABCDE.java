import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
	static boolean[] visited;
	static int answer;
	
	public static void dfs(int start, int length) {
//		System.out.println(length);
		if(length == 5) {
			answer = 1;
			return;
		}
		
		for(int idx : graph.get(start)) {
			if(!visited[idx] && (answer == 0)) {
				visited[idx] = true;
				dfs(idx, length + 1);
				visited[idx] = false;
			}
		}
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		
		for(int i=0; i<N+1; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		for(int i=0; i<M; i++) {
			stk = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(stk.nextToken());
			int b = Integer.parseInt(stk.nextToken());
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		
		for(int i=0; i<N; i++) {
			visited = new boolean[N+1];
//			System.out.println("START " + i);
			visited[i] = true;
			dfs(i, 1);
		}

		System.out.println(answer);
	}
}