'''
Given a square 2D list (matrix), 
return the absolute difference between 
the sums of its two diagonals.

if we assume that the length of each list is the same
we can traverse through each list
and then get the index of each element +1 in the next list by using pointers
the pointer for the left will start at 0
the pointer on the right will start at the end.
we will increase
we need to know the length of atleast 1 array to start at end


'''

def diagonal_difference(matrix):
    end = len(matrix[0]) - 1
    
    start = 0
    first_values = 0
    second_values = 0
    for arr in matrix:
        first_values += arr[start]
        second_values += arr[end]
        start += 1
        end -= 1
        
    return (first_values - second_values)





# Example:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(diagonal_difference(matrix))
# output = |(1+5+9) - (3+5+7)| = 0
