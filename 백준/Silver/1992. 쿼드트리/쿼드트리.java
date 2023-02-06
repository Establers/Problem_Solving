

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static int[][] arr;
	public static StringBuilder sb = new StringBuilder();
	public static void check(int n, int x, int y) {	
		if(posi(n,x,y)) {
			sb.append(arr[x][y]);
			return;
		}
		
	
		int idx = n / 2;
		sb.append('(');
		check(idx, x,		y);
		check(idx, x,		y+idx);
		check(idx, x+idx,	y);
		check(idx, x+idx,	y+idx);
		sb.append(')');
		
	}
	
	public static boolean posi(int n, int x, int y) {
		int temp = arr[x][y];
		for(int i=x; i<n+x; i++) {
			for(int j=y; j<n+y; j++) {
				if(temp != arr[i][j]) {
					return false;
				}
			}
		}
		// all
		return true;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		arr = new int[n][n];
		
		for(int i=0; i<n; i++) {
			String temp = br.readLine();
			for(int j=0; j<n; j++) {
				arr[i][j] = temp.charAt(j)-'0';
			}
		}
		check(n,0,0);
		System.out.println(sb.toString());
	}
}
