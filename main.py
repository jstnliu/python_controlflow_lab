# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
vowels = 'aeiou'
if letter in vowels:
  print(f'the letter {letter} is a vowel')
else:
  print(f'the letter {letter} is a consonant')
  

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = ''
while True:
  phrase = input('Please enter a word or phrase: ')
  if phrase == 'quit':
    break
  print(f'What you entered is {len(phrase)} characters long')
  

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

age = int(input("Input a dog's age: "))
if age < 3: 
  print(f"The dog's age is {age * 10} years")
else:
  print(f"The dog's age is {(age - 2) * 7 + 20}")


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a = input("Enter a side: ")
b = input("Enter a second side: ")
c = input("Enter a third side: ")
if a == b and a == c:
    print(f"A triangle with sides of {a, b, c} is an equilateral triangle - all three sides are equal in length")
elif a != b and a != c and c!= b:
    print(f"A triangle with sides of {a, b, c} is a scalene triangle - all three sides are not equal")
else:
    print(f"A triangle with sides of {a, b, c} is an isosceles triangle - exactly two sides are equal")


# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

n = 0
x = 0
y = 1
for n in range(50):
    print(f"term {n} / number {x}")
    n += 1
    z = x
    x = y
    y = z + x


# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
month = input("Enter the month of the year (Jan - Dec): ")
shortened_month = month[0:3].lower()
date = int(input("Enter the date of the month: "))
if date > 0 or date < 32:
   print("Get your dates right, yea?")
else: 
    if shortened_month in month_list[0:3] or shortened_month == month_list[11]:
        if shortened_month == month_list[0] and (date >= 1 or date <= 31):
            print(f"{month} {date} is in Winter")
        elif shortened_month == month_list[1] and (date >= 1 or date <= 29):
            print(f"{month} {date} is in Winter")
        else:
            if shortened_month == month_list[2] and (date >= 1 or date <= 19):
                print(f"{month} {date} is in Winter")
            elif shortened_month == month_list[11] and (date >= 1 or date < 21):
                print(f"{month} {date} is in Winter")
            else:
                next 
    if shortened_month in month_list[2:6]:
        if shortened_month == month_list[3] and (date >= 1 or date <= 30):
            print(f"{month} {date} is in Spring")
        elif shortened_month == month_list[4] and (date > 0 or date <= 31):
            print(f"{month} {date} is in Spring")
        else:
            if shortened_month == month_list[2] and (date >= 20 or date <= 31):
                print(f"{month} {date} is in Spring")
            elif shortened_month == month_list[5] and (date >= 1 or date <= 20):
                print(f"{month} {date} is in Spring")
            else:
                next 
    if shortened_month in month_list[5:9]:
        if shortened_month == month_list[6] and (date >= 1 or date <= 31):
            print(f"{month} {date} is in Summer")
        elif shortened_month == month_list[7] and (date > 0 or date <= 31):
            print(f"{month} {date} is in Summer")
        else:
            if shortened_month == month_list[5] and (date >= 21 or date <= 30):
                print(f"{month} {date} is in Summer")
            elif shortened_month == month_list[8] and (date >= 1 or date <= 21):
                print(f"{month} {date} is in Summer")
            else:
                next 
    if shortened_month in month_list[8:-1]:
        if shortened_month == month_list[9] and (date >= 1 or date <= 31):
            print(f"{month} {date} is in Fall")
        elif shortened_month == month_list[10] and (date >= 1 or date <= 30):
            print(f"{month} {date} is in Fall")
        else:
            if shortened_month == month_list[8] and (date >= 22 or date <= 30):
                print(f"{month} {date} is in Fall")
            if shortened_month == month_list[11] and (date >= 1 or date < 20):
                print(f"{month} {date} is in Fall")
    


