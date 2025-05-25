from gemini_response import PalindromeRearranger 
from llama_response import PalindromeChecker


class TestRearrangePalindrome():
    def init(self):
        self.models = [PalindromeRearranger(), PalindromeChecker()]

    def test_even_length_perfect_palindrome(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("aabb")
            assert is_valid
            assert result == "abba"

    def test_odd_length_valid_palindrome(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("aaaab")
            assert is_valid
            assert result == "aabaa"

    def test_impossible_palindrome(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("abc")
            assert not is_valid
            assert result is None

    def test_single_character(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("z")
            assert is_valid
            assert result == "z"

    def test_empty_string(self):
        for checker in self.models:
            result, is_valid = checker.rearrange_palindrome("")
            assert is_valid
            assert result == ""


tester = TestRearrangePalindrome()
tester.init()
tester.test_empty_string()
tester.test_single_character()
tester.test_impossible_palindrome()
tester.test_odd_length_valid_palindrome()
tester.test_even_length_perfect_palindrome()
print("All tests passed successfully!")