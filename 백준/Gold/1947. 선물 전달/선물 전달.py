n = int(input())
MOD = 1000000000

d = [0] * (n + 1)
if n >= 1:
    d[1] = 0
if n >= 2:
    d[2] = 1

for i in range(3, n + 1):
    d[i] = (i - 1) * (d[i - 1] + d[i - 2]) % MOD

print(d[n])