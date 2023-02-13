
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashSet<String> set = new HashSet<>();
		ArrayList<String> arrayList = new ArrayList<>();

		int n = Integer.parseInt(br.readLine());
		int k = 1;
		int count = 0;

		for (int a = 0; a < n; a++) {
			arrayList.add(br.readLine());
		}
		while (true) {
			for (int i = 0; i < n; i++) {
				String temp = arrayList.get(i);
				String temp2 = temp.substring(temp.length() - k, temp.length());
//				System.out.println(temp2);
				if (!set.contains(temp2)) {
					set.add(temp2);
					count++;
					if (count == n) {
						System.out.print(k);
						return;
					}
				} else {
//					System.out.println("contain");
					k++;
					count = 0;
					set.clear();
					break;
				}
			}
		}
	}
}
