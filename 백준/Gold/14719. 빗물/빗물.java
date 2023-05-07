import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import javax.xml.ws.AsyncHandler;

public class Main {
	static int h, w;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		h = Integer.parseInt(stk.nextToken());
		w = Integer.parseInt(stk.nextToken());
		
		int answer = 0;
		
		stk = new StringTokenizer(br.readLine());
		
		int[] nums = new int[w];
		for(int i=0; i<w; i++) {
			int temp = Integer.parseInt(stk.nextToken());
			nums[i] = temp;
		}
		
		// input end
		
		for(int i=1; i<w-1; i++) {
			int now_h = nums[i];
			int left = now_h;
			int right = now_h;
			
			for (int l = i-1; l>=0; l--) {
				if(nums[l] > now_h) left = Math.max(left, nums[l]);
			}
			
			for (int r = i+1; r<w; r++) {
				if(nums[r] > now_h) right = Math.max(right, nums[r]);
			}
			
			// end 
			
			if(now_h < right && now_h < left) {
				answer += (Math.min(left, right) - nums[i]);
			}
		}
		
		System.out.println(answer);
		
		
	}
}