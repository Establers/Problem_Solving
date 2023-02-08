
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int n;
	static int m;
	static int[] result; 
	static StringBuilder sb = new StringBuilder();
	public static void bt(int cnt, int start) { 
		if(cnt == m) {
			
			for (int a : result) {
				sb.append(a + " ");
			} 
			sb.deleteCharAt(sb.length()-1).append("\n");
			return;
		}
		
		for(int i=start; i<= n; i++) {
			result[cnt] = i;
			bt(cnt+1, i+1);
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		
		result = new int[m];
		bt(0,1);
		System.out.print(sb.toString());
	}
}
