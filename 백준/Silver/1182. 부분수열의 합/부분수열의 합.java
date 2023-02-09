
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
// 백트래킹은 자연수 일 때만 가능
// 뒤에 들어있는 수들이 음수가 되면 불가능
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	static int N, S, totalCnt;
	static int[] input; // 입력받은 수
	static boolean[] isSelected; // 각 원소가 부분집합 구성에 포함되어있는지 여부
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken()); // 합

		input = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			input[i] = Integer.parseInt(st.nextToken()); 
		}
		
		isSelected = new boolean[N];
		
		generateSubSet(0, 0);
		if (S == 0) totalCnt += -1;
		System.out.println(totalCnt);
		
	}
	

	
	private static void generateSubSet(int cnt, int sum) { // 직전까지 고려된 원소 수  
		if(cnt == N) {
			if(sum == S) {
				totalCnt ++;
				
			}
			return;
		}
		
		// 현재 원소를 부분집합의 구성에 포함
		isSelected[cnt] = true;
		generateSubSet(cnt+1, sum+input[cnt]);
		// 현재 원소를 부분집합의 구성에 비포함
		isSelected[cnt] = false;
		generateSubSet(cnt+1, sum);
		
	}
}

