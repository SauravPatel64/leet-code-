class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq = {}
        
        for word in strs:
            key = "".join(sorted(word))

            if key in freq:
                freq[key].append(word)

            else:
                freq[key] = [word]

        return list(freq.values())