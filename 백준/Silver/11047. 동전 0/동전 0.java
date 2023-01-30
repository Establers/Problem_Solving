import java.awt.print.Printable;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.concurrent.ConcurrentHashMap;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken()); // money
		int count = 0;
		ArrayList<Integer> coin = new ArrayList<>();
		
		for(int i=0; i<n; i++) {
			int temp = Integer.parseInt(br.readLine());
			if (temp <= k) {
				coin.add(temp);
			}
		}
		// 반대로
		for(int i=coin.size()-1; i>=0; i--) {
			int last = (int)(k / (coin.get(i)));
			if(last > 0) {
				k = k - (last*coin.get(i));
				count += last;
			}
			if(n == 0) break;
		}
		
		System.out.println(count);
	}
}

