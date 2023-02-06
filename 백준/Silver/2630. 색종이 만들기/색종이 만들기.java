
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] arr;
	
	static int w_cnt = 0; // 0
	static int b_cnt = 0; // 1
	
	public static void findPaper(int n, int x, int y) {
		char value = checkAll(n,x,y);
		if(value != 'n') {
			if(value == 'b') {
				b_cnt += 1;
				return;
			} else 
			{
				w_cnt += 1;
				return;
			}
		}
		
		// check 완료
		int nextNum = n/2;
		findPaper(nextNum,	x,			y);
		findPaper(nextNum,	x+nextNum,	y);
		findPaper(nextNum,	x,			y+nextNum);
		findPaper(nextNum,	x+nextNum,	y+nextNum);
	}
	
	
	/*
	 * 모두가 1인지 0인지 return 
	 * */
	public static char checkAll(int n, int x, int y) {
		int temp = arr[x][y]; // 좌상단 값 (0 또는 1)
		
		for(int i=x; i<x+n; i++) {
			for(int j=y; j<y+n; j++) {
				if(temp != arr[i][j]) {
					return 'n'; // 다른게 있다
				}
			}
		}

		// 모두가 같다.
		if(temp == 1) return 'b';
		else return 'w'; 
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		StringTokenizer stk = null;
		
		for(int i=0; i<n; i++) {
			stk = new StringTokenizer(br.readLine()," ");
			for(int j=0; j<n; j++) {
				arr[i][j] = Integer.parseInt(stk.nextToken());
			}
		}
		
		findPaper(n, 0, 0);
		
		System.out.println(w_cnt);
		System.out.println(b_cnt);
	}
}
