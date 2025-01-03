class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for s in strs:
            for char in s:
                encoded += chr(ord(char) + 1)  
            encoded += "| "  
        return encoded

    def decode(self, s: str) -> list[str]:
        words = s.split("| ")[:-1]  
        decoded = []
        for word in words:
            decoded_word = ""
            for char in word:
                decoded_word += chr(ord(char) - 1) 
            decoded.append(decoded_word)
        return decoded
