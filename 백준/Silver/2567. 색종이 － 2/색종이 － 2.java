import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static boolean[][] map = new boolean[100][100];
	static int N, result;
	static int[] dirX= {0,0,-1,1}, dirY = {-1, 1, 0, 0};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int disL, disB;
		N = Integer.parseInt(br.readLine());
				
		for(int i=0;i<N;i++) {
			st=new StringTokenizer(br.readLine());
			disL=Integer.parseInt(st.nextToken());
			disB=Integer.parseInt(st.nextToken());
			for(int y=100-disB-10;y<100-disB;y++) {
				for(int x=disL;x-disL<10;x++) {
					// 3 4 5 6 7 8 9 10 11 12
					map[y][x]=true;
				}
			}
		}

		int nx,ny;
		for(int y=0;y<100;y++) {
			for(int x=0;x<100;x++) {
				for(int index=0;index<4;index++) {
					nx=x+dirX[index]; ny=y+dirY[index];
					if(map[y][x] && ((ny<0 || ny==100 || nx<0 || nx==100) || !map[ny][nx])) result++;
				}
			}
		}
		System.out.println(result);
		
	}

}
