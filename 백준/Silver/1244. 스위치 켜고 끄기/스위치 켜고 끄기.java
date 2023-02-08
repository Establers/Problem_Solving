
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[] arr;
	static int[][] stu;
	static int n;
	
	public static void turnSwitch(int a) {
		
		if(arr[a-1] == 0) {
			arr[a-1] = 1;
		} else if(arr[a-1] == 1) {
			arr[a-1] = 0;
		}
	}
	
	public static void change(int[] student) {
		if(student[0] == 1) // 남
		{
			for(int a=1; a<=n; a++) {
				if(a%student[1] == 0) {
					turnSwitch(a);
				}
			}
		} 
		else // 여
		{
			//System.out.println(Arrays.toString(arr));
			int cnt = 1;
			
			while(true) {
				int l = student[1]-cnt;
				int r = student[1]+cnt;
				if(l <= 0 || r > n) {
					break;
				}
				int left = arr[l-1];
				int right = arr[r-1];
				//System.out.println("left "+left +" " +"right "+right);
				if(left != right) {
					break;
				} else {
					cnt += 1;
				}
			}
			cnt += -1;
			//System.out.println("cnt "+cnt);
			// 끝 찾음
			for(int i=student[1]-cnt; i<=student[1]+cnt; i++) {
				turnSwitch(i);
			}
		}
	
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		n = Integer.parseInt(br.readLine()); // 스위치 수
		arr = new int[n];
		StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(stk.nextToken()); 
		}
		
		int studentsNum = Integer.parseInt(br.readLine());
		stu = new int[studentsNum][2];
		
		for(int i=0; i<studentsNum; i++) {
			stk = new StringTokenizer(br.readLine(), " ");
			stu[i][0] = Integer.parseInt(stk.nextToken()); // 남1 여2
			stu[i][1] = Integer.parseInt(stk.nextToken()); // 자기 번호 
		}
		
		for(int i=0; i<studentsNum; i++) {
			change(stu[i]);
		}
		
		// System.out.println(Arrays.toString(arr));
		int count = 0;
		for(int c : arr) {
			sb.append(c+" ");
			count += 1;
			if(count % 20 == 0) {
				sb.deleteCharAt(sb.length()-1);
				sb.append("\n");
			}
		}
		System.out.println(sb.toString());
	}
}
