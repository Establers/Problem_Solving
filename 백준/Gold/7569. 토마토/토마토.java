import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n, m, h;
	static int[][][] board;
	static boolean[][][] visited;
	static Queue<int[]> q = new ArrayDeque<>();
	static int[] dx = { 1, -1, 0, 0, 0, 0 };
	static int[] dy = { 0, 0, 1, -1, 0, 0 };
	static int[] dz = { 0, 0, 0, 0, 1, -1 };
	public static void bfs() {
// 1이 있는 위치 넣기
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				for (int k = 0; k < h; k++) {
					if (board[i][j][k] == 1) {
						q.add(new int[] { i, j, k });
					}
				}
			}
		}

		while (!q.isEmpty()) {
			int[] now = q.poll();
			int x = now[0];
			int y = now[1];
			int z = now[2];

			for (int i = 0; i < 6; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				int nz = z + dz[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < m && 0 <= nz && nz < h) {
					// 경계안
					if (!visited[nx][ny][nz] && board[nx][ny][nz] == 0) {
						// 방문하지 않았고, 토마토가 들어있는 칸 일 경우
						visited[nx][ny][nz] = true;
						board[nx][ny][nz] = board[x][y][z] + 1;
						q.add(new int[] { nx, ny, nz });
					}
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		m = Integer.parseInt(stk.nextToken()); // 6
		n = Integer.parseInt(stk.nextToken()); // 4
		h = Integer.parseInt(stk.nextToken()); // 2

		board = new int[n][m][h];
		visited = new boolean[n][m][h];

		int cnt = 0;
		int max_value = 0;
		for (int k = 0; k < h; k++) {
			for (int i = 0; i < n; i++) {
				stk = new StringTokenizer(br.readLine());
				for (int j = 0; j < m; j++) {
					int temp = Integer.parseInt(stk.nextToken());
					cnt += temp;
					board[i][j][k] = temp;
				}
			}
		}

		// board 정보 다 받음

		bfs();
		
		for(int k=0; k<h; k++) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					max_value = Math.max(max_value, board[i][j][k]);
					if (board[i][j][k] == 0) {
						System.out.println(-1);
						return;
					}
				}
			}
		}


		System.out.println(max_value - 1);

	}

}