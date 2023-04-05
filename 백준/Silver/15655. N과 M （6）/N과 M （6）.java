
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	static int[] arr;
	static int n;
	static int m;
	static ArrayList<Integer> li = new ArrayList<>();
	static StringBuilder sb = new StringBuilder();
	
	public static void bt(int depth, ArrayList<Integer> arrayList) {
		if(depth == m) {
			//System.out.println(arrayList.toString());
			for(int i : arrayList) {
				sb.append(i + " ");
			}
			sb.append("\n");
			return;
		}
		
		//
		for(int i=0; i<n; i++) {

			if (!arrayList.isEmpty() && (arrayList.get(arrayList.size()-1) < arr[i])) {
				arrayList.add(arr[i]);
				bt(depth+1, arrayList);
				arrayList.remove(arrayList.size()-1);
			}
			
			if (arrayList.isEmpty()) {
				arrayList.add(arr[i]);
				bt(depth+1, arrayList);
				arrayList.remove(arrayList.size()-1);
			}

		}
	}
	
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		n = scanner.nextInt();
		m = scanner.nextInt();
		arr = new int[n];
		
		for(int i=0; i<n; i++) {
			arr[i] = scanner.nextInt(); 
		}
		
		Arrays.sort(arr);
		
		bt(0, li);
		System.out.println(sb.toString());
	}
	
	
}
