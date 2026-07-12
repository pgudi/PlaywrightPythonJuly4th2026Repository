# Capitalizze()
str="python programming language"
print(str.capitalize())  # Python programming language

# title
str1="python programming language"
print(str1.title()) # Python Programming Language

# Replace
str2="It is a new Palace"
print(str2.replace("is","was")) # It was a new Palace

# find (it provides position of string or character from left to right)
str3="It is a book, It is on the table"
print(str3.find("is"))  # 3

# rfind (it provides position of string or character from right to left)
str4="It is a book, It is on the table"
print(str4.rfind("is")) # 17

# index (it provides position of string or character from left to right)
str5="It is a book, It is on the table"
print(str5.index("is")) # 3

# rfind (it provides position of string or character from right to left)
str6="It is a book, It is on the table"
print(str6.rindex("is")) # 17

# Lower ( it converts the given string into lowercase)
str7="WELCOME" 
print(str7.lower()) # welcome

# upper ( it converts the given string into uppercase)
str8="programming"
print(str8.upper())

# isalnum  (verifues the string is alpha numeric)
str9="welcome123"
str10="welcome 123"
print(str9.isalnum())
print(str10.isalnum())

# isalpha (verifues the string is alphabetic)
str11="Morning"
print(str11.isalpha())

# istitle ( verifues each word first character is in uppercase)
str12="Welcome To Scripting"
print(str12.istitle())

# islower (verifies the given string is in lowercase)
str13="java"
print(str13.islower())  # True

# isupper (verifies the given string is in uppercase)
str14="MYSQL"
print(str14.isupper()) # True

#isspace (it verifies the given string is space)
str15=" "
print(str15.isspace() ) # True

#isDEcimal (it verifies the given string is decimal)
str16="1234"
str17="12.75"
print(str16.isdecimal())  # True it is 0-9
print(str17.isdecimal())  # False

#isDigit (it verifies the given string is digit)
str18="1234"
str19="12.75"
print(str18.isdigit())  # True it is 0-9
print(str19.isdigit())  # False

#isnumeric (it verifies the given string is digit)
str20="1234"
str21="12.75"
print(str20.isnumeric())  # True it is 0-9
print(str21.isnumeric())  # False

# startsWith , IT verifies whether teh given string available at start position
str22="Lotus is national flower"
print(str22.startswith("Lotus")) # True
print(str22.endswith("flower")) # True

# split [ based on delimer it splits]
str23="Bangalore and Mysore"
print(str23.split(" "))
str24="Apple#Mango#Ornage"
print(str24.split("#"))


#lstrip It removes blank spaces at left hand side of the given String
str25="   java   "
print("Before lStrip the length of String ",len(str25))
print("After lStrip the length of String ",len(str25.lstrip()))

#rstrip It removes blank spaces at right hand side of the given String
str26="   java   "
print("Before rStrip the length of String ",len(str26))
print("After rStrip the length of String ",len(str26.rstrip()))

#strip It removes blank spaces at both sides of the given String
str26="   java   "
print("Before Strip the length of String ",len(str26))
print("After Strip the length of String ",len(str26.strip()))

# Verify whether sTring are equal
str27="Welcome"
str28="welcome"
print(str27==str28)