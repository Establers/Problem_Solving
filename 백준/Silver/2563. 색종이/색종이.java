
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static int N,result;
	static boolean map[][];
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(br.readLine());
		map = new boolean[100][100];

		
		StringTokenizer st;
		int x, y;
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			x=Integer.parseInt(st.nextToken());
			y=Integer.parseInt(st.nextToken());
			for(int tmpy=y;tmpy<y+10;tmpy++) {
				for(int tmpx=x;tmpx<x+10;tmpx++) {
					map[tmpy][tmpx]=true;
				}
			}
		}
		result=0;
		for(int ty=0;ty<100;ty++) {
			for(int tx=0;tx<100;tx++) {
				if(map[ty][tx]) result++;
			}
		}
		System.out.println(result);
		
	}	
}
