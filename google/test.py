# function lessons

def month_days(month, days_in_month):
    print(month + " has" + str(days_in_month) + " days.")

month_days("June", 30)
month_days("July", 31)



def lucky_number(name):
    number = len(name) * 9
    user_1 = "Hello " + name + ". Your lucky number is " + str(number)
    return user_1   
print(lucky_number("Kay"))
print(lucky_number("Cameron"))



def is_positive(number):
  if number>0:
    return True

is_positive(5)



def number_group(number):
  if number>0:
    return "Positive"
  elif number<0:
    return "Negative"
  else:
    return 0

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative



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



def exam_grade(score):
	if score>95:
		grade = "Top Score"
	elif score>=60:
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

