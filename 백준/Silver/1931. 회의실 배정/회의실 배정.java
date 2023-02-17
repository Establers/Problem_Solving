import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int N;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		Meeting[] m = new Meeting[N];
		
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			m[i] = new Meeting(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		}
		Arrays.sort(m);
		int time=0,cnt=0;
		for(int i=0;i<N;i++) {
			if(time<=m[i].start) {
				time=m[i].end;
				cnt++;
			}
		}
		System.out.println(cnt);
	}
	
	public static class Meeting implements Comparable<Meeting>{
		int start, end;

		public Meeting() {};
		public Meeting(int start, int end) {
			super();
			this.start = start;
			this.end = end;
		}
		@Override
		public int compareTo(Meeting o) {
			return end!=o.end?end-o.end:start-o.start;
		}
		@Override
		public String toString() {
			return "Meeting [start=" + start + ", end=" + end + "]";
		}
	}
	
}
