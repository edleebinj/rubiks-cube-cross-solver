import rubik.cube as rb
from rubik.solve import Solver
from itertools import product
def main():
    solved_cube_yb="UUUUUUUUULLLFFFRRRBBBLLLFFFRRRBBBLLLFFFRRRBBBDDDDDDDDD"
    c2 = rb.Cube("DLURRDFFUBBLDDRBRBLDLRBFRUULFBDDUFBRBBRFUDFLUDLUULFLFR")
    c = rb.Cube(solved_cube_yb)#x is right(r) #y is facing up(u) #z is front(f)
    ctwomove = rb.Cube('FUFFUFFUFLLLDFDRRRUBULLLDFDRRRUBULLLDFDRRRUBUBDBBDBBDB')
    #print(c.get_piece(1,1,1).pos[1])
    edge_moves_from_solved_position(c.get_piece(0,-1,0))
    #print(is_down_cross_edge(c.get_piece(0,-1,-1)))   
    dic2 = {}
    create_dic(dic2,2)
    dic3 = {}
    create_dic(dic3,3)
    dic4 = {}
    create_dic(dic4,4)
    dic8 = {}
    create_dic(dic8,8)

    #print(product(*dic2.values()))
    #print(c2.is_solved())
    bruteforce(ctwomove,dic4,4)
    '''
    alg = Solver(c2)
    alg.solve()
    print(' '.join(alg.moves))
    '''
    #for conf in generate_conf(dic):
    #print(generate_conf(dic))

#def test_all_moves(depth,**d):#maxdepth 8
#    if type(depth) != int or depth > 8 or depth < 1:
#        print('depth must be integar and between 1 and 8')
#    else:


def move(cube,notation):
    if notation == 'U':
        cube.U()
    elif notation == 'Ui':
        cube.Ui()
    elif notation == 'U2':
        cube.U()
        cube.U()
    elif notation == 'D':
        cube.D()
    elif notation == 'Di':
        cube.Di()
    elif notation == 'D2':
        cube.D()
        cube.D()
    elif notation == 'R':
        cube.R()
    elif notation == 'Ri':
        cube.Ri()
    elif notation == 'R2':
        cube.R()
        cube.R()
    elif notation == 'L':
        cube.L()
    elif notation == 'Li':
        cube.Li()
    elif notation == 'L2':
        cube.L()
        cube.L()
    elif notation == 'F':
        cube.F()
    elif notation == 'Fi':
        cube.Fi()
    elif notation == 'F2':
        cube.F()
        cube.F()
    elif notation == 'B':
        cube.B()
    elif notation == 'Bi':
        cube.Bi()
    elif notation == 'B2':
        cube.B()
        cube.B()

def edge_moves_from_solved_position(cube_piece):#only works for down cross
    pass
def is_down_cross_edge(cube_piece):
    try:
        if 'D' in cube_piece.colors and cube_piece.pos[0] * cube_piece.pos[2] == 0 and cube_piece.pos[0] + cube_piece.pos[2] != 0:
            return True
        else:
            return False
    except:
        print('something went wrong here#1')
        return "something went wrong here#1"
def is_Down_cross_solved(cube):#not sure if color changes still works
    if cube.get_piece(1,-1,0).colors[1] == cube.get_piece(-1,-1,0).colors[1] == cube.get_piece(0,-1,1).colors[1] == cube.get_piece(0,-1,-1).colors[1] == cube.get_piece(0,-1,0).colors[1] \
    and cube.get_piece(1,-1,0).colors[0] == cube.get_piece(1,0,0).colors[0] and cube.get_piece(-1,-1,0).colors[0] == cube.get_piece(-1,0,0).colors[0] \
    and cube.get_piece(0,-1,1).colors[2] == cube.get_piece(0,0,1).colors[2] and cube.get_piece(0,-1,-1).colors[2] == cube.get_piece(0,0,-1).colors[2]:
        return True
    else: 
        return False

'''
def branches(dic):
    for movement in product(*dic.values()):
        yield {k:v for k,v in zip(dic.keys(),movement)}
'''

def create_dic(d,number):
    for i in range(1,number+1):
        d[i] = ['U','Ui','U2','D','Di','D2','R','Ri','R2','L','Li','L2','F','Fi','F2','B','Bi','B2']
    #print(dictionary)
'''
class bruteforcer(object):
    def __init__(self,c):
        self.cube = c
'''
def bruteforce(cube,dic,dic_depth):
    temp_cube = rb.Cube(cube.flat_str())
    max_searching_length = dic_depth
    #print(temp_cube)
    for algs in product(*dic.values()):
        #print(algs)
        for i in range(1,min(max_searching_length, dic_depth)+1):
            move(temp_cube,algs[i-1])
            if is_Down_cross_solved(temp_cube):
                max_searching_length = min(max_searching_length,i)
                print(algs[:i])
        temp_cube = rb.Cube(cube.flat_str())
            #print("a")
            #print(cube)
#dic = {'1':['U','Ui','U2','R','Ri','R2','F','Fi','F2','L','Li','L2','D','Di','D2','B','Bi','B2'],'2':['U','Ui','U2','R','Ri','R2','F','Fi','F2','L','Li','L2','D','Di','D2','B','Bi','B2'],'3':['U','Ui','U2','R','Ri','R2','F','Fi','F2','L','Li','L2','D','Di','D2','B','Bi','B2'],'4':['U','Ui','U2','R','Ri','R2','F','Fi','F2','L','Li','L2','D','Di','D2','B','Bi','B2'],'5':['U','Ui','U2','R','Ri','R2','F','Fi','F2','L','Li','L2','D','Di','D2','B','Bi','B2']}
if __name__ == '__main__':
    main()
    