import string

def det_palindrome_tf(pal_str):
	# strip out punctuation characters
	no_punc = pal_str.translate(str.maketrans('', '', string.punctuation))
	# now remove spaces
	no_spaces = no_punc.replace(' ', '')
	# now change case to uniform
	is_it_pal = no_spaces.upper()
	# print(f"Input value: {pal_str}, no_punc: {no_punc}, no_spaces: {no_spaces}, is_it_pal: {is_it_pal}")
	num_chars = len(is_it_pal)
	loop_end = num_chars / 2
	str_indx = 1
	left_start = -1
	right_start = 0
	is_it_p = 1
	while (str_indx <= loop_end) & (is_it_p == 1):
		if is_it_pal[str_indx + left_start] == is_it_pal[right_start - str_indx]:
			str_indx += 1
		else:
			is_it_p = 0
			break
	
	if is_it_p == 1:
		print(f"{pal_str} is a palendrome!")
	else:
		print(f"{pal_str} is NOT a palendrome (sigh)")

# commands used in solution video for reference
if __name__ == '__main__':
	det_palindrome_tf('Hannah')
	det_palindrome_tf('Racecar')
	det_palindrome_tf('Hello World')
	det_palindrome_tf("Go hang a salami - I'm a lasagna hog")
	det_palindrome_tf("I would not like a noogie, thank you very much!")