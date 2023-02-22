import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		int N, cnt;
		boolean[][] map;
		List<Integer> list ;
		Queue<int[]> houses ;
		int[] dirX = {0,0,-1,1};
		int[] dirY = {-1,1,0,0};
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new boolean[N][N];
		list = new ArrayList<>();
		houses = new LinkedList<>();
		
		char[] arr;
		for(int i=0;i<N;i++) {
			arr = br.readLine().toCharArray();
			for(int j=0;j<N;j++) {
				map[i][j] = arr[j]=='1'?true:false;
			}
		}
		
		int x,y,nx,ny;
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				cnt=0;
				if(map[i][j]) {
					map[i][j]=false;
					cnt++;
					houses.add(new int[] {j,i});
					while(!houses.isEmpty()) {
						x = houses.peek()[0];
						y = houses.poll()[1];
						for(int k=0;k<4;k++) {
							nx = x+dirX[k];
							ny = y+dirY[k];
							if(nx==N || nx<0 ||ny==N || ny<0) continue;
							if(map[ny][nx]) {
								map[ny][nx]=false;
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
