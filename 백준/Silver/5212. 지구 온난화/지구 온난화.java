import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static char[][] board;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,-1,1};
	
	static ArrayList<int[]> arrayList = new ArrayList<>();
	
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		int x = Integer.parseInt(stk.nextToken());
		int y = Integer.parseInt(stk.nextToken());
		
		board = new char[x][y];
		
		for(int i=0; i<x; i++) {
			String temp = br.readLine();
			for(int j=0; j<y; j++) {
				board[i][j] = temp.charAt(j); 
			}
		}
		
		for(int i=0; i<x; i++) {
			for(int j=0; j<y; j++) {
				if(board[i][j] == 'X') {
					int count = 0;
					for(int a=0; a<4; a++) {
						int nx = i + dx[a];
						int ny = j + dy[a];
//						System.out.println(nx + ny);
						if(0 <= nx && nx < x && 0 <= ny && ny < y) {
							if(board[nx][ny] == 'X') {
								count += 1;
							}
						}
					}
//					System.out.println(count);
					if(count <= 1) {
						arrayList.add(new int[] {i, j});
					}
				}			
			}
		}
		
		for(int[] now : arrayList) {
//			System.out.println("??");
			board[now[0]][now[1]] = '.';
		}
		
		
		int max_x = 0;
		int max_y = 0;
		int min_x = 110;
		int min_y = 110;
		
		for(int i=0; i<x; i++) {
			for(int j=0; j<y; j++) {
				if(board[i][j] == 'X') {
					max_x = Math.max(max_x, i);
					max_y = Math.max(max_y, j);
					min_x = Math.min(min_x, i);
					min_y = Math.min(min_y, j);
				}			
			}
		}
		
		for(int i=min_x; i<=max_x; i++) {
			for(int j=min_y; j<=max_y; j++) {
				System.out.print(board[i][j]);
			}
			System.out.println();
		}
		
	}
}