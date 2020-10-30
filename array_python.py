# The array in python is handled by a module named array.
# array(data type, value list)

import array

arr = array.array('i',[1,2,3,2,4,1,3,4])
print(arr)

for i in range(len(arr)):
	print(arr[i], end=' ')
print("\n")

##################################################################################################
# append function
# print("append function")
# arr.append(80)
# for i in range(len(arr)):
# 	print(arr[i], end=' ')
# print('\n')

##################################################################################################
# insert function
# print("Insert function")
# arr.insert(2,10)
# for i in range(len(arr)):
# 	print(arr[i], end=' ')
# print('\n')

##################################################################################################
# pop function
# print("Popped element is : ", end=' ')
# print(arr.pop())
# for i in range(len(arr)):
# 	print(arr[i], end=' ')
# print("\n")

##################################################################################################
# remove function
# print("remove function")
# arr.remove(1)
# for i in range(len(arr)):
# 	print(arr[i], end=' ')
# print('\n')

##################################################################################################
# index function
# print("index function")
# print(arr)
# print('\n')
# print("the index of first occurrence of 4 is : ")

# print(arr.index(4))
# print('\n')

##################################################################################################
# reverse function
# print("original array : ", end=' ')
# for i in range(len(arr)):
# 	print(arr[i], end=' ')
# print('\n')

# print("array after applying reverse function : ", end=' ')
# arr.reverse()

# for i in range(len(arr)):
# 	print(arr[i], end=' ')
# print('\n')

##################################################################################################
# typecode
# print("typecode of array arr is : ", end=' ')
# print(arr.typecode)
# print('\n')

##################################################################################################
# itemsize
# print("itemsize of array arr is : ", end=' ')
# print(arr.itemsize)
# print('\n')

##################################################################################################
# buffer_info() function
# print("buffer_info of array arr is : ", end=' ')
# print(arr.buffer_info())
# print('\n')

##################################################################################################
# count() function
# print("the number of 2 in array arr is : ", end=' ')
# print(arr.count(2))
# print('\n')

##################################################################################################
# extend(arr) function
# arr1 = array.array('i',[8,2,0,22,32,89])
# print("arr1 : ", arr1)
# print("extendng array arr with arr1 : ", end=' ')
# arr.extend(arr1)
# print(arr)
# print('\n')

##################################################################################################
# fromlist(list)
# li = [11,22,33,44]
# print("list li : ", li)
# arr2 = array.array('i',[1,2,3,4,5])
# print("arr2 : ", arr2)
# arr2.fromlist(li)
# print(arr2)
# print('\n')

##################################################################################################
# tolist
# arr2 = array.array('i',[1,2,3,4,5])
# print("arr2 : ", arr2)

# li = arr2.tolist()
# print(li)
# print('\n')

##################################################################################################
# program for array rotation

def array_rotation(arr, num):
	temp = []
	for i in range(0,len(arr)-num):
		temp.append(arr[num+i])

	for j in range(num):
		temp.append(arr[j])

	return temp
arr = [1,2,3,4,5,6,7]
num = 3
print("initial array : ", arr)
print("rotated array : ", array_rotation(arr,num))
print('\n')

##################################################################################################
# program for array rotation

def leftRotateByOne(arr,n):
	temp = arr[0]

	for i in range(n-1):
		arr[i] = arr[i+1]
	
	arr[n-1] = temp


def leftRotate(arr, d, n):
	for i in range(d):
		leftRotateByOne(arr,n)
	return arr

print("left rotating the array by 10 : ", end=' ')
print(leftRotate(arr,10,len(arr)))
print('\n')

##################################################################################################
# Reversal algorithm for array rotation

def reverseArray(arr,start,end):
	while start < end:
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp
		start += 1
		end -= 1

def rotateArray(arr,d):
	if d == 0:
		return arr

	n = len(arr)
	d = d%n

	reverseArray(arr,0,d-1)
	reverseArray(arr,d,n-1)
	reverseArray(arr,0,n-1)

	return arr

arr = [1,2,3,4,5]
print("array after rotation : ",rotateArray(arr,2))
print('\n')

##################################################################################################
# cyclically rotate the array by one clockwise

def clyclicRotate(arr,d,n):
	for i in range(d):
		clockwiseRotateByOne(arr,n)

	return arr

def clockwiseRotateByOne(arr,n):
	temp = arr[n-1]

	for i in range(n-1,0,-1):
		arr[i] = arr[i-1]
	
	arr[0] = temp

arr = [1,2,3,4,5,6,7]
d = 1
print("cyclic rotation by 2 : ",clyclicRotate(arr,d,len(arr)))
print('\n')

##################################################################################################
# To reverse an array of string
arr = [1,2,3]

def reverseArray(arr, start, end):
	while start < end:
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp
		start += 1
		end -= 1
	return arr

print("arr : ", arr)
start = 0
end = len(arr)-1
print("reverse array : ",reverseArray(arr,start,end))
print('\n')

##################################################################################################
# recursive program to reverse an array

def reverseList(arr,start,end):
	if start >= end:
		return

	temp = arr[start]
	arr[start] = arr[end]
	arr[end] = temp
	
	reverseList(arr, start+1, end-1)

arr = [1,2,3,4]
start = 0
end = len(arr)-1
print('original list : ', arr)
reverseList(arr,start,end)
print("reverse list is : ", arr)