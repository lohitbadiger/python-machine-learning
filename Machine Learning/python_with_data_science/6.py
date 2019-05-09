import numpy as np 
first_array=np.array([1,2,3,4,5])

print(first_array)
print('__________________________')

array_with_zero=np.zeros((3,3))
print(array_with_zero)
print('__________________________')

array_with_ones=np.ones((3,3))
print(array_with_ones)

print('__________________________')

# randomly set number
array_with_empty=np.empty((3,4))
print(array_with_empty)

print('__________________________')
np_arrage=np.arange(12)
print(np_arrage)
print('__________________________')
# give new shape to the above array
np_arrage.reshape(3,4)
print(np_arrage)

print('__________________________')

# Return evenly spaced numbers over a specified interval.


np_linespace=np.linspace(1,10,5)
print(np_linespace)

print('__________________________')
oneD_array=np.arange(15)
print(oneD_array)
print('__________________________')
# Rearaging above
Two_D=oneD_array.reshape(3,5)
print(Two_D)

# Three Dimensional Array

Three_D=np.arange(27).reshape(3,3,3)
print(Three_D)
print(Three_D.ndim)

# Class and attribute of ndarray
# ndarray.ndim =>it used get dimension of array

np_city=np.array(['hubli','Goa', 'hampi','Banglore']) 
print(np_city.ndim)
# its 2d array below
np_city_with_2=np.array([['hubli','Goa', 'hampi','Banglore'],['ahubli','Gaoa', 'haampi','Banglaore'],['ahubli','Gaoa', 'haampi','Banglaore']]) 
print(np_city_with_2.ndim)

# ndarray.shape

np_city=np.array(['hubli','Goa', 'hampi','Banglore']) 
print(np_city.shape)

np_city_with_2=np.array([['hubli','Goa', 'hampi','Banglore'],['ahubli','Gaoa', 'haampi','Banglaore'],['ahubli','Gaoa', 'haampi','Banglaore']]) 
print(np_city_with_2.shape)