import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());
		
		int[] zero = new int[41];
		int[] one = new int[41];
		
		zero[0] = 1;
		zero[1] = 0;
		
		one[0] = 0;
		one[1] = 1;
		
		for (int i=0; i<t; i++) {
			int n = Integer.parseInt(br.readLine());
			
			if(n < 2) {
				if (n == 0) {
					System.out.printf("%d %d\n",zero[0], one[0]);
				} else if(n == 1) {
					System.out.printf("%d %d\n",zero[1], one[1]);
				}
			} else {
				for (int j=2; j<=n; j++) {
					zero[j] = zero[j-1] + zero[j-2];
					one[j] = one[j-1] + one[j-2];
				}
				System.out.printf("%d %d\n", zero[n], one[n]);
			}
		}
	}
}
