import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Main {
	static int N, cnt;
	static char[][] map;
	static boolean[][] calced;
	static List<Integer> list ;
	static List<int[]> houses ;
	static int[] dirX = {0,0,-1,1};
	static int[] dirY = {-1,1,0,0};
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(br.readLine());
		map = new char[N][N];
		calced = new boolean[N][N];
		list = new ArrayList<>();
		houses = new LinkedList<>();
		
		for(int i=0;i<N;i++) {
			map[i] = br.readLine().toCharArray();
		}
		
		int x,y,nx,ny;
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				cnt=0;
				if(map[i][j]=='1') {
					map[i][j]='0';
					cnt++;
					houses.add(new int[] {j,i});
					while(!houses.isEmpty()) {
						x = houses.get(0)[0];
						y = houses.get(0)[1];
						houses.remove(0);
						for(int k=0;k<4;k++) {
							nx = x+dirX[k];
							ny = y+dirY[k];
							if(nx==N || nx<0 ||ny==N || ny<0) continue;
							if(map[ny][nx]=='1') {
								map[ny][nx]='0';
								cnt++;
								houses.add(new int[] {nx,ny});
							}
						}
					}
					list.add(cnt);
				}
			}
		}
		list.sort((o1,o2)->o1-o2);
		
		System.out.println(list.size());
		for(int a : list) {
			System.out.println(a);
		}
		
		
	}
}
