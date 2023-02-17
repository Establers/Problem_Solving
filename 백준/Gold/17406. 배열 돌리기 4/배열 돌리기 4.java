import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static int N, M, K, tmp;
	static int result = Integer.MAX_VALUE;
	static int[][] map, rotArr;
	static boolean[] taken;
	static final int R=0, C=1, S=2;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N=Integer.parseInt(st.nextToken());
		M=Integer.parseInt(st.nextToken());
		K=Integer.parseInt(st.nextToken());
		map = new int[N][M];
		rotArr = new int[K][3];
		taken = new boolean[K];
		
		for(int y=0;y<N;y++) {
			st = new StringTokenizer(br.readLine());
			for(int x=0;x<M;x++) {
				map[y][x] = Integer.parseInt(st.nextToken());
			}
		}
		
		for(int i=0;i<K;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<3;j++) {
				rotArr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int cnt=K;
		//연산 수행, 먼저 수행할 회전방법 지정
		for(int i=0;i<K;i++) {
			doRotate(cnt-1,i);
		}
		System.out.println(result);
		
	}

	private static void doRotate(int cnt, int pick) {
//		System.out.print("방법"+pick+" / ");
		if(!taken[pick]) {
			taken[pick]=true;

			
			//연산 수행
			for(int size=rotArr[pick][S];size>0;size--) {
				doRoll(pick,size);
			}
			
			//다음 연산 지정
			for(int i=0;i<K;i++) {
				if(!taken[i])
					doRotate(cnt-1,i);
			}
			if(cnt==0) {
				calcRows();
			}
			
			//연산 역수행
			for(int size=rotArr[pick][S];size>0;size--) {
				doRollReverse(pick, size);
			}
			
			
			taken[pick]=false;
		}
	}


	//주어진 크기의 사각형 시계 반대방향 roll
	private static void doRollReverse(int pick, int size) {
		int LTY, LTX; //LEFT TOP지점의 X,Y
		LTY=rotArr[pick][R]-size-1;
		LTX=rotArr[pick][C]-size-1;
		
		int x,y;
		
		tmp=map[LTY][LTX];
		x=LTX; y=LTY; //위쪽변 roll
		for(;x<LTX+size*2;x++) {
			map[y][x]=map[y][x+1]; 
		}
		x=LTX+size*2; //우측변 roll
		for(;y<LTY+size*2;y++) {
			map[y][x]=map[y+1][x]; 
		}
		y=LTY+size*2; //아랫변 roll
		for(;x>LTX;x--) {
			map[y][x]=map[y][x-1]; 
		}
		x=LTX; //좌측변 roll
		for(;y>LTY;y--) {
			map[y][x]=map[y-1][x]; 
		}
		map[LTY+1][LTX] = tmp;
		
	}
	
	private static void doRoll(int pick, int size) {
		int LTY, LTX; //LEFT TOP지점의 X,Y
		LTY=rotArr[pick][R]-size-1;
		LTX=rotArr[pick][C]-size-1;

		int x,y;
		
		tmp=map[LTY][LTX+2*size-1];
		x=LTX+2*size-1; y=LTY; //위쪽변 roll
		for(;x>LTX;x--) {
			map[y][x]=map[y][x-1]; 
		}
		x=LTX; y=LTY; //좌측변 roll
		for(;y<LTY+size*2;y++) {
			map[y][x]=map[y+1][x]; 
		}
		y=LTY+size*2; //아랫변 roll
		for(;x<LTX+size*2;x++) {
			map[y][x]=map[y][x+1]; 
		}
		x=LTX+size*2; //우측변 roll
		for(;y>LTY;y--) {
			map[y][x]=map[y-1][x]; 
		}
		map[LTY][LTX+2*size] = tmp;
		
	}


	private static void calcRows() {
		int total;
		for(int[] row : map) {
			total=0;
			for(int i : row) {
				total+=i;
			}
			result = Math.min(total, result);
		}
	}

}
