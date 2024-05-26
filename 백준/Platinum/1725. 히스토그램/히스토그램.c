#include <stdio.h>
#define max(a, b) ( (a) < (b) ? (b) : (a) )
#define min(a, b) ( (a) > (b) ? (b) : (a) )
int N;//히스토그램수
int H[100000+10] = {0, };//히스토그램 높이
typedef struct {
    int idx;
    int h;
}stack;
stack s[123456];
int sp = 0;
 
void append(int idx, int h){
    s[sp].idx=  idx;
    s[sp].h = h;
    sp++;
}
 
stack popleft(){
    return s[--sp];
}
 
int is_empty(){
    return sp == 0;
}
 
stack peek(){
    return s[sp-1];
}
 
long long answer = -1;
int InputData(void) {
    scanf("%d", &N);
    if (N == 0) return 0;
 
    for (int i=0; i<N; i++){
        scanf("%d", &H[i]);
    }
 
    sp = 0;
    H[N] = 0;
    answer = -1;
 
    for(int i=0; i<=N; i++){
        int start = i;
        int next_h = H[i]; 
 
 
        while(!is_empty() && peek().h >= next_h){
         
            stack st = popleft();
            start = st.idx;
            int now_h = st.h;
 
            answer = max(answer, (long long)(i - start) * now_h);
        }
 
        append(start, next_h);
    }
 
    while(!is_empty()){
        stack a = popleft();
        int width = 1;
        if(!is_empty()){
            width = peek().idx + 1;
        }
        answer = max(answer, (N - width + 1) * a.h);
    }
 
    printf("%lld\n", answer);
    return 0;
}
 
int main(void) {
 
    while(InputData()){//입력받는 부분
 
        // 한 테스크 케이스에 대해서 진행해야하니 입력을 한줄 받으면 그때 진행해야함
 
        // printf("%lld\n", answer);//출력하는 부분
    }
    return 0;
}