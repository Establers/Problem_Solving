
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.concurrent.ArrayBlockingQueue;

public class Main {
	static int N;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		Queue<Integer> que = new ArrayBlockingQueue<>(N);
		for(int i=1; i<=N ; i++) {
			que.offer(i);
		}
		
		while(true) {
			if(que.size()==1) break;
			que.poll();
			if(que.size()==1) break;
			que.offer(que.poll());
		}
		System.out.println(que.poll());
	}
}
