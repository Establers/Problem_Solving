import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;

public class Main {
	static int N,K;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] str = br.readLine().split(" "); 
		N=Integer.parseInt(str[0]);
		K=Integer.parseInt(str[1]);
		
		List<Integer> list = new LinkedList<>();
		
		for(int i=1;i<=N;i++) {
			list.add(i);
		}
		
		ListIterator<Integer> itr = list.listIterator();
		
		bw.write("<");
		for(int i=0;list.size()>0 && i<N;i++) {
			int k=-1;
			for(int j=0;j<K;j++) {
				
				if(itr.hasNext()) {
					k=itr.next().intValue();
				} else {
					itr = list.listIterator();
					if(itr.hasNext())
						k = itr.next().intValue();
					else break;
				}
				
			}
			itr.remove();
			bw.write(String.valueOf(k));
			if(list.size()==0) {
				bw.write(">");
				break;
			}
			bw.write(", ");
		}
		bw.flush();
		
		
		
		
		
	}

}
