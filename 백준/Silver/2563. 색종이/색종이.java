
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = null;
		
		int n = Integer.parseInt(br.readLine());
		int a,b = 0;
		int count = 0;
		
		boolean[][] board = new boolean[100][100];
		
		for(int i=0; i<n; i++) {
			stk = new StringTokenizer(br.readLine());
			a = Integer.parseInt(stk.nextToken());
			b = Integer.parseInt(stk.nextToken());
			
			for(int x=a-1; x<a+9; x++) {
				for(int y=b-1; y<b+9; y++) {
					if (x >= 100 || y >= 100) continue;
					board[x][y] = true; 
				}
			}
		
		}
		
		for(int i=0; i<100; i++) {
			for(int j=0; j<100; j++) {
				if(board[i][j] == true) count++;
			}
		}
		
		System.out.println(count);
	}
}
