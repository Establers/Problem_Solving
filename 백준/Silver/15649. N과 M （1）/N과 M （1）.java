
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static StringBuilder sbr = new StringBuilder();
	static ArrayList<Integer> arrayList = new ArrayList<>();
	static int n;
	static int m;
	static boolean[] visited;
	public static void bt(int depth) {
		if(depth == m) {
			// System.out.println(arrayList.toString());
			for(int i : arrayList) {
				//System.out.print(i+" ");
				sbr.append(i+" ");
			} 
			sbr.append("\n");		
			return;
		}
		
		for(int i=1; i<=n; i++) {
			if(visited[i] == false) {
				visited[i] = true; 
				arrayList.add(i);
				bt(depth+1);
				visited[i] = false;
				arrayList.remove(arrayList.size()-1);
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		n = scanner.nextInt();
		m = scanner.nextInt();
		visited = new boolean[n+1];
		
		bt(0);
		System.out.println(sbr.toString());
		
	}
}
