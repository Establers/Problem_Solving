import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	//////////////////////////////
	/*
	 * N과 M 3과 유사함
	 * 중복을 허용하는 수열
	 * 주어진 자연수 중에서 M개를 고른 수열
	 * 같은 수를 여러번 골라도 됨
	 * 
	 */
	//////////////////////////////
	
	static int N,M;
	static StringBuilder sb = new StringBuilder();
	static int[] nums;
	static ArrayList<Integer> arrayList = new ArrayList<>();
	static int[] givenNumbers;
	
	public static void bt(int depth, int[] num) {
		if(depth == M) {
			for(int i=0; i<M; i++) {
				sb.append(num[i]+" ");
			}
			sb.append("\n");
			return;
		}
		
		for(int i : givenNumbers) { 
			nums[depth] = i;
			bt(depth + 1, nums);
		}
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		nums = new int[M];
		givenNumbers = new int[N];
		
		stk = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			givenNumbers[i] = Integer.parseInt(stk.nextToken());
		}
		
		Arrays.sort(givenNumbers);
		// 오름 차순을 위한 정렬
		bt(0, nums);
		
//		bt_with_ArrayList(0);

		System.out.println(sb.toString());
		
	}
}