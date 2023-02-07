
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int[][] arr;
    static int n;
    static int result = Integer.MAX_VALUE;
    static int sum = 0;
    static boolean[] visited;

    public static void recur(int depth, int sum, int pre) {
        if(depth == n-1) {
        	if (arr[pre][0] != 0) {
        		result = Math.min(result, sum + arr[pre][0]);
        	}             
            return;
        }

        
        for(int i=1; i<n; i++) {
            if(visited[i] == false && arr[pre][i] != 0) {
                visited[i] = true;
                // System.out.println(pre +" "+i);
	            recur(depth+1, sum + arr[pre][i], i);
	            visited[i] = false;    
            }
       }
    }


public static void main(String[] args) throws NumberFormatException, IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer stk = null;

    
    n = Integer.parseInt(br.readLine());
    arr = new int[n][n];
    visited = new boolean[n];
    
    for(int i=0; i<n; i++) {
        stk = new StringTokenizer(br.readLine()," ");
        for(int j=0; j<n; j++) {
            arr[i][j] = Integer.parseInt(stk.nextToken());
        }
    }
    recur(0, 0, 0);
    System.out.println(result);
    
    }
}