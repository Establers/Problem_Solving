import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, numWhite, numBlue;
	static final boolean BLUE = true, WHITE = false;
	static boolean[][] Map;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		Map = new boolean[N][N];
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<N;j++) {
				if(st.nextToken().equals("1")) {
					Map[i][j]=BLUE;
				} //else Map[i][j]=WHITE;
			}
		}
		boolean isDividable=false; 
		boolean previous = Map[0][0];
		for(int i=0;i<N && !isDividable;i++) {
			for(int j=0;j<N;j++) {
				if(isDividable = (previous != Map[i][j])) {
					break;
				}
			}
		}
		if(isDividable)
			checkColor(N,0,0);
		else {
			if(previous) numBlue++;
			else numWhite++;
		}
		
		System.out.println(numWhite);
		System.out.println(numBlue);
	}
	
	private static void checkColor(int n,int startX, int startY) {
		n=n/2;
		boolean isDividable, previous;
		//(isDividable == true) = 나눌 수 있으면 = 사각형 내부 요소들이 다르면 > 비교 중지하고 나누기 시작
		//(isDividable == false) = 나눌 수 없으면 = 사각형 내부 요소들이 다 같다면 > previous에 해당하는 색 ++, 분할 X
		
		//첫번째 사각형
		isDividable=false; 
		previous = Map[startY][startX];
		for(int i=startY;i-startY<n && !isDividable;i++) {
			for(int j=startX;j-startX<n;j++) {
				if(isDividable = (previous != Map[i][j])) {
					break;
				}
			}
		}
		if(isDividable) {
			checkColor(n,startX,startY);
		} else {
			if(previous) numBlue++;
			else numWhite++;
		}		
		
		//두번째 사각형
		isDividable=false;
		previous = Map[startY+n][startX];
		for(int i=startY+n;i-startY-n<n && !isDividable;i++) {
			for(int j=startX;j-startX<n;j++) {
				if(isDividable = (previous != Map[i][j])) {
					break;
				}
			}
		}
		if(isDividable) {
			checkColor(n,startX,startY+n);
		} else {
			if(previous) numBlue++;
			else numWhite++;
		}		
		
		
		//세번째 사각형
		isDividable=false;
		previous = Map[startY][startX+n];
		for(int i=startY;i-startY<n && !isDividable;i++) {
			for(int j=startX+n;j-startX-n<n;j++) {
				if(isDividable = (previous != Map[i][j])) {
					break;
				}
			}
		}
		if(isDividable) {
			checkColor(n,startX+n,startY);
		} else {
			if(previous) numBlue++;
			else numWhite++;
		}		

		
		//네번째 사각형
		isDividable=false;
		previous = Map[startY+n][startX+n];
		for(int i=startY+n;i-startY-n<n && !isDividable;i++) {
			for(int j=startX+n;j-startX-n<n;j++) {
				if(isDividable = (previous != Map[i][j])) {
					break;
				}
			}
		}
		if(isDividable) {
			checkColor(n,startX+n,startY+n);
		} else {
			if(previous) numBlue++;
			else numWhite++;
		}		
		
	}
	
}
