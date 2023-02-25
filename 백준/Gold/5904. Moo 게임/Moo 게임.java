
import java.util.ArrayList;
import java.util.Scanner;

// Moooo... Mooooooo... 아무무 ..ㅎㅎ;;
public class Main {
	static int N;
	static ArrayList<Integer> seq = new ArrayList<>();
	static char answer;
	
	public static void find_half(int k, int now_idx) {
		// 너.. 축에 있니?
		if(k == 0) {
//			System.out.println("k = 0 :" + now_idx);
			if(now_idx == 0) {
				answer = 'm';
			} else {
				answer = 'o';
			}
			return;
		}
//		System.out.println("now_idx : " + now_idx);
		if(seq.get(k-1)-1 < now_idx && now_idx < seq.get(k-1) + k+3) {
			if(now_idx == seq.get(k-1)) {
				// 너.. 축인데도 M에 있구나?
				answer = 'm';
				return;
			} else {
				answer = 'o';
				return;
			}
		}
		
		// 축에 없꾸나 왼쪽에 있니.. 오른쪽에 있니?..
		else if(seq.get(k-1) + k+3 <= now_idx){
			// 오른쪽
			find_half(k-1, (now_idx -(seq.get(k-1)) -(k+3)));
		} else if(now_idx <= seq.get(k-1)){
			// 왼쪽
//			System.out.println("왼쪽");
			find_half(k-1, now_idx);
		}
	}
	
	
	
	public static void main(String[] args) {
		// 대칭되는 형식의 그거다
		// 대칭? -> 분할정복?
		Scanner scanner = new Scanner(System.in);
		N = scanner.nextInt();
		int k = 2;
		seq.add(3);
		seq.add(10);
		
		while(true) {
			if(seq.get(seq.size()-1) > N) {
				 break;
			}
			seq.add(
					(seq.get(k-1)*2) + k + 3);
			k += 1;
		}
		k += -1;
//		System.out.println(k);
		find_half(k, N-1);
//		System.out.println(seq.get(seq.size()-1));
//		System.out.println(seq.get(1));
		System.out.println(answer);
		
	}
}
