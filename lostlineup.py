n = int(input())
q = [0] * n
q[0] = 1
s = list(map(int, input().split()))
for i in range(n-1):
    q[s[i]+1] = i+2
print(' '.join(map(str, q)))
