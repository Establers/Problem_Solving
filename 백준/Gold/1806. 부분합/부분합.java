

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int n = Integer.parseInt(st.nextToken());
		int s = Integer.parseInt(st.nextToken());
		
		ArrayList<Integer> li = new ArrayList<>();
		int temp = 0;
		li.add(0);
		
		st = new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<n; i++) {
			temp += Integer.parseInt(st.nextToken());
			li.add(temp);
		}
		// System.out.println(li);
		int val = 0;
		int INF = 9999999;
		int result = INF;
		int start = 0;
		int end = 0;
		while (true) {
			val = li.get(end) - li.get(start);
			
			if(val >= s) { 
				// 조건 만족
				result = Math.min(result, end-start);
				// 크기 줄이기
				if(start < li.size()-1 ) {
					start += 1;
				}
			} else {
				// 조건 X
				if(end == li.size()-1) {
					break;
				}
				if(end < li.size()-1) {
					end += 1;
				}
				
			}
		}
		if (result != INF) {
			System.out.println(result);
		} else {
			System.out.println("0");
		}
		
	}
}
