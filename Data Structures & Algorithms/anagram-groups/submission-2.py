class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = {}

        for word in strs:
            temp_word = "".join(sorted(word))
            if temp_word in anag_dict:
                anag_dict[temp_word].append(word)
            else:
                anag_dict[temp_word] = [word]
            
        return [v for v in anag_dict.values()]