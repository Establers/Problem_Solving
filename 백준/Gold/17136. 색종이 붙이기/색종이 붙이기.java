
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	// 개인적으로 스도쿠와 비슷하다고 생각함.
	static int[][] board;
	static int[] paper_remain = {0, 5,5,5,5,5};
	static int N = 10;
	static int answer = Integer.MAX_VALUE;

	public static void board_fill_xy_1(int x, int y, int type) {
		for (int i = x; i < x + type; i++) {
			for (int j = y; j < y + type; j++) {
				board[i][j] = 1; 
			}
		}
	}
	
	public static void board_fill_xy_0(int x, int y, int type) {
		for (int i = x; i < x + type; i++) {
			for (int j = y; j < y + type; j++) {
				board[i][j] = 0; 
			}
		}
	}
	
	public static boolean check_xy_boundary_value(int x, int y, int type) {
		for (int i = x; i < x + type; i++) {
			for (int j = y; j < y + type; j++) {
				if(i >= N || j >= N) {
					return false;
				}
				if(board[i][j] == 0) {
					return false;
				}
			}
		}
		return true; // in the boundary and not '1'
	}
	
	/*
	 * y 0~9 -> x 0~9 탐색
	 * 모든 부분에 대해 그냥 무지성 백트래킹
	 * 좌표에 Backtracking 하는 부분은 스도쿠 문제와 거의 유사
	 * 
	 */
	public static void bt(int x, int y, int result) {
		if(x == 10) { // end 조건
			answer = Math.min(answer, result);
//			System.out.println(Arrays.toString(paper_remain));

			return;
		}		
		// System.out.println("x , y: "+ x + " " + y);
		if(result > answer) {
			return;
		}
				
		// 옆으로 (y++) 하면서... y = 9 되면 x+1, y=0으로..
		if(y == 10) {
			bt(x+1, 0, result);
			return;
		} 
		
		if(board[x][y] == 1) {
			// 5 4 3 2 1 
			for(int t=5; t>0; t--) {
				// 색종이가 남아 있어야함
				if(paper_remain[t] <= 0) continue;
				// 색종이의 범위 안에 있어야함, 0이 있으면 안됨
				if(!check_xy_boundary_value(x, y, t)) continue;
				
				// 모든 정상 경우에서 Backtracking 진행
				board_fill_xy_0(x, y, t); 
				paper_remain[t] += -1;
				bt(x, y+1, result+1);
				paper_remain[t] += +1;	 // 사용한 색종이 복구
				board_fill_xy_1(x, y, t);
			}
		} else {
			// board[x][y] == 0 일경우
			bt(x, y+1, result);
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = null;
		board = new int[N][N];

		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(stk.nextToken());
			}
		}
		// Input end
		bt(0, 0, 0);
		
		if(answer == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(answer);
		}
		
		

	}
}
