
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n,w,L;
	static int[] trucks;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(stk.nextToken()); // 트럭 수
		w = Integer.parseInt(stk.nextToken()); // 다리길이
		L = Integer.parseInt(stk.nextToken()); // 최대하중
		int weigth = 0;
		int count = 0;
		trucks = new int[n];
		
		stk = new StringTokenizer(br.readLine());
		
		for(int i=0; i<n; i++) {
			trucks[i] = Integer.parseInt(stk.nextToken());
		}
		
		Queue<Integer> q = new LinkedList<Integer>();
		
		// 1. 다리길이 만큼 0 추가
		for(int i=0; i<w-1; i++) {
			q.add(0);
		}
		
		// 2. 첫번째 트럭 올리기
		q.add(trucks[0]);
		count += 1;
		// 3. 무게변수에 트럭 무게 만큼 더하기
		weigth += trucks[0];

		int idx = 1;
		int pollValue = 0;
		boolean lastFlag = false;
		if(n==1) {
			System.out.println(n+w);
			return;
		}
		
		while(!q.isEmpty()) {
			// 4. Pop (pop 한개 1 이상이면 무게변수 빼기)
			//System.out.println(q.toString());
			pollValue = q.poll();
			count += 1;
			if(pollValue >= 1) {
				weigth -= pollValue;
				// if(idx < n-1) idx += 1;
			}
			
			// 5. 들어갈 트럭 무게 + 현재 무게 < 하중 --> 넣기
			
			if(weigth + trucks[idx] <= L) {
				if(!lastFlag) {
					if(idx != 0) {
						q.add(trucks[idx]);
						// System.out.println("add " + trucks[idx]);
						weigth += trucks[idx];
						if (idx == n-1) lastFlag = true;
					}
					if(idx < n-1) {
						idx += 1;
					}
				}
			} else {
				// 5.1 하중보다 넘으면 0 넣기
				if(!lastFlag) q.add(0);
			}
		}
		if(n == 1) count += -1;
		System.out.println(count);
	}
}
