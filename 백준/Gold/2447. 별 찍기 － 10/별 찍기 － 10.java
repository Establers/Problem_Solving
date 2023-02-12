
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	static StringBuilder sb = new StringBuilder();
	
	public static void fractal(int n, int x, int y, char[][] arr) {
		if(n == 1) {
			return;
		}
		
		
		// 중간점 공백으로 해버리깅..
		for(int i= x+n/3; i<x+(n-n/3); i++) { // 가로
			for(int j=y+n/3; j<y+(n-n/3); j++) { // 세로
				arr[i][j] = ' '; 
			}
		}
		// 길이에 따른 공백의 개수가 다르므로, 길이에 맞게 for문 수행회수를 정하였고
		// 크기에 따른 가변 인덱스를 for문에 주어서 해당 위치에 맞게(9x9칸을 나누었을 때 가로세로 036 036 각각의 인덱스가 나옴)
		// 공백으로 바꾸게 했음.
		
		for(int i=x; i<=x+(n-(n/3)); i += n/3) { 
			for(int j=y; j<=y+(n-(n/3)); j += n/3) {
				fractal(n/3, i, j, arr);
			}
		}
		// x와 y의 크기에 따른 가변 인덱스를 주어 그 위치에서의 
        // 일반적인 상황에서 9개의 재귀함수를 호출하도록 하였음
		
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		char[][] arr = new char[n][n];
		int x =0;
		int y =0;
		for(char a[] : arr) {
			Arrays.fill(a, '*');
		}
		fractal(n, x, y, arr);
		

		
		for (int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				sb.append(arr[i][j]);
			}
			sb.append("\n");
		}
		
		System.out.println(sb.toString());
	}
}
