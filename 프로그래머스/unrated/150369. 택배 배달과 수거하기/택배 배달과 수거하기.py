def solution(cap, n, deliveries, pickups):
    answer = 0
    dv = 0
    pi = 0
    
    # 항상 끝에서 부터 와야함
    for i in range(n-1, -1, -1) :
        
        # 해당 거리를 방문
        visit_cnt = 0
        
        dv += deliveries[i]
        pi += pickups[i]
        # 끝에 갔을 때 배달이랑 수거양
        
        # 여러번 할 수 있으니
        while True :
            # print("i",i, "dv",dv,"pi",pi)
            if(dv > 0 or pi > 0) :
                # 뭔가를 가지고 있다면
                dv -= cap
                pi -= cap
                # 용량 만큼 빼주고
                
                # 방문은 해야하니 + 1
                visit_cnt += 1
            else :
                break
                
        answer += 2 * visit_cnt * (i+1)
        
    return answer