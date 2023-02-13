
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(stk.nextToken());
		int K = Integer.parseInt(stk.nextToken());
		int cnt = 0;
		
		LinkedList<Integer> linkedList = new LinkedList<Integer>();
		
		for(int i=1; i<=N; i++) {
			linkedList.add(i);
		}
		
		ListIterator<Integer> iterator = linkedList.listIterator(linkedList.size());

		while(iterator.hasPrevious()) {
			iterator.previous();
		}
		System.out.print("<");
		while(!linkedList.isEmpty()) {
			
			for(int i=0; i<K; i++) {
				if(iterator.hasNext()) {
					iterator.next();
				} else {
					for(int b=0; b<linkedList.size()-1; b++) {
						iterator.previous();
					}
				}
			}
			// System.out.println("제거할 값 : " + iterator.previous()); 
			System.out.print(iterator.previous());
			iterator.remove();
			if(!linkedList.isEmpty()) System.out.print(", ");
		}
		System.out.print(">");
		
	}
}
