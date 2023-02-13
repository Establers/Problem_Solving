// 요세푸스 문제


import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int N = scanner.nextInt();
		int M = scanner.nextInt();
		int cnt = 0;
		
		Queue<Integer> queue = new LinkedList<Integer>();
		
		for(int i=1; i<=N; i++) {
			queue.add(i);
		}
		System.out.print("<");
		while(!queue.isEmpty()) {
			for(int i=0; i<M-1; i++) {
				if(!queue.isEmpty()) {
					queue.add(queue.poll());
				}
			}
			
			System.out.print(queue.poll());
			if(!queue.isEmpty()) System.out.print(", ");
		}
		
		System.out.print(">");
	}
}