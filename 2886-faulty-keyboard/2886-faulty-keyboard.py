class Solution:
    def finalString(self, s: str) -> str:
        word =""
        for c in s:
            if c == 'i':
                word = word[::-1]
            else:
                word=word+c
        return word