from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, "r")
    lines = file.readlines()
    file.close()

    currC = "NULL"
    currA = "NULL"
    counter = 0    
    ident(transform)
    length = len(lines)

    while (counter < length):
        currC = lines[counter]
        currC = currC.strip()
        #print currC

        if currC == "line": #DONE
            counter += 1
            currA = lines[counter]
            currA = currA.strip()
            args = currA.split()
            add_edge( points, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]) )
            #print args
        elif currC == "ident": #DONE
            ident(transform)
        elif currC == "scale":
            counter += 1            
            currA = lines[counter]
            currA = currA.strip()
            args = currA.split()
            matrix = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(matrix, transform)
        elif currC == "move": #DONE
            counter += 1
            currA = lines[counter]
            currA = currA.strip()
            args = currA.split()
            matrix = make_translate(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(matrix, transform)
        elif currC == "rotate":
            counter += 1
            currA = lines[counter]
            currA = currA.strip()
            args = currA.split()
            axis = args[0]
            theta = args[1]
            if (axis == "x"):
                matrix = make_rotX(theta)
                matrix_mult(matrix, transform)
            elif (axis == "y"):
                matrix = make_rotY(theta)
                matrix_mult(matrix, transform)
            elif (axis == "z"):
                matrix = make_rotZ(theta)
                matrix_mult(matrix, transform)
            else:
                print "borked"
        elif currC == "apply": #DONE
            #print_matrix(transform)
            matrix_mult(transform, points)
        elif currC == "display": #DONE
            draw_lines(points, screen, color)
            display(screen)
            clear_screen(screen)
            #ident(transform)
        elif currC == "save": #DONE
            counter += 1
            currA = lines[counter]
            currA = currA.strip()
            draw_lines(points, screen, color)
            ppm_name = 'pic.ppm'
            save_ppm( screen, ppm_name )
        elif currC == "quit": #DONE
            return
        else: #DONE
            pass

        counter += 1
