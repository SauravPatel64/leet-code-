class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        sorted_nums = sorted(
            freq,
            key=lambda x: freq[x],
            reverse=True
        )

        return sorted_nums[:k]

        