import java.util.Scanner;

import java.util.*;

public class Main {
    static int[][] board;
    static int[][] rotation;
    static int n, m;
    static int[][] copyArray;
    static int[][] copyArray2;
    static boolean[] visited; 
    static int[] numbers;
    
    static int result = Integer.MAX_VALUE;
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        n = scan.nextInt();
        m = scan.nextInt();
        int k = scan.nextInt(); // 배열 돌리는 횟수
        visited = new boolean[k]; 
        copyArray2 = new int[n][m];
        numbers = new int[k];
        board = new int[n][m];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                board[i][j] = scan.nextInt();
            }
        }
        // board에 값 넣기
        
        
        rotation = new int[k][3];
        for(int i = 0; i < k; i++) {
            rotation[i][0] = scan.nextInt();
            rotation[i][1] = scan.nextInt();
            rotation[i][2] = scan.nextInt();
        }         

//        for(int a=0; a<n; a++) {
//			for(int b=0; b<m; b++) {
//				copyArray2[a][b] = board[a][b];
//			}
//		}
        
        perm(0, k);
        
        System.out.println(result);
    }
    
    public static void perm(int cnt, int k) {   	
    	if(cnt == k) { 
    		int[][] copyArray2 = new int[n][m];
    		for(int a=0; a<n; a++) {
    			for(int b=0; b<m; b++) {
    				copyArray2[a][b] = board[a][b];
    			}
    		}
    		
    		for(int i=0; i<k; i++) {
    			rotation(n, m, rotation[numbers[i]][0], rotation[numbers[i]][1], rotation[numbers[i]][2], copyArray2);
    		}
    		
//        	for(int i=0; i<n; i++) {
//        		for(int j=0; j<m; j++) {
//        			System.out.print(copyArray2[i][j]);
//        		}
//        		System.out.println();
//    		}
//        	System.out.println();
    		result = Math.min(result, get_sum_lineby(copyArray2));
    		
    		return;
    	}
    	
    	else {
    		for(int i=0; i<k; i++) {
    			if(!visited[i]) {
    				visited[i] = true;
    				numbers[cnt] = i;
//    				rotation(n, m, rotation[i][0], rotation[i][1], rotation[i][2], arr);
    				perm(cnt+1, k);
    				visited[i] = false;
    			}
    		}
    		
    	}
    	
    }
    
    public static void rotation(int N, int M, int R, int C, int S, int[][] arr) {
    	
    	// int repeat = Math.min(R-C-, M) / 2;
    	
    	int repeat = S;	
    	int goX = R-S-1;
    	int goY = C-S-1;
    	int stopX = R+S-1; 
    	int stopY = C+S-1;
   
    	// 
//    	for(int i=0; i<N; i++) {
//    		for(int j=0; j<M; j++) {
//    			System.out.print(copyArray[i][j]);
//    		}
//    		System.out.println();
//    	}
    	// (R-C, C-S) to (R+C, C+S)
    	for(int i=0; i < repeat; i++) {  // 안쪽으로 들어가는 횟수
    		int temp = arr[goX + i][goY + i]; 
  
    		// 왼
    		for(int j=goX + i; j< stopX - i; j++) {
    			arr[j][goY + i] = arr[j+1][goY + i];
    		}
    		
    			
    		// 아래
    		for(int j=goY + i; j < stopY - i; j++) {
    			arr[stopX-i][j] = arr[stopX-i][j+1];  
    		}
    			
    		// 오른
    		for(int j=stopX - i; j > goX + i; j--) {
    			arr[j][stopY - i] = arr[j-1][stopY - i]; 
    		}
    		
    		// 위
    		for(int j=stopY - i; j > goY + i; j--) {
    			arr[goX+i][j] = arr[goX+i][j-1]; 
    		}
    		
    		arr[goX + i][goY + i + 1] = temp;		
    	}
//    	

    	
    }
    
    public static int get_sum_lineby(int[][] arr) {
    	int value = Integer.MAX_VALUE;
    	int temp = 0;
        for(int i = 0; i < n; i++) {
        	temp = 0;
            for(int j = 0; j < m; j++) {
                temp = arr[i][j] + temp; 
            }
            value = Math.min(value, temp);
        }
    	return value;
    }
  
}
