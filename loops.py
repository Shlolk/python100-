programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language) 
  """
 here  Without that indentation,
you would get an IndentationError:

"""
#here we are using to print ot iterate the charaters 
char='code ' 
for i in code:
    print(i)
 """   
you can also nest for loops in Python. 
Here is an example of using a nested for loop:
"""
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)
"""
Another type of loop you can use in Python is the while loop.
This type of loop will repeat a block of code until the condition is False.
Here is an example of using a while loop for a guessing game:
"""
sceret_num=3
gusse=0 
  while gusse!=sceret_num:
      gusse=int(intput("gusses the sceret number :"))
      if gusse != sceret_num:
          print("worng gusses")

print("you got it..... ")
"""
if you wanted to keep track of the index for each element? Well,
one option is to create an index variable and increment it by 1 
    for each iteration of the loop, like this:
"""
languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1         
#this method is good but we can do this with more better way with the help of enumerate()
# The enumerate() function keeps track of the index for an iterable and returns an enumerate object.
languages = ['Spanish', 'English', 'Russian', 'Chinese']
list(enumerate(languages))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]
#zip() function that make a pair of two different lists of same position of elements
code_busters=['shlok','adiba' ,'krishna','sachin','yessia']
postion=['fullstack','frontend','frontend','database','frontend']
print(zip(code_busters,postion))
#anothe example zip with for loop 
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')

#here is example of using loop or if condition to check whather the number is even or not
even_numbers = []
for num in range(21):  #here the no will be 0 to 20.
    if num % 2 == 0:   #this condition check wather  the number is even or not 
        even_numbers.append(num) #if the conditon is true even_numbers list

print(even_numbers) #here we print the list 
'''problem of the first code is 
1.create the empty list 
2.crate loop 
3.crete the condition for checking wheather no is  event or not 
4.if true print the list     
'''
#their is another way to do that and this is very consise..
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers) #this method is called list Comprehensions...
#another example 
number=[1,2,3,4,5]
result=[(num,'even') if num%2==0 else (num,'odd') for num in numbers]
print(result) #output:[(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]


