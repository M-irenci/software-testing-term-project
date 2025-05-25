from gemini_response import PalindromeOperations as gemini_class
from llama_response import PalindromeOperations as llama_class
from typing import Counter

class TestRearrangePalindrome():
    def init(self):
        self.models = [gemini_class(), llama_class()]

    def test_even_length_perfect_palindrome(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("aabb")
            assert is_valid
            assert Counter(result) == Counter("aabb")  # Should use all characters
            assert result == result[::-1]  # Should be a perfect palindrome


    def test_odd_length_valid_palindrome(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("aaaab")
            assert is_valid
            assert Counter(result) == Counter("aaaab")
            assert result == result[::-1]

    def test_impossible_palindrome(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("abc")
            assert not is_valid
            assert result is None

    def test_single_character(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("z")
            assert is_valid
            assert Counter(result) == Counter("z")
            assert result == "z"

    def test_empty_string(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("")
            assert is_valid
            assert Counter(result) == Counter("")
            assert result == result[::-1]


tester = TestRearrangePalindrome()
tester.init()
tester.test_empty_string()
tester.test_single_character()
tester.test_impossible_palindrome()
tester.test_odd_length_valid_palindrome()
tester.test_even_length_perfect_palindrome()
print("All tests passed successfully!")