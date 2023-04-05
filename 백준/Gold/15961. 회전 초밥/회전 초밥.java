import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, D, K, C, max;
	static int[] belt, visited;

	public static void main(String[] args) throws IOException {
		init();
		System.out.println(findAnswer());
	}

	private static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		belt = new int[N];
		visited = new int[D + 1];

		for (int i = 0; i < N; i++) {
			belt[i] = Integer.parseInt(br.readLine());
		}
	}

	private static int findAnswer() {
		int count = 0;
		int max = 0;

		for (int i = 0; i < K; i++) {
			if (visited[belt[i]] == 0) {
				count++;
			}
			visited[belt[i]]++;
		}

		max = count;

		for (int i = 1; i <= N; i++) {
			if (max <= count) {
				max = count;
				if (visited[C] == 0) {
					max++;
				}
			}
			if (i == N) {
				return max;
			}
			
			visited[belt[i - 1]]--;
			if (visited[belt[i - 1]] == 0) {
				count--;
			}

			if (visited[belt[(i + K - 1) % N]] == 0) {
				count++;
			}
			visited[belt[(i + K - 1) % N]]++;
		}
		return max;
	}
}