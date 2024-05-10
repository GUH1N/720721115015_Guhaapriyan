def climbStairs(n: int):
    if n <= 3: return n

    prev1 = 3
    prev2 = 2
    cur = 0

    for _ in range(3, n):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur
    return cur

print(climbStairs(2))
print(climbStairs(3))