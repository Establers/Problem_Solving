import java.io.*;
import java.util.*;

public class Main {
	
	static int n;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static int[][] board;
	static Queue<int[]> q = new ArrayDeque<>();
	static ArrayList<Integer> answers = new ArrayList<>();
	static int danzi = 0;
	static int counts = 0;
	
	static boolean[][] visited;
	
	public static void dfs(int x, int y, int count) {
		
		for(int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if(0 <= nx && nx < n && 0 <= ny && ny < n) {
				// 경계안
				if(!visited[nx][ny] && board[nx][ny] != 0) {
					counts++;
					visited[nx][ny] = true;
					dfs(nx, ny, count+1);
				} 
			} 
		}
	}
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		board = new int[n][n];
		visited = new boolean[n][n];
		
		for(int i=0; i<n; i++) {
			String temp = br.readLine();
			for(int j=0; j<n; j++) {
				board[i][j] = temp.charAt(j) - '0';
			}
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(!visited[i][j] && board[i][j] != 0) {
					counts = 1;
					visited[i][j] = true; 
					dfs(i, j, 0);
					answers.add(counts);
				}
			}
		}
		
		
		Collections.sort(answers);
		System.out.println(answers.size());
		for(int h : answers) {
			System.out.println(h);
		}

	}
}