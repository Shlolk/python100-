#memeory repersentation of python of (binary , octal ,hexadecimal)

#converting int to float
x=10
print(float(x))
y=12.5
print(int(y))

#binary 
a=bin(10)
print(a)

#octal 
a=oct(20)
print(a)

#hexadecimal
a=hex(4)
print(a)

#how to take user input 
a=hex(int(input("enter the number:")))
print(a)

#str 

a=str(10)
b=str(20)
print(a+b)

#str 
s='welcome adiba to the section b'
print(s[3:6])

s='shlok is a good student'
print(s*2)

#bytes datatype 
b=[10,20,30,40,255]
x=bytes(b)
for i in x:
    print(i) 

#string manupaltion 
my_string = "i am learing python with most poopular teacher"

print(my_string.upper())#converts the string to uppercase
print(my_string.lower())

name= "  adiba "
print(name.strip())#removes the white spaces from the string
print(name.lstrip())#removes the white spaces from the left side of the string
print(name.rstrip())#removes the white spaces from the right side of the string
print(name.replace("a","A"))#replaces the character a with A in the string
print(name.split())#splits the string into a list of words

my_list= ['hello','adiba','welcome']
print("-".join(my_list))#joins the list of words into a string with - as a separator 


name= 'shlok kumar '
print(name.startswith("s"))#returns True if the string starts with s
print(name.endswith("k"))#returns True if the string ends with k
print(name.count('o'))#returns the number of times o appears in the string
print(name.find('shlok'))#returns the index of the first occurrence of shlok in the string
print(name.capitalize())#capitalizes the first letter of the string
print(name.title())#capitalizes the first letter of each word in the string

print(name.isupper())#returns True if all the characters in the string are uppercase
print(name.islower())#returns True if all the characters in the string are lowercase

