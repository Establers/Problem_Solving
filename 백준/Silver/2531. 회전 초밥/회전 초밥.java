import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	static int N, D, K, C, max;
	static int[] belt;
	static List<Set<Integer>> choosedSushis;

	public static void main(String[] args) throws IOException {
		init();
		findEatingCase();
		findAnswer();
		System.out.println(max);
	}

	private static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		belt = new int[N];
		choosedSushis = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			belt[i] = Integer.parseInt(br.readLine());
		}
	}

	private static void findEatingCase() {
		Set<Integer> choosedSushi;
		max = 0;
		for (int i = 0; i < N; i++) {
			choosedSushi = new HashSet<>();
			for (int j = i; j < i + K; j++) {
				choosedSushi.add(belt[j % N]);
			}

			if (choosedSushi.size() > max) {
				choosedSushis.clear();
				choosedSushis.add(choosedSushi);
				max = choosedSushi.size();
				continue;
			}

			if (choosedSushi.size() == max) {
				choosedSushis.add(choosedSushi);
			}
		}
	}

	private static void findAnswer() {
		for (Set<Integer> sushis : choosedSushis) {
			if (!sushis.contains(C)) {
				max++;
				break;
			}
		}
	}
}