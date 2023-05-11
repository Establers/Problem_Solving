"""
1. 양, 늑대 수를 들고다니면서 DFS로 이진트리 방문
2. 조건을 만족할 때 마다 max값으로 answer 값을 갱신 (sheep 개수)
"""


answer = 0

def solution(info, edges):
    
    # visited = [ False for _ in range(len(info)+1)]

    def dfs(node, s, w, visited_node) :
        global answer
        # print(visited_node)
        if s <= w : return     
        if s > w : 
            # 조건에 만족하는 경우
            answer = max(answer, s)

        # 탐색
        # p, c = edges[node]            
        # print(p, c)
        # 자기가 바로 양옆만 갈 수 있는 것이 아님
        for p, c in edges : 
            if p in visited_node and c not in visited_node :           
                if info[c] == 0 : # 양
                    visited_node.append(c)                
                    dfs(c, s + 1, w, visited_node)
                    visited_node.pop()
                else : # 늑대
                    visited_node.append(c)
                    dfs(c, s, w + 1, visited_node) 
                    visited_node.pop()
            # dfs 종료 후, visited_node 끝 값 빼기
                # visited[c] = False
                # visited_node.pop()
                
    # visited[0] = True
    dfs(0, 1, 0, [0]) # 노드번호, 양 수, 늑대 수
    
    return answer