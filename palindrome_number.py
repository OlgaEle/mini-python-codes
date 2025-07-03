class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not (-2**31 <= x <= (2**31) - 1):
            raise ValueError('x must be between -2^31 and 2^31-1')
        list_original = [i for i in str(x)]
        list_reverse = list_original[::-1]
        result = list_original == list_reverse
        return result
