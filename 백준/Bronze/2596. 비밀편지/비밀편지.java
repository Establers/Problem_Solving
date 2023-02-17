import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {


	public static void main(String[] args) throws NumberFormatException, IOException {
		final int A=0,B=1,C=2,D=3,E=4,F=5,G=6,H=7;
		
		char[][] code = new char[8][6];
		code[A]="000000".toCharArray();
		code[B]="001111".toCharArray();
		code[C]="010011".toCharArray();
		code[D]="011100".toCharArray();
		code[E]="100110".toCharArray();
		code[F]="101001".toCharArray();
		code[G]="110101".toCharArray();
		code[H]="111010".toCharArray();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int wrongCnt[];
		char[] oneWord;
		String result="";
		
		int N = Integer.parseInt(br.readLine());
		String str = br.readLine();
				
		for(int pos=0;pos<N;pos++) {
			boolean matched = false;
			wrongCnt=new int[8];
			oneWord = str.substring(0+pos*6, 6+pos*6).toCharArray();
			for(int i=0;i<6;i++) {
				if(oneWord[i]!=code[A][i]) {
					wrongCnt[A]++;
				}
				if(oneWord[i]!=code[B][i]) {
					wrongCnt[B]++;
				}
				if(oneWord[i]!=code[C][i]) {
					wrongCnt[C]++;
				}
				if(oneWord[i]!=code[D][i]) {
					wrongCnt[D]++;
				}
				if(oneWord[i]!=code[E][i]) {
					wrongCnt[E]++;
				}
				if(oneWord[i]!=code[F][i]) {
					wrongCnt[F]++;
				}
				if(oneWord[i]!=code[G][i]) {
					wrongCnt[G]++;
				}
				if(oneWord[i]!=code[H][i]) {
					wrongCnt[H]++;
				}
			}
			
			//일치하는 경우가 있을 경우
			for(int i=0;i<H+1;i++) {
				if(wrongCnt[i]==0) {
					result+=(char)('A'+i);
					matched=true;
					break;
				}
			}
			//하나를 제외하고 일치할 경우
			if(!matched) {
				boolean[] notOver2 = new boolean[8];
				int trueCnt=0;
				for(int i=0;i<H+1;i++) {
					if(wrongCnt[i]<2) {
						notOver2[i]=true;
						trueCnt++;
					}
				}
				if(trueCnt==0) {
					System.out.println(pos+1);
					return;
				} else if(trueCnt==1) {
					for(int i=0;i<H+1;i++) {
						if(notOver2[i]) {
							result+=(char)('A'+i);
							break;
						}
					}
				}
			}
			
			
		}
		System.out.println(result);
		

		
		br.close();
	}

}
