def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    
    for com in range(n) :
        if visited[com] ==False :
            dfs(n, computers, com, visited)
            answer+=1 # dfs로 최대한 하나의 네트워크 생성 후 빠져나오면 카운트
    return answer

def dfs(n, computers, com, visited) :
    visited[com] = True
    for connect in range(n) :
        if connect != com and computers[com][connect] ==1 :
            if visited[connect] == False :
                dfs(n, computers, connect, visited)