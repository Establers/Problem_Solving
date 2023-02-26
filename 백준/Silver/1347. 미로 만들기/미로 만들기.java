import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
	static int[] dx = {-1, 0, 1, 0}; // 상, 우, 하, 좌
	static int[] dy = {0, 1, 0, -1}; // 상, 우, 하, 좌
	
	static char[][] board = new char[100][100];
	
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		String seq = br.readLine();
		int dir = 2;
		
		int my_x = 50;
		int my_y = 50;
		
		
		int max_x = 0;
		int max_y = 0;
		int min_x = 110;
		int min_y = 110;
//		Arrays.fill(board, '#');
		for(int i = 0; i<100; i++) {
			Arrays.fill(board[i], '#');
		}
		board[my_x][my_y] = '.';
		max_x = Math.max(max_x, my_x);
		max_y = Math.max(max_y, my_y);
		min_x = Math.min(min_x, my_x);
		min_y = Math.min(min_y, my_y);
		for(int i=0; i<n; i++) {
			char temp = seq.charAt(i);
			if(temp == 'R') {
				dir += 1;
				if(dir == 4) {
					dir = 0;
				}
			} else if(temp == 'L') {
				dir += -1;
				if(dir == -1) {
					dir = 3;
				}
			} else if(temp == 'F') {
				// 앞으으로 간다잉~~~~~~~
				my_x += dx[dir];
				my_y += dy[dir];
				
			}
			board[my_x][my_y] = '.';
			max_x = Math.max(max_x, my_x);
			max_y = Math.max(max_y, my_y);
			min_x = Math.min(min_x, my_x);
			min_y = Math.min(min_y, my_y);
		}
		
		for(int i=min_x; i<=max_x; i++) {
			for(int j=min_y; j<=max_y; j++) {
				System.out.print(board[i][j]);
			}
			System.out.println();
		}

	}
}