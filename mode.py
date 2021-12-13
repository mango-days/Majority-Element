# Majority Element

# Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

import numpy as np

data = [ 3 , 1 , 3 , 3 , 2 , 3 , 1 , 3 , 3 , 2 ]
unique = np.array ( data )
mode_count = 0
mode = -1

for index in range ( 0 , len ( unique ) ) :
    temp = data.count ( unique [ index ] )
    if temp > mode_count :
        mode_count = temp
        mode = unique [ index ]
    
print ( mode )