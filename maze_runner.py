from maze_search import *

def create_complex_test_maze():
    """Creates a mazs with thre rooms for testing.
        Returns the start room to the maze."""
    #create rooms, mark the escape room or rooms.
    rmA = Room('A')
    rmB = Room('B')
    rmC = Room('C')
    rmD = Room('D')
    rmE = Room('E')
    rmF = Room('F')
    rmG = Room('G')
    rmH = Room('H')
    rmI = Room('I')
    rmJ = Room('J')
    rmK = Room('K')
    rmL = Room('L', is_esc=True)
    rmM = Room('M')
    rmN = Room('N')
    rmO = Room('O')
    rmP = Room('P', is_esc=True)
    rmQ = Room('Q')
    #set links
    rmA.room1=rmB
    rmA.room2=rmC
    rmA.room3=rmE
    rmA.room4=rmF
    rmC.room1=rmD
    rmF.room1=rmM
    rmF.room4=rmG
    rmM.room1=rmO
    rmM.room4=rmN
    rmO.room1=rmP
    rmO.room4=rmQ
    rmG.room3=rmI
    rmG.room4=rmH
    rmI.room3=rmJ
    rmJ.room3=rmK
    rmJ.room4=rmL
    return rmA

def create_simple_test_maze():
    """Creates a mazs with thre rooms for testing.
        Returns the start room to the maze."""
    #create rooms, make one as the escape room.
    rmA = Room('A')
    rmB = Room('B')
    rmC = Room('C', is_esc=True)
    #create links:
    rmA.room3=rmB
    rmA.room4=rmC
    return rmA

def print_list(iterator):
    """Notice that a list can produce an iterator."""
    out_str = ""
    for obj in iterator:
        out_str+=str(obj)+'\n'
    print(out_str)

if __name__=="__main__":
    
    # we suggest creating an instance of your Stack and testing it.
    start_room = create_simple_test_maze()
    #start_room = create_complex_test_maze()
    # you can make your own mazes as well.
    esc_list, visit_list = find_escapes(start_room)
    print("escape rooms\n")
    print_list(iter(esc_list))
    print("visited rooms\n")
    print_list(iter(visit_list))