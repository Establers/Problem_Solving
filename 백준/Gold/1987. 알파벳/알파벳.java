import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int R,C, result;
	static final int[] dirX= {0,0,-1,1}, dirY= {-1,1,0,0};
	static char[][] map;
	static boolean[][] visited;
	static boolean[] visitedC;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R=Integer.parseInt(st.nextToken());
		C=Integer.parseInt(st.nextToken());
		map = new char[R][C];
		visited = new boolean[R][C];
		visitedC= new boolean['Z'-'A'+1];
		
		for(int i=0; i<R;i++) {
			map[i]=br.readLine().toCharArray();
		}
		
		visitedC[map[0][0]-'A']=true;
		visited[0][0]=true;
		run(0,0,1);
		
		System.out.println(result);
	}
	
	private static void run(int x, int y, int cnt) {
		if(cnt>result) result=cnt;
		int nx, ny;
		for(int i=0;i<4;i++) {
			nx = x+dirX[i]; ny=y+dirY[i];
			if(nx<0 || nx==C || ny<0 || ny==R) continue;
			if(visited[ny][nx]) continue;
			if(visitedC[map[ny][nx]-'A']) continue;
			
			visitedC[map[ny][nx]-'A']=true;
			visited[ny][nx]=true;
			run(nx,ny,cnt+1);
			visitedC[map[ny][nx]-'A']=false;
			visited[ny][nx]=false;
		}
	}

}
