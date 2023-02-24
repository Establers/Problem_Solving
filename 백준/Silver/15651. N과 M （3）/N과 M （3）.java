import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	//////////////////////////////
	/*
	 * 
	 * 중복을 허용하는 수열
	 * 1~N까지 자연수 중에서 M개를 고른 수열
	 * 같은 수를 여러번 골라도 됨
	 * 
	 */
	//////////////////////////////
	
		
	static int N,M;
	static StringBuilder sb = new StringBuilder();
	static int[] nums;
	
	public static void bt(int depth, int[] num) {
		if(depth == M) {
			for(int i=0; i<M; i++) {
				sb.append(num[i]+" ");
			}
			sb.append("\n");
			return;
		}
		
		for(int i=1; i<=N; i++) {
			nums[depth] = i;
			bt(depth + 1, nums);

		}
		
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		N = scanner.nextInt();
		M = scanner.nextInt();
		nums = new int[M];
		
		bt(0, nums);
		
		System.out.println(sb.toString());
		
	}
}