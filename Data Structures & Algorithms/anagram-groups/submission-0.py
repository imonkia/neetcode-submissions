class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anag_dict = {}

        for _, word in enumerate(strs):
            temp_word = "".join(sorted(word))
            if temp_word in anag_dict:
                anag_dict[temp_word].append(word)
            else:
                anag_dict[temp_word] = [word]
            
        return [v for v in anag_dict.values()]