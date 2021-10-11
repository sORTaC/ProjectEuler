#extract digits and store it in a list
def extract_digits(n):
	#create list that will store the extracted digits
	digits = []
	#perform extraction
	while n != 0:
		digits.append(n % 10)
		n = n // 10
	digits.reverse()
	return digits

#compare digits to check if it's a pallindrome 
def comp_digits(m):
	#get size to iterate through
	num_of_digits = len(m)
	#single digit numbers are not pallindromes
	if num_of_digits == 1:
		return False
	size = num_of_digits // 2
	for i in range(size):
		if m[i] != m[num_of_digits - 1 - i]:
			return False
	return True

def check_pallindrome(num):
	var1 = extract_digits(num)
	var2 = comp_digits(var1)
	return var2

def solve_problem(lower_limit, upper_limit):
	max = 0
	for i in range(upper_limit, lower_limit, -1):
		for j in range(upper_limit, lower_limit, -1):
			num = i*j
			result = check_pallindrome(num)
			if result == True:
				if num > max:
					max = num
	print("The answer is :", max)

solve_problem(100, 999)