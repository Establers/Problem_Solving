import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int nums = 1;
		int cnt = 1;
		
		while(n > nums) {
			nums += 6 * cnt;
			cnt += 1;
		}
		System.out.println(cnt);
		
		
	}
}
