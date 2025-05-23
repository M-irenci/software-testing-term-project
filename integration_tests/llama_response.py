from typing import List
from collections import Counter

class PalindromeChecker:
    def concatenate(self, strings: List[str]) -> str:
        return ''.join(strings)

    def is_palindrome(self, text: str) -> bool:
        return text == text[::-1]

    def reverse_delete(self, s: str, c: str) -> tuple:
        s = ''.join([char for char in s if char not in c])
        return s, self.is_palindrome(s)

    def rearrange_palindrome(self, s: str) -> str:
        counter = Counter(s)
        odd_count = sum(count % 2 for count in counter.values())
        if odd_count > 1:
            return None, False
        mid_char = [char for char, count in counter.items() if count % 2 != 0][0] if odd_count else ''
        s = ''.join([char for char in s if char != mid_char])
        s, is_palindrome = self.reverse_delete(s, mid_char)
        if not is_palindrome:
            front, back = s[:len(s)//2], s[len(s)//2:]
            while not self.is_palindrome(self.concatenate([front, mid_char, back])):
                front, back = front[1:], back[1:]
            s = self.concatenate([front, mid_char, back])
        return s, self.is_palindrome(s)
class TestRearrangePalindrome:
    def __init__(self):
        self.checker = PalindromeChecker()

    def test_rearrange_palindrome(self):
        result_str, result_bool = self.checker.rearrange_palindrome("aabbc")
        assert result_bool
        assert result_str == result_str[::-1]

    def test_rearrange_palindrome_none(self):
        result_str, result_bool = self.checker.rearrange_palindrome("aacb")
        assert not result_bool
        assert result_str is None

    def test_rearrange_palindrome_single(self):
        result_str, result_bool = self.checker.rearrange_palindrome("a")
        assert result_bool
        assert result_str == result_str[::-1]

    def test_rearrange_palindrome_already(self):
        result_str, result_bool = self.checker.rearrange_palindrome("abcba")
        assert result_bool
        assert result_str == result_str[::-1]

    def test_rearrange_palindrome_long(self):
        result_str, result_bool = self.checker.rearrange_palindrome("aabbbbcccc")
        assert result_bool
        assert result_str == result_str[::-1]

# Run tests manually
tester = TestRearrangePalindrome()
tester.test_rearrange_palindrome()
tester.test_rearrange_palindrome_none()
tester.test_rearrange_palindrome_single()
tester.test_rearrange_palindrome_already()
tester.test_rearrange_palindrome_long()
