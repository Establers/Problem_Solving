
import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer> nums = new ArrayList<>();
		
		StringTokenizer stk = null;
		stk = new StringTokenizer(br.readLine(), " ");
		for(int a=0; a<n; a++) {
			nums.add(Integer.parseInt(stk.nextToken()));
		}
		
		int[] arr = new int[1001]; // 0 - 소수
		
		for(int i=2; i<Math.sqrt(1000)+1; i++) {
			if (arr[i] == 0) {
				for(int j=i+i; j<1001; j+=i) {
					// System.out.println(j);
					if (arr[j] == 0) {
						arr[j] = 1;
					}
				}
			}
		}
		arr[0] = 1;
		arr[1] = 1;
		
		int count = 0;
		for (Integer a : nums) {
			//System.out.println(a);
			if(arr[a] == 0) {
				count++;
			}
		}
		System.out.println(count);
		
	}
}
