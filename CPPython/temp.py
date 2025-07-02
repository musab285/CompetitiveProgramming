def lcs(s1, s2, m, n ):
    if m==0 or n==0:
        return 0
    if s1[m-1] == s2[n-1]:
        return  1+lcs(s1,s2, m-1, n-1)
    else:
        return max(lcs(s1, s2, m-1, n), lcs(s1, s2, m, n-1))
def lcsmem(s1, s2, m, n, memo):
    if m==0 or n==0:
        return 0
    if memo[m][n] != -1:
        return memo[m][n]

    if s1[m-1] == s2[n-1]:
        memo[m][n] = 1+lcs(s1,s2, m-1, n-1, memo)
    else:
        memo[m][n] = max(lcs(s1, s2, m-1, n), lcs(s1, s2, m, n-1))
        return memo[m][n]
def lisIdx(arr, idx):
    if idx == 0:
        return 1
    mx = 1
    for prev in range(idx):
        if arr[prev] < arr[idx]:
            mx = max(mx, lisEndingAtIdx(arr, prev) + 1)
    return mx
def lis(arr):
    n = len(arr)
    res = 1
    for idx in range(1, n):
        res = max(res, lisIdx(arr, idx))
    return res
def prefsum(arr):
    n = len(arr)
    sum = [0] * n
    sum[0] = arr[0]
    for i in range(1, n):
        sum[i] = sum[i - 1] + arr[i]
    return sum

if __name__ == "__main__":
    t = int(input())
    for x in range(t):
        n = int(input())
        a = set(map(int, input().split()))
        print(len(a))