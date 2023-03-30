import java.io.*;
import java.util.*;

public class Main {
	final static int BOARD_SIZE = 9;
	static int[][] board = new int[BOARD_SIZE][BOARD_SIZE];
	static int countZero = 0;

	public static void main(String[] args) throws IOException {
		init();
		playSdoku();
	}

	private static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int i = 0; i < BOARD_SIZE; i++) {
			String tmp = br.readLine();
			for (int j = 0; j < BOARD_SIZE; j++) {
				board[i][j] = tmp.charAt(j) - '0';
				if (board[i][j] == 0) {
					countZero++;
				}
			}
		}
	}

	private static void playSdoku() {
		for (int i = 0; i < BOARD_SIZE; i++) {
			for (int j = 0; j < BOARD_SIZE; j++) {
				if (countZero == 0) {
					printBoard();
					System.exit(0);
				}

				if (board[i][j] != 0) {
					continue;
				}

				Set<Integer> usedNums = new HashSet<>();
				usedNums.addAll(findUsableNumAtRow(i));
				usedNums.addAll(findUsableNumAtCol(j));
				usedNums.addAll(findUsableNumAtBox(i, j));
				List<Integer> usableNums = new ArrayList<>(removeUsedNum(usedNums));
				Collections.sort(usableNums);

				for (int num : usableNums) {
					board[i][j] = num;
					countZero--;
					playSdoku();
					board[i][j] = 0;
					countZero++;
				}
				return;
			}
		}
	}

	private static Set<Integer> removeUsedNum(Set<Integer> usedNums) {
		Set<Integer> usableNums = new HashSet<>();
		usableNums.addAll(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));
		for (int num : usedNums) {
			if (usableNums.contains(num)) {
				usableNums.remove(num);
			}
		}
		return usableNums;
	}

	private static Set<Integer> findUsableNumAtRow(int x) {
		Set<Integer> UsedNums = new HashSet<>();
		for (int i = 0; i < BOARD_SIZE; i++) {
			if (board[x][i] != 0) {
				UsedNums.add(board[x][i]);
			}
		}
		return UsedNums;
	}

	private static Set<Integer> findUsableNumAtCol(int y) {
		Set<Integer> UsedNums = new HashSet<>();
		for (int i = 0; i < BOARD_SIZE; i++) {
			if (board[i][y] != 0) {
				UsedNums.add(board[i][y]);
			}
		}
		return UsedNums;
	}

	private static Set<Integer> findUsableNumAtBox(int x, int y) {
		Set<Integer> UsedNums = new HashSet<>();
		int StartX = x - (x % 3);
		int StartY = y - (y % 3);
		for (int i = StartX; i < StartX + 3; i++) {
			for (int j = StartY; j < StartY + 3; j++) {
				if (board[i][j] != 0) {
					UsedNums.add(board[i][j]);
				}
			}
		}
		return UsedNums;
	}

	private static void printBoard() {
		for (int i = 0; i < BOARD_SIZE; i++) {
			for (int j = 0; j < BOARD_SIZE; j++) {
				System.out.print(board[i][j]);
			}
			System.out.println();
		}
	}
}