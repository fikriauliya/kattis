n = int(input())
l = list(map(int, input().split()))
l.sort()
suml = sum(l)
maxl = max(l)
print(max(suml, 2*maxl))