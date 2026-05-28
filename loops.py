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
          
