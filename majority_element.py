import numpy as np

array = [ 3 , 0 , 0 , 2 , 0 , 4 ]
unique_array = np.array ( array )
unique_array = np.unique ( unique_array )

n = len ( array )
majority_condition = int ( n / 2 )

ans = -999

for index in range ( 0 , len ( unique_array ) ) :
    if array .count ( unique_array [ index ] ) >= majority_condition :
        ans = unique_array [ index ]
        
if ans != -999 : print ( " majority element =" , ans )
else : print ( " no majority element " )
