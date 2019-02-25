"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    print_str = ""
    for rows in matrix:
        print_str += "|"
        for x in rows:
            str_num = str(x)
            num_spaces = 3 - len(str_num)
            print_str += num_spaces * "0" + str_num
            print_str += " "
        print_str = print_str[:-1]
        print_str += "|\n"
    print(print_str)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    matrix[:] = new_matrix(len(matrix), len(matrix))
    for x in range(len(matrix)):
        matrix[x][x] = 1
    return matrix

def dot(v1, v2):
    x = 0
    for x in v1:
        x+=v1 * v2
    return x

def getVector(m1,loc,direction):
    vector = []
    if direction == "down":
        vector = [k[loc] for k in m1]
    else:
        vector = m1[loc]
    return vector

def dotProd(v1,v2):
    tot = 0
    for x in range(len(v1)):
        #print(v1,v2,x)
        tot += v1[x] * v2[x]
    return tot


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    ret_matrix = new_matrix(len(m1),len(m2[0]))
    #print_matrix(ret_matrix)
    for horizontal_indices in range(len(m1)):
        horizontal_vector = getVector(m1, horizontal_indices, "right")
        #print(m2[0])
        for vertical_indices in range(len(m2[0])):
            vertical_vector = getVector(m2, vertical_indices, "down")
            #print([horizontal_indices,vertical_indices])
            ret_matrix[horizontal_indices][vertical_indices] = dotProd(horizontal_vector, vertical_vector)
    m2[:] = ret_matrix
    return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( rows ):
        m.append( [] )
        for r in range( cols ):
            m[c].append( 0 )
    return m


