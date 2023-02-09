

import java.io.BufferedReader;
import java.util.Scanner;

// N 자리 소수 일 경우
// 

public class Main {
	static int N;
	static StringBuilder sb = new StringBuilder();
	static int[] numArr = {1,3,7,9};
	
	public static void find_prime(int depth, int num) {
		if(promising(num)) {
			if (depth == N) {
				sb.append(num+"\n");
				return;
			}
			for(int n : numArr) {				
				num = (int)(10*num + n);
				// System.out.println(num);
				find_prime(depth+1, num);
				num = num / 10;
			}
		}

		
	}
	
	public static boolean promising(int num) {
		for(int i=2; i<=(int)(Math.sqrt(num)); i++) {
			if (num % i == 0) {
				//System.out.println("소수ㄴ" + i);
				return false; // 소수아님
			}
		}
		return true;
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		N = scanner.nextInt();
		
		find_prime(1, 2);
		find_prime(1, 3);
		find_prime(1, 5);
		find_prime(1, 7);
		
		System.out.println(sb.toString());
	}
}
