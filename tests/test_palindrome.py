import pytest

from gengo import is_palindrome, find_longest_palindrome_substring, find_minimum_cuts


@pytest.mark.parametrize('input_string, result', [
	('abcdcba', True),
	('goooooogle', False), 
	('gengo', False), 
	('', True), 
	('WilaBaliw', True)
])
def test_is_palindrome(input_string, result):
	assert is_palindrome(input_string) == result

@pytest.mark.parametrize('input_string, result', [
	('abaxyzzyxf', 'Xyzzyx'),
	('gooooooogleeee', 'Gooooooog'),
	('abbbadbca', 'Abbba'),
	('', ''),
	('WilaBaliw', 'Wilabaliw')
])
def test_find_longest_palindrome_substring(input_string, result):
	assert find_longest_palindrome_substring(input_string) == result

@pytest.mark.parametrize('input_string, result', [
	('noonabbad', 2),
	('noongooogabbad', 3),
	('goooog', 0),
	('', 0),
	('alphAbet', 7)
])
def test_find_minimum_cuts(input_string, result):
	assert find_minimum_cuts(input_string) == result
