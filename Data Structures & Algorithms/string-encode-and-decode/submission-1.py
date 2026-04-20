class Solution:
    def encode(self, strs:list[str]) -> str:
        res = ""
        
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res
    
    def decode(self, s:str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
                
            length_str = s[i:j]
            length = int(length_str)
            
            start_of_word = j + 1
            end_of_word = j + 1 + length
            
            word = s[start_of_word : end_of_word]
            
            res.append(word)
            
            i = end_of_word
        
        return res