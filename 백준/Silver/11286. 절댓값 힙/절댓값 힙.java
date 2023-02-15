import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.TreeMap;

public class Main {
	static int N;
	static Map<Integer,Integer> minList = new HashMap<>();
	static TreeMap<Integer,Integer> tm = new TreeMap<>();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(br.readLine());
		
		int n;
		int tmpK,tmpV;
		Entry<Integer,Integer> tmpE;
		for(int i=0;i<N;i++) {
			n=Integer.parseInt(br.readLine());
			
			if(n<0) {
				n*=-1;			
				if(minList.containsKey(n)) {
					minList.put(n, minList.get(n)+1);
				} else
					minList.put(n, 1);
			}
			
			if(n==0) {
				if(tm.size()==0) {
					bw.write("0\n");
				} else {
					tmpE= tm.pollFirstEntry();
					tmpK = tmpE.getKey();
					tmpV = tmpE.getValue();
					
					if(minList.containsKey(tmpK)) { //음수면 tmpK =-1; , minList 정리 (value0일시 삭제)
						int tmp;
						if((tmp = minList.get(tmpK)-1)==0) minList.remove(tmpK);
						else minList.put(tmpK, tmp);
						
						tmpK*=-1;
					}
					
					bw.write(String.valueOf(tmpK));
					bw.newLine();
					
					if(tmpE.getValue()>1) { //감소시킨 value가 1이상이면 다시 treemap에 넣는다.
						tm.put(tmpE.getKey(),tmpV-1);
					}
				}
			} else {
				if(tm.containsKey(n)) {
					tm.put(n, tm.get(n)+1);
				} else {
					tm.put(n, 1);
				}
			}
		}
		bw.flush();
	}

}
