class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        # keep only alphanumeric characters
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        # reverse the cleaned string
        rev = cleaned[::-1]

        # compare
        return cleaned == rev
