def solution(sizes):
    width = []
    height = []
    for s in sizes :
        if s[0]<s[1] :
            s[0],s[1] = s[1],s[0]
        width.append(s[0])
        height.append(s[1])
    return max(width) * max(height)
