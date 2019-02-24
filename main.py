from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

for x in range(20):
add_edge(matrix, x**2, int(x

draw_lines( matrix, screen, color )
display(screen)
