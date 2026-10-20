from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = list(Counter(tasks).values())
        max_f = max(freqs)
        max_count = freqs.count(max_f)
        
        ans = (max_f - 1) * (n + 1) + max_count
        return max(ans, len(tasks))
        