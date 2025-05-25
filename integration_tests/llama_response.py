class PalindromeOperations:
    def concatenate(self, strings: list[str]) -> str:
        return ''.join(strings)

    def is_palindrome(self, text: str) -> bool:
        return text == text[::-1]

    def reverse_delete(self, s: str, c: str) -> tuple[str, bool]:
        s = ''.join(char for char in s if char not in c)
        return s, self.is_palindrome(s)

    def rearrange_palindrome(self, s: str) -> tuple[str | None, bool]:
        from collections import Counter
        counter = Counter(s)
        odd_count_chars = [char for char in counter if counter[char] % 2 != 0]
        if len(odd_count_chars) > 1:
            return None, False
        half = ''.join(char * (counter[char] // 2) for char in counter)
        palindrome = self.concatenate([half, *odd_count_chars, half[::-1]]) if odd_count_chars else self.concatenate([half, half[::-1]])
        return palindrome, self.is_palindrome(palindrome)


class TestPalindromeOperations:
    def test_rearrange_palindrome(self):
        assert PalindromeOperations().rearrange_palindrome("aab") == ("aba", True)

    def test_rearrange_palindrome_with_multiple_odd_chars(self):
        assert PalindromeOperations().rearrange_palindrome("aabccc") == (None, False)

    def test_rearrange_palindrome_with_no_odd_chars(self):
        assert PalindromeOperations().rearrange_palindrome("aabb") == ("abba", True)

    def test_rearrange_palindrome_with_empty_string(self):
        assert PalindromeOperations().rearrange_palindrome("") == ("", True)

    def test_rearrange_palindrome_with_single_char(self):
        assert PalindromeOperations().rearrange_palindrome("a") == ("a", True)

if __name__ == "__main__":
    test = TestPalindromeOperations()
    test.test_rearrange_palindrome()
    test.test_rearrange_palindrome_with_multiple_odd_chars()
    test.test_rearrange_palindrome_with_no_odd_chars()
    test.test_rearrange_palindrome_with_empty_string()
    test.test_rearrange_palindrome_with_single_char()
    print("All tests passed successfully!")