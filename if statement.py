#IF STATEMENT
#GENERATION NAME

age = int(input("Enter your age:\n"))

#if statements
if age>=12 and age<=27:
    print("you are Gen z")

elif age>=28 and age<=43:
    print("you are a millennial")

elif age>=44 and age<=59:
    print("you are Gen x")

elif age<-60 and age>=78:
    print("you are a Boomer")

else:
    print("sorry! you are out of bounds...")