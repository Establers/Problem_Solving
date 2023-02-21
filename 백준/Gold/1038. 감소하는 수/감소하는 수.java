import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	static ArrayList<Long> arrayList = new ArrayList<>();
	static int n;
	
	public static void bt(int depth, long num) {
		if (depth == 10) {
			return;
		}
		
		arrayList.add(num);
		// System.out.println(num);
		for(int i=0; i< 10; i++) {
			if(num % 10 > i) {
				// 감소하는 수를 만들 수 있는 경우
				bt(depth + 1, (num * 10) + i);
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		n = scanner.nextInt();
		
		// 9 8 7 6 5 4 3 2 1 0
		// 2 ^ 10 (부분집합 개수)

		for(int i=0; i<10; i++) {
			bt(0, i);
		}
			
		Collections.sort(arrayList);
		
		if (n >= 1023) {
			System.out.println(-1);
			return;
		} else if(n < 10) { 
			System.out.println(n);
			return;
		} else {
			System.out.println(arrayList.get(n));
		}
		
		
		
	}
}