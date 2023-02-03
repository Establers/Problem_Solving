

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
	    BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
	    StringTokenizer stk = null;

	    stk = new StringTokenizer(br.readLine(), " ");
	    double a = Integer.parseInt(stk.nextToken());
	    double b = Integer.parseInt(stk.nextToken());
	    double c = Integer.parseInt(stk.nextToken());
	    int num = (int)(Math.ceil((c-b)/(a-b)));
	    System.out.println(num);
	}
}
