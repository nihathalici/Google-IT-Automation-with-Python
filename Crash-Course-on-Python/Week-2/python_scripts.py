##############################
# Expressions and Variables  #
##############################


"""
In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. 
The friends decide to split the bill evenly between them, after adding 15% tip for the service. 
Calculate the tip, the total amount to pay, and each friend's share, then output a message saying 
"Each person needs to pay: " followed by the resulting number.
"""
bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2
print("Each person needs to pay: " + str(share))

"""
This code is supposed to take two numbers, divide one by another so that the result is equal to 1, 
and display the result on the screen. Unfortunately, there is an error in the code. 
Find the error and fix it, so that the output is correct.
"""
numerator = 10
denominator = 10
result = numerator / denominator
print(result)


# Combine the variables to display the sentence "How do you like Python so far?" 
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6 + " " + word7)

"""
This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. 
Find the error in the code and fix it, so that the output is correct.
"""
print( str("2 + 2 = ") + str(2+2) )


##############
# Functions  #
##############

"""
This function converts miles to kilometers (km).

Complete the function to return the result of the conversion
Call the function to convert the trip distance from miles to kilometers
Fill in the blank to print the result of the conversion
Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result
"""
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2.0 * my_trip_km) )


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


"""
Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. 
This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work.
"""
def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))


#################
# Conditionals  #
#################

'''
Complete the script by filling in the missing parts. The function receives a name, 
then returns a greeting based on whether or not that name is Taylor.
'''
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

# What’s the output of this code if number equals 10?
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)
  
"""
If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. 
A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, 
which calculates the total number of bytes needed to store a file of a given size?
"""
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = int(filesize / block_size)
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return full_blocks * block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


"""
Complete the function by filling in the missing parts. The color_translator function receives the name of a color, 
then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), 
so it returns "unknown" for all other colors.
"""
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


"""
Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". 
For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". 
Fill in this function so that it returns the proper grade.
"""
def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

"""
The longest_word function is used to compare 3 words. It should return the word with the most number of characters 
(and the first in the list when they have the same length). Fill in the blank to make this happen.
""""
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

"""
The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). 
Complete the body of the function so that it returns the right number.
Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.
"""
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
	if denominator == 0:
		return 0
	return (numerator % denominator) / denominator

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
