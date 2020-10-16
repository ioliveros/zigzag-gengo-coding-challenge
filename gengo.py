"""
--------------------------------------------------
Gengo Coding Exam
--------------------------------------------------
@author: Ian Oliveros
@date: October 16, 2020
"""


"""
level1:
- Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome. 

Sample Input:
	string = "abcdcba" 
Sample Output:
	 true // it's written the same forward and backward
"""
def is_palindrome(input_string):
	"""function will determine wether the given `input_string` is a palindrome or not
	:input_string: <str>
	"""
	# we will lower both string to ignore case
	#
	# time space complexity for this algorithim is O(n) since we are reversing 
	# a dynamic collection of string with `n` length, 
	# which is treated as a list comprehension in python
	return True if input_string[::-1].lower() == input_string.lower() else False

"""
level2:
- Now write a function that, given a string, returns its longest palindromic substring. 
You can assume that there will only be one longest palindromic substring. 

Sample Input:
	string = "abaxyzzyxf" 
Sample Output:
	"Xyzzyx"
"""

def find_longest_palindrome_substring(input_string):
	"""detertmines wether a string has a substring palindrome then outputs the longest palindrome string
	:input_string: <str>
	"""
	len_string = len(input_string)
	palindrome_str = ''
	for l in range(len_string, 0, -1):
		find_flag = False
		for i in range(len_string-l+1):
			word = input_string[i:i+l]
			if not is_palindrome(word): continue
			palindrome_str = input_string[i:i+l]
			find_flag = True
		if find_flag:
			break
	return palindrome_str.title()
