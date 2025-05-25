from typing import List
from collections import Counter

class PalindromeOperations:
    def concatenate(self, strings: List[str]) -> str:
        """ Concatenate list of strings into a single string
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
        """
        return ''.join(strings)

    def is_palindrome(self, text: str) -> bool:
        """
        Checks if given string is a palindrome
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
       Consider case sensitivity
        """
        return text == text[::-1]

    def reverse_delete(self, s: str, c: str) -> tuple[str, bool]:
        """Task
        We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
        then check if the result string is palindrome.
        A string is called palindrome if it reads the same backward as forward.
        You should return a tuple containing the result string and True/False for the check.
        Example
        For s = "abcde", c = "ae", the result should be ('bcd',False)
        For s = "abcdef", c = "b"  the result should be ('acdef',False)
        For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
        """
        result_string = ''.join([char for char in s if char not in c])
        is_pal = self.is_palindrome(result_string)
        return (result_string, is_pal)

    def rearrange_palindrome(self, s: str) -> tuple[str, bool]:
        """
        Rearranges the characters of a string to form a palindrome if possible.

        Returns:
            A tuple containing:
            - The rearranged palindrome string, or None if not possible.
            - A boolean indicating whether a palindrome was successfully formed.
        """
        char_counts = Counter(s)
        odd_counts = [char for char, count in char_counts.items() if count % 2 != 0]

        if len(odd_counts) > 1:
            return (None, False)

        middle_char = odd_counts[0] if odd_counts else ''
        half_palindrome = ''.join(sorted([char * (count // 2) for char, count in char_counts.items()]))
        palindrome = self.concatenate([half_palindrome, middle_char, half_palindrome[::-1]])

        if (self.is_palindrome(palindrome)):
            return (palindrome, True)
        else:
            return (None, False)


import unittest

class TestRearrangePalindromeIntegration(unittest.TestCase):

    def setUp(self):
        self.operations = PalindromeOperations()

    def test_rearrange_palindrome_success(self):
        """Test a case where a palindrome can be formed."""
        result, success = self.operations.rearrange_palindrome("aabbccdde")
        self.assertTrue(success)
        self.assertEqual(len("aabbccdde"), len(result))
        self.assertTrue(self.operations.is_palindrome(result))

    def test_rearrange_palindrome_failure(self):
        """Test a case where a palindrome cannot be formed."""
        result, success = self.operations.rearrange_palindrome("aabbbcd")
        self.assertFalse(success)
        self.assertIsNone(result)

    def test_rearrange_palindrome_with_existing_palindrome(self):
         """Test a case where a palindrome is already formed."""
         result, success = self.operations.rearrange_palindrome("aba")
         self.assertTrue(success)
         self.assertEqual("aba",result)

    def test_rearrange_palindrome_empty_string(self):
        """Test an empty string input."""
        result, success = self.operations.rearrange_palindrome("")
        self.assertTrue(success)
        self.assertEqual("", result)

    def test_rearrange_palindrome_single_character(self):
        """Test a single character string input."""
        result, success = self.operations.rearrange_palindrome("a")
        self.assertTrue(success)
        self.assertEqual("a", result)

if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit:
        pass