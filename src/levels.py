#blue is the piece that moves 
#red the other symbols
#yellow is the wall
#The first 2 levels are easy, the next 2 medium and the others hard 

levels = {
    #Level 2 - Cell
    1: [
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ['y', 'r', None, None, 'b', 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', 'r', None, 'y', 'y', 'y'],
    ['y', 'y', 'y', 'y', None, None]],

    #Level 4 - Loop
    2: [
    ['y', 'y', 'y', 'y', 'y', 'y', 'y'],
    ['y', None, None, 'b', None, None, 'y'],
    ['y', None, None, 'y', None, None, 'y'],
    ['y', None, 'r', 'y', 'r', None, 'y'],
    ['y', None, None, 'y', None, None, 'y'],
    ['y', None, None, 'b', None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y']],

    #Level 13 - Scoop
    3: [
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
    ['y', None, None, 'r', None, 'b', None, None, 'y'],
    ['y', None, None, None, None, None, None, None, 'y'],
    ['y', None, 'r', None, 'r', None, 'r', None, 'y'],
    ['y', None, None, None, None, None, None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']],

    #Level 21 - Split (don't know how to implement the +)
    4: [
    [None, None, 'y', 'y', 'y', 'y', 'y', 'y', None, None],
    [None, None, 'y', None, None, None, None, 'y', None, None],
    [None, None, 'y', None, None, None, None, 'y', None, None],
    ['y', 'y', 'y', None, None, None, None, 'y', 'y', 'y'],
    ['y', 'r', 'r', None, None, None, None, None, 'b', 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']],

    #Level 23 - Lock
    5: [
    ['y', 'y', 'y', 'y', 'y', None],
    ['y', None, None, None, 'y', None],
    ['y', 'r', None, None, 'y', None],
    ['y', 'y', 'y', None, 'y', 'y'],
    ['y', 'b', None, None, None, 'y'],
    ['y', 'r', None, None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ],
    
    #Level 29 - Ring (not 100% because theres 2 blue pieces)
    6: [
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ['y', 'b', None, None, 'b', 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', 'b', None, None, 'b', 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ]
}
    
