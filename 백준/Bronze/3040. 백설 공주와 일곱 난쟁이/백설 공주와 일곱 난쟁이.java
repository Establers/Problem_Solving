
import java.awt.print.Printable;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	static boolean[] visited = new boolean[9];
	static StringBuilder sb = new StringBuilder();
	static int sum;
	static int[] numbers;
	static int[] select = new int[9];
	static ArrayList<Integer> arrayList = new ArrayList<>();
	
	public static void dfs(int depth, int value, int idx) {
		if(depth == 7) {
			if(value == 100) {
				// System.out.println("정답출력");
				for(int i : arrayList) {
					System.out.println(i);
				}
			}
			return;
		}
		
		for(int i=idx; i<9; i++) {
			if(!visited[i]) {
				visited[i] = true;
				value += numbers[i];
				arrayList.add(numbers[i]);
				
				dfs(depth+1, value, i);
				visited[i] = false;
				value -= numbers[i];
				arrayList.remove(arrayList.size()-1);
			}
		}
	}
	
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		numbers = new int[9]; 
		
		for(int i=0; i<9; i++) {
			numbers[i] = scanner.nextInt();
		}
		
		dfs(0, 0, 0);
	}
	
	
}
