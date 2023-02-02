import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = null;
		
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer> li = new ArrayList<>();
		
		for(int i=0; i<n; i++) {
			li.add(Integer.parseInt(br.readLine()));
		}
		
		Collections.sort(li);
		StringBuilder sb = new StringBuilder();
		
		for(int i=0; i<n; i++) {
			sb.append(li.get(i)).append("\n");
		}
		
		System.out.println(sb.toString());
		
	}
}