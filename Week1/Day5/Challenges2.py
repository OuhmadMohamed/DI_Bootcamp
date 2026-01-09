#***********************  Challenges #2  **********************
#__________________________________________________________________



#------------------------------------------------
#  Exercise 1
#---------------------------------------------
rows = 3
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2*i - 1))
'''
  *
 ***
*****
'''
#_________________________
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)
'''
    *
   **
  ***
 ****
*****
'''
#____________________________
rows = 5

# Top triangle
for i in range(1, rows + 1):
    print('*' * i)

# Bottom inverted triangle
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * i)

'''
*
**
***
****
*****
*****
 ****
  ***
   **
    *
'''

###########################################################################
##########################################################################
#---------------------------------------------------------------
#  Exercise 2
#----------------------------------------------------------------

my_list = [2, 24, 12, 354, 233]  # Initial list

for i in range(len(my_list) - 1):  # Outer loop, i goes from 0 to 3
    minimum = i  # Assume the minimum element is at index i
    for j in range(i + 1, len(my_list)):  # Inner loop, check all elements after i
        if(my_list[j] < my_list[minimum]):  # If a smaller element is found
            minimum = j  # Update the index of the minimum
            if(minimum != i):  # If the minimum is not at position i
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]  # Swap them

print(my_list)  # Print the sorted list
