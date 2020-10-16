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

	:ouput: <boolean>
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

	:output: <str>
	"""
	# first is get the input string and iterate through it from top to bottom
	# that way we check the longer strings first
	# if we find the longest palindrome we terminate the loop 

	# time space complexity for this algorithm is O(n)*2 for the two loops run down
	# through string and another O(n) for the checking if substring generated from loop
	# is a palindrome: O(n)*3

	len_string = len(input_string)
	palindrome_str = ''
	for l in range(len_string, 0, -1):
		find_flag = False
		for i in range(len_string-l+1):
			substring = input_string[i:i+l]
			if not is_palindrome(substring): continue
			palindrome_str = input_string[i:i+l]
			find_flag = True
		if find_flag:
			break
	return palindrome_str

"""
level3:
- Now write a function that returns the minimum number of cuts needed to perform on the string such that each remaining substring is a palindrome. 

Sample Input:
	string = "noonabbad"
Sample Output:
	2 // noon | abba | d
"""
def find_minimum_cuts(input_string):
	"""detertmines mimnimum cuts to perform in a string such that each remaining substring is a palindrome
	:input_string: <str>

	:output: <int>
	"""
	# time space complexity
	# `_min_palindrome_partition` is being called recursively n times before reaching its base case so its O(n), 
	# but since it is being called twice we can say that it's O(2n)
	# now, since inside the function we are looping the recursively call, we can say that it's O(n2) * O(2n)
	# lastly, we are calling the is_palindrome function which is linear O(n)
	# therefore,
	# O(2n) * O(n)**2 * O(n) => O(2n)3	

	# we try to calculate the palindrome status of every position `start_index` to position `end_index`.
	# represented by n*m matrix 2D
	# wherein we represent each value for each nxm item and determine the minimum cut per iteration
	# eg.
	#	  n o o 
	#	n 0	1 1  	
	#	o 0 1 1 
	#	o 0 1 1

	output = _min_palindrome_partition(input_string, 0, len(input_string) - 1)
	return output

def _min_palindrome_partition(input_string, start_index, end_index):
	"""
	:input_string: <str>
	:start_index: <int>
	:end_index: <int>

	:output: <int>
	"""

	# we check if the start_index is greater or equal than the current length of string -1
	# if yes we return 0 because we know that we reached the end of the loop
	# also we check if string is palindrome that way we know that it's either single character
	# or already a palindrome string which requires no minimum cut
	if (start_index >= end_index) or is_palindrome(input_string[start_index:end_index + 1]):
		return 0

	answer = float('inf')
	for s in range(start_index, end_index):
		count = (1 + _min_palindrome_partition(input_string, start_index, s) + 
			_min_palindrome_partition(input_string, s + 1, end_index)
		)
		answer = min(answer, count)
	return answer
