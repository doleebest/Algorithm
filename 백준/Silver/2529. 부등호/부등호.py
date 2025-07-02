k = int(input())
signs = input().split()

min_ans = ''
max_ans = ''
visited = [False] * 10  # 0~9 숫자 사용 여부


def valid(x, y, op):
    if op == '<':
        return x < y
    else:
        return x > y


def dfs(depth, num_str):
    global min_ans, max_ans

    if depth == k + 1:
        if not min_ans:
            min_ans = num_str
        else:
            max_ans = num_str
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or valid(int(num_str[-1]), i, signs[depth - 1]):
                visited[i] = True
                dfs(depth + 1, num_str + str(i))
                visited[i] = False


# 작은 숫자부터 시도 → min_ans 먼저 저장됨, 마지막 건 max_ans 됨
dfs(0, '')

print(max_ans)
print(min_ans)