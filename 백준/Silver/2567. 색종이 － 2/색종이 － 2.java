// 사용하는 라이브러리 Import
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N; // 검정 스카프 개수를 담을 static 변수
	static int[][] board = new int[103][103]; 
	// 경계값 계산 시, zero padding 을 해주기 위해 100보다 큰 +3 만큼 보드 크기를 잡았다
	// 끝자리에 있다면, 4방향에 대해 0이 없기에 계산이 되지 않아 둘레에 포함되지 않을 수 있다.
	// 이런 상황을 방지하기 위해, zero로 패딩을 해주어 계산이 되도록 해주었다. 
	
	static int[] dh = {-1,1,0,0}; // 1의 상하좌우(순서는 다름)에서 0을 찾기 위해 사용
	static int[] dw = {0,0,1,-1}; // 1의 상하좌우(순서는 다름)에서 0을 찾기 위해 사용
	static int result = 0; // 답을 담을 변수 
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 인풋을 받기 위한 조치
		StringTokenizer stk = new StringTokenizer(br.readLine());
		// 인풋을 받기 위한 조치
		
		N = Integer.parseInt(stk.nextToken());
		// 스카프 개수 인풋
		
		// 가로 10, 세로 10 크기의 검은색 천을 넣음
		// 넓이가 아닌 둘레를 구해야함
		
		for(int i=0; i<N; i++) {
			stk = new StringTokenizer(br.readLine());
			// 스카프 위치 인풋을 받기 위한 조치
			int w = Integer.parseInt(stk.nextToken());
			// 스카프 위치 (가로)
			int h = Integer.parseInt(stk.nextToken());
			// 스카프 위치 (세로)
			
			// 검정 스카프 만큼 색칠을 하기 위한 for문
			for(int a=h; a< h+10; a++) {	// 크기는 10x10이니 10 만큼 반복
				for(int b=w; b< w+10; b++) {// 크기는 10x10이니 10 만큼 반복
					board[a][b] = 1; // board 0 -> 1로 표시해 스카프강 위치해 있는 표시 
				}
			}
		
		}
		// end input
		
		// 스카프 입력이 제대로 되었는지 확인하기 위한 것, 사용하지 않음.
//		for(int a=0; a<100; a++) {
//			for(int b=0; b< 100; b++) {
//				System.out.print(board[a][b]);
//			}
//			System.out.println();
//		}
		
		

		// 스카프 둘레 탐색
		for(int a=0; a<100; a++) { 		// 모든 H에 대하여
			for(int b=0; b< 100; b++) { // 모든 W에 대해
				if(board[a][b] == 1) {
					int count  = 0; // 인접한 0의 개수를 담을 변수
					
					for(int d=0; d<4; d++) { // 4방 탐색을 위한 for문 
						int nh = a+dh[d]; // 앞서 만든 dh에 대해 4방 탐색
						int nw = b+dw[d]; // 앞서 만든 dh에 대해 4방 탐색
						
						// 경계값 밖을 조사하려고 하면, ArrayindexoutError가 발생하므로, 
						// continue 해준다.
						if(nh >= 102 || nh < 0 || nw < 0 || nw >= 102) continue;
						
						// 0과 얼마나 만나는지에 대해 count를 센다
						if(board[nh][nw] == 0) { // 0이면
							count += 1; // count ++
						}
					}
					
					if(count == 1) {
						result += 1;
						// 0과 한번만 만난다는 것은 꼭지점이 아닌 변이므로, 둘레 계산시 1만 추가
					} else if(count == 2) {
						result += 2;
						// 0과 두번이 만난다는 것은 꼭지점이므로 둘레 계산에 중복이 된다.
						// 그래서 1을 더하는 것이 아닌 2를 더해 처리해준다
					}
				}
				
			}
			
		}
		
		// 계산 종료
		
		
		System.out.println(result); // 결과 출력	
	}
}