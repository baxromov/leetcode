def palindrome(N):
    for i in range(1, N + 1):
        print(int('1' * i)**2)


N = int(input())
res = []
for i in range(N):
     res.append(i)
     print(res + res[-2::-1])
