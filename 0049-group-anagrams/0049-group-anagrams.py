from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            # Sort the characters of each string to use as a hash map key
            key = "".join(sorted(s))
            groups[key].append(s)
            
        return list(groups.values())