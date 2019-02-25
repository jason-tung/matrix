from display import *
from draw import *
from matrix import *
import random


diagnostic = True
if diagnostic:
    print("------TESTING MATRIX FX------")
    m1 = new_matrix(2, 6)
    print("----TESTING MATRIX CREATION----")
    print("this is a new 2x6 matrix")
    #print(m1)
    print_matrix(m1)
    for row in range(len(m1)):
        for col in range(len(m1[row])):
            m1[row][col] = col + row
    m1_copy = new_matrix(2, 6)
    for row in range(len(m1_copy)):
        for col in range(len(m1_copy[row])):
            m1_copy[row][col] = col + row
    print("----TESTING MATRIX IDENTITY----")
    print("this is m1_copy")
    print_matrix(m1_copy)
    ident(m1_copy)
    print("this is m1_copy after using ident on it")
    print_matrix(m1_copy)
    m2 = new_matrix(6, 2)
    for row in range(len(m2)):
        for col in range(len(m2[row])):
            m2[row][col] = row + col * (row + 2)
    print("----TESTING MATRIX MULT----")
    print("this is m2")
    print_matrix(m2)
    print("this is m1")
    print_matrix(m2)
    print("this is test_copy (the identity of m1) multipied by m1")
    print_matrix(matrix_mult(m1_copy, m1))
    print("this is m2 multiplied by m1")
    print_matrix(matrix_mult(m2, m1))
    print("this is m1 after multiplying (to verify it changed)")
    print_matrix(m1)
    print("----TESTING ADD_EDGES----")
    m3 = new_matrix()
    for row in range(len(m3)):
        for col in range(len(m3[row])):
            m3[row][col] = random.randint(0,10)
    print("this is m3")
    print_matrix(m3)
    print("this is m3 after adding the following edge: 5,6,7 to 8,9,10")
    add_edge(m3, 5,6,7,8,9,10);
    print_matrix(m3)






screen = new_screen()
color = [ 0, 255, 0 ]
matrix_trunk = new_matrix(4,0)
matrix_leaves = new_matrix(4,0)

def draw_tree(level, x, y, length, angle):
    x1 = int(x + length * math.sin(angle * (math.pi / 180)))
    y1 = int(y + length * math.cos(angle * (math.pi / 180)))
    if level < 5:
        add_edge(matrix_trunk, x, y,0 , x1, y1, 0)
    else:
        add_edge(matrix_leaves, x, y, 0, x1, y1, 0)
    #print(color)
    if level < 10:
        draw_tree(level + 1, x1, y1, length - length * 0.2, angle + 20)
        draw_tree(level + 1, x1, y1, length - length * 0.2, angle - 20)


draw_tree(0, 250, 0, 90, 0)

draw_lines( matrix_trunk, screen, [139,69,19] )
draw_lines( matrix_leaves, screen, [0,255,0] )
display(screen)
