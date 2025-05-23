from typing import List
from collections import Counter

class PalindromeRearranger:

    def concatenate(self, strings: List[str]) -> str:
        """ Concatenate list of strings into a single string
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
        """
        return "".join(strings)

    def is_palindrome(self, text: str):
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

    def reverse_delete(self, s, c):
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
        result = "".join([char for char in s if char not in c])
        return (result, self.is_palindrome(result))

    def rearrange_palindrome(self, s: str) -> str:
        """
        Rearranges a string to form a palindrome.  If the function has more than one odd character count, it will return None.
        The function will return the result palindrome, None if there isn't an output.
        """
        counts = Counter(s)
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]

        if len(odd_chars) > 1:
            return None, False

        middle = odd_chars[0] if odd_chars else ""
        remaining_chars = [char for char in s if char not in odd_chars]
        # Remove characters that make it not a palindrome
        remove_chars = ""
        temp_counts = Counter(remaining_chars)
        for char in temp_counts:
            if temp_counts[char] % 2 != 0:
                remove_chars += char

        deleted_string, _ = self.reverse_delete(s, remove_chars)

        counts = Counter(deleted_string)
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]

        if len(odd_chars) > 1:
            return None, False

        middle = odd_chars[0] if odd_chars else ""
        left = ""
        for char, count in counts.items():
            if char != middle:
                left += char * (count // 2)

        # Concatenate to form palindrome
        palindrome = self.concatenate([left, middle, left[::-1]])
        return palindrome, self.is_palindrome(palindrome)

import unittest

class TestPalindromeRearrangerIntegration(unittest.TestCase):

    def setUp(self):
        self.rearranger = PalindromeRearranger()

    def test_rearrange_simple_palindrome(self):
        result_str, result_bool = self.rearranger.rearrange_palindrome("aabb")
        self.assertTrue(result_bool)
        self.assertEqual(result_str, result_str[::-1])

    def test_rearrange_palindrome_with_middle_char(self):
        result_str, result_bool = self.rearranger.rearrange_palindrome("aabba")
        self.assertTrue(result_bool)
        self.assertEqual(result_str, result_str[::-1])

    def test_rearrange_impossible_palindrome(self):
        result_str, result_bool = self.rearranger.rearrange_palindrome("aabbbc")
        self.assertFalse(result_bool)
        self.assertIsNone(result_str)

    def test_rearrange_already_palindrome(self):
        result_str, result_bool = self.rearranger.rearrange_palindrome("madam")
        self.assertTrue(result_bool)
        self.assertEqual(result_str, "madam")

    def test_rearrange_complex_string(self):
        result_str, result_bool = self.rearranger.rearrange_palindrome(
            "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"
        )
        self.assertTrue(result_bool)
        self.assertEqual(sorted(result_str), sorted("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"))
        self.assertEqual(result_str, result_str[::-1])

try: 
    unittest.main()
except SystemExit:
    pass