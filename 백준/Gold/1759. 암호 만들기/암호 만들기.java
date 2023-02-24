import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	static char[] moum = {'a','e','i','o','u'};
	static int L, C;
	static ArrayList<Character> arrayList = new ArrayList<>();
	static ArrayList<Character> answer = new ArrayList<>();
	static boolean[] visited;
	static StringBuilder sb = new StringBuilder();
	
	public static void backtracking(int depth, int idx) {
		if(depth == L) {
			int count = 0;
			
			for(char i : answer) {
				for(int a=0; a<5; a++) {
					if(i == moum[a]) {
						count += 1;
					}
				}
			}
			
			// 최소 1개의 모음, 최소 두개의 자음	
			if(count >= 1 && (L-count) >= 2) {
				for(char i : answer) {
					sb.append(i);
				}
				sb.append("\n");
			}

			return;
		}
		
		
		for(int i=idx; i<C; i++) {
			if(!visited[i]) {
				visited[i] = true;
				answer.add(arrayList.get(i));
				backtracking(depth+1, i+1);
				answer.remove(answer.size()-1);
				visited[i] = false;
			}
		}
		
		
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		L = Integer.parseInt(stk.nextToken());
		C = Integer.parseInt(stk.nextToken());
		visited = new boolean[C+1];
		
		stk = new StringTokenizer(br.readLine());
		
		for(int i=0; i<C; i++) {
			arrayList.add(stk.nextToken().charAt(0));
		}
		
		Collections.sort(arrayList);
		
		backtracking(0,0);
		
		System.out.println(sb.toString());
	}
}