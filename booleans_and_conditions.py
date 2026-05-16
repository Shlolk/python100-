#Comparison operators are operators that let you compare two or more values, and return a boolean value.
#The most common comparison operators are:
# == (equal to)    if two values are equal, it returns True, otherwise it returns False.
# != (not equal to) checks if two values are not equal, it returns True if they are not equal, and False if they are equal.
# < (less than)    if the left value is less than the right value, it returns True, otherwise it returns False.
# > (greater than) if the left value is greater than the right value, it returns True, otherwise it returns False.
# <= (less than or equal to) if the left value is less than or equal to the right value, it returns True, otherwise it returns False.
# >= (greater than or equal to) if the left value is greater than or equal to the right value, it returns True, otherwise it returns False.

#example 
print(5==5)# true
print(5!=5)# false
print(5<10)# true
print(5>10)# false
print(5<=10)# true
print(5>=10)# false

#In Python, the most basic conditional is the if statement. Here's the basic syntax:
#if condition:
#    # code to execute if the condition is true
#You can also use else and elif (short for "else if") to create more complex conditions:
#if condition1:
#    # code to execute if condition1 is true
#elif condition2:
#    # code to execute if condition2 is true
#else:
#    # code to execute if none of the conditions are true
if 5 > 3:
    pass
 # this code will execute if the condition is true
#if statement contains a pass statement. When a pass statement is executed, nothing happens. This is a special keyword that can be used as a placeholder for future code and it is useful when empty
#  code blocks are not allowed.
#In this example, the condition 5 > 3
#  is true, so the code block under the if statement will execute. However, since it contains only a pass statement, nothing will happen when the code is run.

age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') 