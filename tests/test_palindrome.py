import pytest

from gengo import is_palindrome


@pytest.mark.parametrize('input_string, result', [
	('abcdcba', True),
	('goooooogle', False), 
	('gengo', False), 
	('', True), 
	('WilaBaliw', True)
])
def test_is_palindrome(input_string, result):
	assert is_palindrome(input_string) == result
