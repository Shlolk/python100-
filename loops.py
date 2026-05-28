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
