## Print

print("")
print(" PRINT EXERCISE")
print("")

print("I am now learning AI")
print('This is printed using single quotes')
print("""
Now
this
is printed
using
triple
quotes
""")
print("Here I am using backslash t \t for space")

print("I am now using backslash n for \n new line")

print("")
print("")

## Variable

print("")
print(" VARIABLE EXERCISE")
print("")

var = "Hello World"
print(var)
print(type(var))

case1 = "camelCase"
case2 = "PascalCase"
case3 = "snake_case"

print("This is",case1,"\nThis is", case2,"\nThis is ",case3)


print("")
print("")

## Operators

print("")
print(" OPERATORS EXERCISE")
print("")


    ## Arithmatic Operators


print("")
print("\t ARITHMATIC OPERATORS")
print("")

a = 1
b = 2
c = (a+b)
print("1 + 2 is",c)

d = 5
e = d-c
print("5 - 3 is",e)

f = 6
g = f*e
print("6 times 2 is",g)

h = 7
i = h/g
print("7 divided by 12 is",i)

j = 8
k = j % i
print("8 modulus 0.583 is",k)

l = 2
m = 4
n = m**l
print("4 power 2 is",n)


print("")
print("")


     ## Assignment Operators

print("")
print("\t ASSIGNMENT OPERATORS")
print("")

ass1 = "first value"
a = ass1
print("Using assingment operator (=) I assigned my", ass1)

ass2 = 5
b = ass2
print("Using asignment I can also assign an Integer such as", ass2)

incAss = 3
incAss += 1
print("Using increment operator (+=) I get the value" , incAss)

decAss = 4
decAss -= 1
print("Using decrement Operator (-=) I get",decAss , "when I initially give the number 4")

print("")
print("")


    ## Comparision Operators

print("")
print("\t COMPARISION OPERATORS")
print("")

comOp0 = 2
comOp = 3
comOp1 = 3
comOp3 = (comOp == comOp1)
print("Is 3 equal to 3",comOp3)

comOp2 = 4
comOp4 = (comOp1 == comOp2)
print ("Is 3 equal to 4",comOp4)

eg = "example"
eg1 = "example"
eg2 = "Example"

eg3 = (eg == eg1)
eg4 =  (eg == eg2)

print("Comparing 'example' and 'example' using == we get",eg3)
print("Comparing 'example' and 'Example' using == we get",eg4)

comOp5 = (comOp != comOp1)
print("Is 3 not equal to 3",comOp5)

comOp6 = (comOp != comOp2)
print("Is 3 equal to 4",comOp6)

comOp7 = (comOp < comOp1)
print("Is 3 less than 3",comOp7)

comOp8 = (comOp < comOp2)
print("Is 3 less than 4",comOp8)

comOp9 = (comOp > comOp1)
print("Is 3 greater than 3",comOp9)

comOp10 = (comOp > comOp2)
print("Is 3 greater than 4",comOp10)

comOp11 = (comOp2 > comOp)
print("Is 4 greater than 3",comOp11)

comOp12 = (comOp <= comOp1)
print("Is 3 less than equal to 3",comOp12)

comOp13 = (comOp <= comOp2)
print("Is 3 less than equal to 4",comOp13)

comOp14 = (comOp <= comOp0)
print("Is 3 less than equal to 2",comOp14)

comOp15 = (comOp >= comOp1)
print("Is 3 greater than equal to 3",comOp15)

comOp16 = (comOp >= comOp2)
print("Is 3 greater than equal to 4",comOp16)

comOp17 = (comOp >= comOp0)
print("Is 3 greater than equal to 2",comOp17)



print("")
print("")



    ## Logical Operators

print("")
print("\t LOGICAL OPERATORS")
print("")

## AND

print("false and false is",comOp16 and comOp16)
print("false and true is",comOp16 and comOp17)
print("true and false is",comOp15 and comOp16)
print("true and true is",comOp15 and comOp17)

print("")


## OR

print("false and false is",comOp16 or comOp16)
print("false and true is",comOp16 or comOp17)
print("true and false is",comOp15 or comOp16)
print("true and true is",comOp15 or comOp17)

print("")


## NOT

print("not of false is",not comOp16)
print("not of true is",not comOp17)

print("")
print("")


    ## Identity Operator

print("")
print("\t IDENTITY OPERATORS")
print("")

## is

idOp = 2
idOp1 = 2
idOp2 = 3


idOp3 = (idOp is idOp1)
print("2 is 2",idOp3)

idOp5 = (idOp is idOp2)
print("2 is 3",idOp5)


print("")


## is not

idOp4 = (idOp is not idOp1)
print("2 is not 2",idOp4)



idOp6 = (idOp is not idOp2)
print("2 is not 3",idOp6)

print("")
print("")



    ## Membership Operator

print("")
print("\t MEMBERSHIP OPERATORS")
print("")


## in

memOp = "Today is a Good Day"

print("Is 'Today' in 'Today is a Good Day'" , "Today" in memOp)
print("Is 'today' in 'Today is a Good Day'" , "today" in memOp)

print("")


## not in

print("Is 'Good' not in 'Today is a Good Day'" , "Good" not in memOp)
print("Is 'Bad' not in 'Today is a Good Day'" , "Bad" not in memOp)

print("")
print("")



# len


print("")
print(" LEN EXERCISE")
print("")

lenVar = "Learning len() function in python"
var01 = len(lenVar)
print("length of the sentence 'Learning len() function in python' is: ",var01)

lenVar1 = "Now comapring length of string using len"
var02 = len(lenVar1)
print("length of the sentence 'Now comapring length of string using len' is: ",var02)

lenVar2 = "How comapring length of string using pen"
var03 = len(lenVar2)
print("length of the sentence 'How comapring length of string using pen' is: ",var03)


var04 = var01 == var02
print("Comparing first and second sentence's length using var ",var04)

var05 = var02 == var03
print("Comparing second and third sentence's length using var ",var05)

print("")
print("")

# concatination

print("")
print(" CONCATINATION EXERCISE")
print("")


concat = "I am an "
concat1 = "AI Engineer"
concat2 = 34

concat3 = concat + concat1
print(concat3)

concat4 = concat + str(concat2) ## typecasting; forcing 34 to be considered a string instead of an integer
print(concat4)


