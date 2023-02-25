
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
	static int[] people_in_node;
	static boolean[] visited;
	static int N;
	static int answer = Integer.MAX_VALUE;
	static Queue<Integer> q = null;
	static ArrayList<Integer> select_list = new ArrayList<>();
	
	public static void bfs(int x) {
		q = new ArrayDeque<>();
		q.add(x);
		visited[x] = true;
		
		while(!q.isEmpty()) {
			int now = q.poll();
			
			for(int togo : graph.get(now)) {
				if(!visited[togo]) {
					visited[togo] = true;
					q.add(togo);
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		/*
		6
		5 2 3 4 1 2
		2 2 4
		4 1 3 6 5
		2 4 2
		2 1 3
		1 2
		1 2
		*/
		
		N = Integer.parseInt(stk.nextToken());
		people_in_node = new int[N+1];
		visited = new boolean[N+1];
		
		for(int i=0; i<N+1; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		int sum_people = 0;
		stk = new StringTokenizer(br.readLine());
		for(int i=1; i<N+1; i++) {
			// 각 노드별 인구수
			people_in_node[i] = Integer.parseInt(stk.nextToken());
		}
		
		for(int i=1; i<N+1; i++) {
			sum_people += people_in_node[i];
		}
		
		for(int i=1; i<N+1; i++) {
			stk = new StringTokenizer(br.readLine());
			int temp = Integer.parseInt(stk.nextToken()); // 인접한 구역의 수?
			for(int a=0; a<temp; a++) {
				// 무방향(양방향)
				int to = Integer.parseInt(stk.nextToken());
				graph.get(i).add(to);
				graph.get(to).add(i);
			}
		}
		
		// input end
		
		// 모든 부분집합에 대해, 무분 집합에 포함되는 노드, 포함되지 않는 도드
		// 그 중에 하나의 집합에 대해 visited 처리를 하고 (둘다 해야함 서로 반전해서)
		// 모든 노드에 대해 DFS / BFS 를 진행하고, count++;를 하는데
		// count == 2 일 때, 그 집합에 대한 것을 게산한다.
		
		// 0 1 2 3 4 5
		for(int i=1; i < (1<<N)-1; i++) {
			for(int a=0; a<N; a++) {
				if((i & (1<<a)) != 0) {
//					System.out.print((a+1) + " ");
					select_list.add(a+1);
				}
			}
			// 부분집합 완성
			// 지금은 그냥 모두다 연결되어 있는 형태
			visited = new boolean[N+1];
			
			for(int s_num : select_list) {
				visited[s_num] = true;
			}
			
			int count = 0;
			for(int k=1; k<N+1; k++) {
				if(!visited[k]) {
					bfs(k);
					count += 1;
				}
			}
			
			for(int s_num : select_list) {
				visited[s_num] = false;
			}
			
			for(int k=1; k<N+1; k++) {
				if(!visited[k]) {
					bfs(k);
					count += 1;
				}
			}
			
//			System.out.println("count : " + count);
			if(count == 2) {
				// 두개의 연결 구역이 있음 -> 정상케이스
				int temp = 0;
				for(int s_num : select_list) {
					temp += people_in_node[s_num];
				}
				// a + b = s
				// b = s - a
				// a - b = a - (s - a)
				// 		 = 2a - s
				// abs(2a - s)
				answer = Math.min(answer, Math.abs(temp*2 - sum_people)); 
			}			
			
			for(int s_num : select_list) {
				visited[s_num] = false;
			}
			select_list.clear();
			

		}
		
		if(answer != Integer.MAX_VALUE) {
			System.out.println(answer);
		} else {
			System.out.println(-1);
		}
			
	}
}
