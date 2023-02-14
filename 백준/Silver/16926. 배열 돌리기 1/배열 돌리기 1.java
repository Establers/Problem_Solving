
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] graph;
	public static void swap(int a,int b, int c, int d) {
		int temp = 0;
		temp = graph[a][b];
		graph[a][b] = graph[c][d];
		graph[c][d] = temp; 
	}
		
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(stk.nextToken());
		int m = Integer.parseInt(stk.nextToken());
		int r = Integer.parseInt(stk.nextToken());
		
		graph = new int[n][m];
		
		for(int i=0; i<n; i++) {
			stk = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				graph[i][j] = Integer.parseInt(stk.nextToken());
			}
		}
		
		
		
		for(int re = 0; re < r; re++) {
			int repeat = Math.min(n, m) / 2;
			
			for(int i=0; i<repeat; i++) {
			
				for(int a=i; a<=m-2-i; a++) {
					swap(i, a, i, a+1);
				}
				
//				for(int x=0; x<n; x++) {
//					for(int j=0; j<m; j++) {
//						System.out.print(graph[x][j] + " ");
//					}
//					System.out.println();
//				}
//				System.out.println();
				
				for(int a=i; a<=n-2-i; a++) {
					swap(a, m-i-1, a+1, m-i-1);
				}
				
//				for(int x=0; x<n; x++) {
//					for(int j=0; j<m; j++) {
//						System.out.print(graph[x][j] + " ");
//					}
//					System.out.println();
//				}
//				System.out.println();
				
				///
				for(int a=m-i-1; a>=i+1; a--) {
					swap(n-1-i, a, n-1-i, a-1);
				}
				
//				for(int x=0; x<n; x++) {
//					for(int j=0; j<m; j++) {
//						System.out.print(graph[x][j] + " ");
//					}
//					System.out.println();
//				}
//				System.out.println();
				
				for(int a=n-i-1; a>i+1; a--) {
					swap(a, i, a-1, i);
				}
				
//				for(int x=0; x<n; x++) {
//					for(int j=0; j<m; j++) {
//						System.out.print(graph[x][j] + " ");
//					}
//					System.out.println();
//				}
//				System.out.println();
			}
			
		}
		
		
	
		
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				System.out.print(graph[i][j] + " ");
			}
			System.out.println();
		}
		
		
		
	}
}
