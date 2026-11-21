class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded=encoded+s+"~"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ""
        for char in s:
            if char == "~":
                decoded.append(word)
                word = ""
            else:
                 word = word+char
        return decoded
