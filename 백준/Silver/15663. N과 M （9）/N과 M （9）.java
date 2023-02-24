
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int[] numbers;
	static boolean[] visited;
	static LinkedHashSet<ArrayList<Integer>> hashSet = new LinkedHashSet<>();
	static ArrayList<Integer> arrayList = new ArrayList<>();
	
	public static void bt(int depth, int start) {
		// 숫자가 똑같은게 오면 하나만 출력
		if(depth == M) {
//			hashSet.add(arrayList);
			hashSet.add(new ArrayList<Integer>(arrayList));
			return;
		}
		
		for(int i=start; i<N; i++) {
			if(!visited[i]) {
				visited[i] = true;
				arrayList.add(numbers[i]);
				bt(depth + 1, 0);
				visited[i] = false; 
				arrayList.remove(arrayList.size()-1);
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		StringBuilder stringBuilder = new StringBuilder();
		
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		
		stk = new StringTokenizer(br.readLine());
		numbers = new int[N];
		visited = new boolean[N];
		
		for(int i=0; i<N; i++) {
			numbers[i] = Integer.parseInt(stk.nextToken());
		}
		
		Arrays.sort(numbers);
		bt(0, 0);
		
		for(ArrayList<Integer> li : hashSet) {
			for(Integer a : li) {
				stringBuilder.append(a+" ");
			}
			stringBuilder.append("\n");
		}
		System.out.println(stringBuilder.toString());
	}
}
