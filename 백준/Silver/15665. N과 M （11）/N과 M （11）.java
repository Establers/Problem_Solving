
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.StringTokenizer;

public class Main {
	static int N,M;
	static int[] numbers;
	static StringBuilder sb = new StringBuilder();
	static LinkedHashSet<ArrayList<Integer>> hashSet = new LinkedHashSet<>();
	static ArrayList<Integer> arrayList = new ArrayList<>();
	
	public static void bt(int depth) {
		if(depth == M) {
			hashSet.add(new ArrayList<Integer>(arrayList));
			return;
		}
				
		for(int i=0; i<N; i++) {
			arrayList.add(numbers[i]);
			bt(depth + 1);
			arrayList.remove(arrayList.size()-1);
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		
		numbers = new int[N];
		
		stk = new StringTokenizer(br.readLine());
		
		for(int i=0; i<N; i++) {
			numbers[i] = Integer.parseInt(stk.nextToken());
		}
		
		Arrays.sort(numbers);
		bt(0);
		
		for(ArrayList<Integer> li : hashSet) {
			for(Integer a : li) {
				sb.append(a+" ");
			}
			sb.append("\n");
		}
		
		System.out.println(sb.toString());
		
		
		
		
	}
}
