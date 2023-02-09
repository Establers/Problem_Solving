import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Values {
	int a;
	int c;
	int g;
	int t;
	
	public Values(int a, int c, int g, int t){
		this.a = a;
		this.c = c;
		this.g = g;
		this.t = t;
	}

	@Override
	public String toString() {
		return "Values [a=" + a + ", c=" + c + ", g=" + g + ", t=" + t + "]";
	}
	
}

public class Main {
	static int S;
	static int P;
	static int A,C,G,T;
	static String DNA;
	static int result = 0;
	ArrayList<Integer[]> li = new ArrayList<>();
	
	public static int count(String str, char ch) {
		int co = (int)str.chars().filter(c -> c == ch).count();
		return co;
	}
	
	public static boolean checkSum(String str, int a, int c, int g, int t) {
		if(count(str, 'A') >= a && count(str, 'C') >= c && count(str, 'G') >= g && count(str, 'T') >= t) {
			return true;
		}
		return false;
	}
	

	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer stk = new StringTokenizer(br.readLine());
		S = Integer.parseInt(stk.nextToken());
		P = Integer.parseInt(stk.nextToken());
		
		
		DNA = br.readLine();
		
		stk = new StringTokenizer(br.readLine());
		A = Integer.parseInt(stk.nextToken()); // 0
		C = Integer.parseInt(stk.nextToken()); // 1
		G = Integer.parseInt(stk.nextToken()); // 2
		T = Integer.parseInt(stk.nextToken()); // 3
		
		Values val = new Values(0, 0, 0, 0);
		
		String str = DNA.substring(0, P);
		if(S == P) {
			str = DNA;
			val.a = count(str, 'A');
			val.c = count(str, 'C');
			val.g = count(str, 'G');
			val.t = count(str, 'T');
			if (
					val.a >= A
				&& 	val.c >= C
				&& 	val.g >= G
				&& 	val.t >= T
					) {
				result += 1;
			}
			System.out.println(result);
			return;
		}
		val.a = count(str, 'A');
		val.c = count(str, 'C');
		val.g = count(str, 'G');
		val.t = count(str, 'T');
		// System.out.println(val.toString());
		if (
				val.a >= A
			&& 	val.c >= C
			&& 	val.g >= G
			&& 	val.t >= T
				) {
			result += 1;
		}
		for(int i=0; i<S-P; i++) {
			switch (DNA.charAt(i)) {
			case 'A':
				val.a += -1;
				break;
			case 'C':
				val.c += -1;
				break;
			case 'G':
				val.g += -1;
				break;
			case 'T':
				val.t += -1;
				break;
			}
			//System.out.println(str.toString());
			DNA.charAt(str.length()+i);
			//System.out.println(DNA.charAt(str.length()+i));
			switch (DNA.charAt(str.length()+i)) {
			case 'A':
				val.a += 1;
				break;
			case 'C':
				val.c += 1;
				break;
			case 'G':
				val.g += 1;
				break;
			case 'T':
				val.t += 1;
				break;
			}
			//System.out.println(val.toString());
			if (
					val.a >= A
				&& 	val.c >= C
				&& 	val.g >= G
				&& 	val.t >= T
					) {
				result += 1;
			}
		}
	
		
		System.out.println(result);
		
		
	}
}
