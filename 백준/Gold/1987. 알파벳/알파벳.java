
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Point{
	public int x;
	public int y;
	public String nli;
	public Point(int x, int y,  String nli) {
		this.x = x;
		this.y = y;
		this.nli = nli;
	}
}

public class Main {
	static int R;
	static int C;
	static int[][] board;
	static boolean[] visited;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static int count = 1;
	
	
	public static void dfs(int a, int b, int depth) {
		count = Math.max(count, depth);
		
		for(int i=0; i<4; i++) {
			int nx = a+dx[i];
			int ny = b+dy[i];
				if(!inTheBoundary(nx, ny)) {
					continue;
				} else {
					if(!visited[(board[nx][ny])]) {
						visited[(board[nx][ny])] = true;
						dfs(nx, ny, depth+1);
						visited[(board[nx][ny])] = false;
					}
					
				}
		}
	}


	public static boolean inTheBoundary(int nx, int ny) {
		if(nx < 0 || nx >= R || ny < 0 || ny >= C) {
			return false;
		}
		return true;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		board = new int[R][C];
		visited = new boolean[26];
		//System.out.println(Integer.parseInt('Z'));
		
		for(int i=0; i<R; i++) {
			String temp = br.readLine();
			for(int j=0; j<C; j++) {
				board[i][j] = temp.charAt(j) - 'A'; // A : 0 .. 
			}
		}
		visited[(board[0][0])] = true;
		dfs(0,0,1);

		
		System.out.println(count);
	}
}

