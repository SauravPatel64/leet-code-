class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1

        for ch in t:
            if ch not in freq:
                return False

            freq[ch] -= 1

        for value in freq.values():
            if value != 0:
                return False

        return True
        