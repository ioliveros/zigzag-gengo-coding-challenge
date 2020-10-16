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
