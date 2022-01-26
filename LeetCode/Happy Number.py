# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

def solve(n, visited):
    if n == 1:
        return True
    if n in visited:
        return False
    visited[n] = 1
    n = str(n)
    l = list(n)
    l = list(map(int, l))
    temp = 0
    for i in l:
        temp += (i ** 2)
    return solve(temp, visited)