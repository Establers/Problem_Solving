import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		
		Queue<Integer> q = new ArrayDeque<>();
		for(int i=1; i<=n; i++) {
			q.add(i);
		}
		
		while(q.size() != 1) {
			q.poll();
			q.add(q.poll());
		}
		
		System.out.println(q.peek());
	}
}
