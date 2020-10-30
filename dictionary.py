##########################################################################################
# Dictionary in python
# d = {'a':1,'b':2}

# for i in d:
# 	print(f'{i} : {d[i]}')

# for index, value in enumerate(d):
# 	print("index : {}, key : {}, value : {}".format(index, value, d[value]))


##########################################################################################
# Function to illustrate the use of break in loop
# print("function to illustrate the use of break in loop")
# def breakDemo(arr):
# 	for i in arr:
# 		if i == 2:
# 			break
# 		print(i)
# 	print()

# arr = [10,3,1,2,30]
# breakDemo(arr)


##########################################################################################
# Function to illustrate the use of continue in loop
# print("Function to illustrate the use of continue in loop")
# def continueDemo(arr):
# 	for i in arr:
# 		if i == 2:
# 			continue
# 		print(i)
# 	print()

# continueDemo(arr)


##########################################################################################
# map, filter and lambda function 
# def square(x):
# 	return x**2

# li = [1,2,3,4,5]
# map_result = map(square, range(5))
# print(map_result)
# print(list(map_result))


##########################################################################################
# lambda function
# a = lambda x,y : x*y
# print(a)
# print(a(6,9))

# def lambdaFunc(x):
# 	return lambda a : a*x

# func = lambdaFunc(4)
# print(func(6))


##########################################################################################
# filter function
# filterResult = filter(lambda x : x%2 == 0, li)
# print(filterResult)
# print(list(filterResult))


##########################################################################################
# tuple
# tup = 'kanay', 'karan'
# print(tup)

# tup = ('kanay', 'karan')
# print(tup)

# tuple3 = ('python',)*3
# print(tuple3)


##########################################################################################
# sets
# normal_set = set([1,2,'s',1])
# print(normal_set)
# normal_set.add((7,8))
# print(normal_set)

# s1 = {1,2,3}
# s2 = {2,5,7}

# print(s1|s2)
# print(s1&s2)
# print(s1-s2)
# print(s1^s2)


##########################################################################################
# frozensets
# frozen_set = frozenset(['a','b','c'])
# print(frozen_set)


##########################################################################################
# taking multiple inputs at a time using split() method and list comprehension
# x, y = input("enter two value : ").split()
# print('first value = {}, second value = {}'.format(x,y))

# x,y,z = input("enter three values : ").split()
# print('first : {} second : {} third : {}'.format(x,y,z))

# x = list(map(int, input("enter multiple values : ").split()))
# print(x)

##########################################################################################
# multiple inputs using list comprehensions
x, y = [int(x) for x in input("enter two values : ").split()]
print(x,y)

x,y,z = [int(x) for x in input("enter three values : ").split()]
print(x,y,z)

x = [int(x) for x in input("enter multiple values : ").split()]
print(x)