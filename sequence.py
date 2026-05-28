#list 
list1=[10,20,30,40,50]#list is a collection of items which are ordered and changeable. It allows duplicate members.
print(list1)        
#avtanges of list are it is mutable and it can contain different datatypes and it is ordered and it allows duplicate members.
#disadvantages of list are it is not memory efficient and it is not faster than other datatypes like tuple and set.

#list of opertions having on the list 
list1=[10,20,30,40,50]
print(list1[0])#accessing the first element of the list.....
print(list1[1])#accessing the second element of the list....
print(list1[2])#accessing the third element of the list.....
print(list1[3])#accessing the fourth element of the list....
print(list1[4])#accessing the fifth element of the list.....

list1=[10,20,30,40,50]     
for i in list1:
    print(i) #here we are using the for loop to access the elements of the list and print them one by one


tuple1=(10,20,30,40,50) #tuple is a collection of items which are ordered and unchangeable. It allows duplicate members
print(tuple1)
#advantages of tuple are it is memory efficient and it is faster than list and it is ordered and it allows duplicate members.
#disadvantages of tuple are it is not mutable and it can not contain different datatypes.

set1={10,20,30,40,50} #set is a collection of items which are unordered and unchangeable. It does not allow duplicate members.
print(set1)

#nested list : list inside list 
developer= ['shlok',21,['c++','rust','pyhton']]
print(developer[2])#here the ouput will be ['c++','rust','python']
# in the nested list you can see that index start with 0 so shlok is zero intex , 21 is 1 index ,and the another list in side list is carry the indx no 3 
# if you want to acces the one element from the nested list so we can do this 
developer = ['shlok', 21, ['Python', 'Rust', 'C++']]
developer[2][1] # 'rust'
#Unpacking values from a list is a technique used to assign values
#from a list to new variables. Here is an example of unpacking a
#developer list into new variables called name, age an
developer = ['shlok', 21,'rust developer']
name,age,job= developer 
print(name)#shlok
print(age)#21
print(job)#rust developer 
#if you want to print the one element and print rest as it is you can use * ashstrack symbol for that ....
developer = ['shlok', 21, 'Rust Developer']
name, *rest = developer
print(name) # 'shlok'
print(rest) # [21, 'Rust Developer']
#how to append the list with the help of append() method
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6] 
#If you want to add one list at the end of another, you can also use the append() method like this:
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]
#extend,medthod - we extent the list with multiple value and append we extent the list with the  single method 
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10] so this is the output 
"""
To insert an element at a specific index in a list, you can use 
the insert() method. This method accepts two arguments: the index where you
wish to insert the new item and the item you want to insert."""

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print(numbers) # [1, 2, 2.5, 3, 4, 5]
#Another way to create a tuple is by using the tuple() constructor like this:
developer = 'Shlok'
tuple(developer) # ('S','h','l','o','k')
programing_language=('python','c++','rust')
'rust' in programing_language #True
'java' in programing_language #False


