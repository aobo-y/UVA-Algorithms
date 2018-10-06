# bottom up dynamic programming for Question 3 in PS4
def combination(n, m):
  memoize = [[0 for a in range(0, m + 1)] for b in range(0, n + 1)]

  for i in range(1, n + 1):
    for j in range(max(0, m - n + i), min(i, m) + 1):
      if j == 0 or i == j:
        memoize[i][j] = 1
      else:
        memoize[i][j] = memoize[i - 1][j] + memoize[i - 1][j - 1]

  return memoize[n][m]

print(combination(10, 5))
