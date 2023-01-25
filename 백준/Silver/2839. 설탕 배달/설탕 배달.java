import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		int d[] = new int[5001];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		
		for(int i=0; i<=n; i++) {
			d[i] = 5001;
		}
		
		d[0] = 0;
		// 3
		for(int i=3; i<n+1; i++) {
			if(d[i-3] != 5001) {
				d[i] = Math.min(d[i], d[i-3]+1); // 배수 값 설정
			}
		}
		
		// 5
		for(int i=5; i<n+1; i++) {
			if(d[i-5] != 5001) {
				d[i] = Math.min(d[i], d[i-5]+1); // 배수 값 설정
			}
		}
		// 5와 3 공배수도 min에 의해 최소값 결정됨
		
		// 답 출력
		if(d[n] != 5001) {
			System.out.println(d[n]);
		} else {
			System.out.println(-1);
		}
		
		
	}
}