# regular expressions are used to parse a specifc text/pattern/number from the paragraph.

# ^ indicates the beginning and $ indicates the end of the line.
# . indicates any character, its a wild card.
# grep command used to find the characters in a text, -i used to find both upper and lowercase characters

import re

result=re.search(r"aza", "plaza") # r= raw string
print(result)

result=re.search(r"aza", "bazaar")
print(result)

result=re.search(r"aza", "maze")
print(result)


result=re.search(r"^x", "xenon")
print(result)

result=re.search(r"p.ng", "penguin")
print(result)


def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

result=re.search(r"[Pp]ython", "Python")
print(result)


result=re.search(r"[a-z]way", "This is the of the highway")
print(result)

result=re.search(r"[a-z]way", "Wat a way to go") # None cause space before way and we expect an alphabet
print(result)

result=re.search("cloud[a-zA-Z0-9]", "cloudy")
print(result)

result=re.search("cloud[a-zA-Z0-9]", "cloud9") # Upper and lowercase letters and numbers
print(result)

result=re.search(r"[^a-zA-Z]", "tis is a sentence with spaces.") # matches the first white space
print(result)

result=re.search(r"[^a-zA-Z ]", "tis is a sentence wit spaces.") # mathes the fullstop,since there is space at the end
print(result)

result=re.search(r"cat|dog", "cats.") # either or
print(result)

result=re.search(r"cat|dog", "i like dogs and cats.") # either or
print(result)

result=re.findall(r"cat|dog", "i like dogs and cats.") # either or
print(result)

result=re.search(r"p.*n", "pygmalion") # to match all the characters in between
print(result)

result=re.search(r"p.*n", "python programming") 
print(result)

result=re.search(r"p[a-z]*n", "python programming") 
print(result)

result=re.search(r"o+l+", "goldfish") 
print(result)

result=re.search(r"o+l+", "moolly") 
print(result)

result=re.search(r"o+l+", "scdvosdvslsdavocsl") # Here there are different characters in between o and l
print(result)

result=re.search(r"p?each", "To each their own") # ? means optional
print(result)

result=re.search(r"p?each", "there are peaches") 
print(result)

result=re.search(r".com", "welcome") 
print(result)

result=re.search(r"\.com", "welcome") # \ is used as an escape character to include . in the search
print(result)

result=re.search(r"\.com", "domain.com") 
print(result)

result=re.search(r"\w*", "domain.com") # \w matches letters numbers and underscores
print(result)

result=re.search(r"\w*", "domain_com") # \w matches letters, numbers and underscores
print(result)

# \d matching digits
# \s matching white space characters ie space, tab, new line
# \b for word boundaries


result=re.search(r"A.*a", "Argentina") # country starting with upper case A and end with lowercase a.
print(result)

result=re.search(r"A.*a", "Azerbaijan") 
print(result)

result=re.search(r"^A.*a$", "Azerbaijan") 
print(result)

result=re.search(r"^A.*a$", "Australia") 
print(result)

pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"  # pattern for a python variable name. variable name starts with letters or _
print(re.search(pattern,"_tis_is_a_vais" ))
print(re.search(pattern,"tis is_a_vais" ))
print(re.search(pattern,"tis_is_a_vais1" ))
print(re.search(pattern,"2tis_is_a_vais1" ))