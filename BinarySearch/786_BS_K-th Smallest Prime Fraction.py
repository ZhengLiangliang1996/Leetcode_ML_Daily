class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        n = len(A)
        l = 0.0
        r = 1.0
        while l < r:
            m = (l + r) / 2
            max_f = 0.0
            total = 0      
            j = 1
            for i in range(n - 1):
                while j < n and A[i] > m * A[j]: j += 1
                if j == n: break
                total += n - j
                f = A[i] / A[j]
                if f > max_f:
                    p, q, max_f = i, j, f
            if total == K:
                return [A[p], A[q]]
            elif total > K:
                r = m
            else:
                l = m
        return []