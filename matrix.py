import math

def make_translate( x, y, z ):
    matrix = new_matrix()
    ident(matrix)
    matrix[3][0] = x
    matrix[3][1] = y
    matrix[3][2] = z
    return matrix

def make_scale( x, y, z ):
    matrix = new_matrix()
    ident(matrix)
    matrix[0][0] = x
    matrix[1][1] = y
    matrix[2][2] = y

    return matrix
'''
    halfX = 250
    halfY = 250
    halfZ = 250

    translation_m = make_translate(x, y, z)
    translation_m2 = make_translate(-x, -y, -z)

    final_matrix = new_matrix()
    ident(final_matrix)
    
    matrix_mult(translation_m2, final_matrix)
    matrix_mult(matrix, final_matrix)
    matrix_mult(translation_m, final_matrix)

    return final_matrix
'''



def make_rotX( theta ):    
    matrix = new_matrix()
    ident(matrix)

    rad = math.radians( float(theta) )
    
    matrix[1][1] = math.cos(rad)
    matrix[2][1] = -math.sin(rad)
    matrix[1][2] = math.sin(rad)
    matrix[2][2] = math.cos(rad)

    return matrix

def make_rotY( theta ):
    matrix = new_matrix()
    ident(matrix)

    rad = math.radians( float(theta) )
    
    matrix[0][0] = math.cos(rad)
    matrix[2][0] = math.sin(rad)
    matrix[0][2] = -math.sin(rad)
    matrix[2][2] = math.cos(rad)

    return matrix

def make_rotZ( theta ):
    matrix = new_matrix()
    ident(matrix)

    rad = math.radians( float(theta) )
    
    matrix[0][0] = math.cos(rad)
    matrix[1][0] = -math.sin(rad)
    matrix[0][1] = math.sin(rad)
    matrix[1][1] = math.cos(rad)

    return matrix

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
