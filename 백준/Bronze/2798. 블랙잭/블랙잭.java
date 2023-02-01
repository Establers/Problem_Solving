import java.awt.print.Printable;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = null;
		
		stk = new StringTokenizer(br.readLine()," ");
		int n = Integer.parseInt(stk.nextToken());
		int m = Integer.parseInt(stk.nextToken());
		
		stk = new StringTokenizer(br.readLine()," ");
		
		ArrayList<Integer> li = new ArrayList<>();
		for (int i=0; i<n; i++) {
			li.add(Integer.parseInt(stk.nextToken()));
		}
		int result = 0;
		
		for(int a=0; a<n; a++) {
			for(int b=a+1; b<n; b++) {
				for(int c=b+1; c<n; c++) {
					int temp = li.get(a)+ li.get(b)+li.get(c);
					if(temp <= m && temp > result) {
						result = temp;
					}
				}
			}
		}
		
		System.out.println(result);	
	}
}