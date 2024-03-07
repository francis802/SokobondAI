#Blue is the piece that moves 
#Red the other symbols
#yellow is the wall
#The first 2 levels aHe easy, the next 2 medium and the others hand 

levels = {
    #Level 2 - Cell
    1: [
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ['y', 'H', 'H', None, 'O', 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', 'O', None, 'y', 'y', 'y'],
    ['y', 'y', 'y', 'y', None, None]],

    #Level 4 - Loop
    2: [
    ['y', 'y', 'y', 'y', 'y', 'y', 'y'],
    ['y', None, None, 'O', None, None, 'y'],
    ['y', None, None, 'y', None, None, 'y'],
    ['y', None, 'H', 'y', 'H', None, 'y'],
    ['y', None, None, 'y', None, None, 'y'],
    ['y', None, None, 'O', None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y']],

    #Level 13 - Scoop
    3: [
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
    ['y', None, None, 'H', None, 'O', None, None, 'y'],
    ['y', None, None, None, None, None, None, None, 'y'],
    ['y', None, 'H', None, 'H', None, 'H', None, 'y'],
    ['y', None, None, None, None, None, None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']],

    #Level 21 - Split (don't know how to implement the +)
    4: [
    [None, None, 'y', 'y', 'y', 'y', 'y', 'y', None, None],
    [None, None, 'y', None, None, None, None, 'y', None, None],
    [None, None, 'y', None, None, None, None, 'y', None, None],
    ['y', 'y', 'y', None, None, None, None, 'y', 'y', 'y'],
    ['y', 'H', 'H', None, None, None, None, None, 'O', 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']],

    #Level 23 - Lock
    5: [
    ['y', 'y', 'y', 'y', 'y', None],
    ['y', None, None, None, 'y', None],
    ['y', 'H', None, None, 'y', None],
    ['y', 'y', 'y', None, 'y', 'y'],
    ['y', 'O', None, None, None, 'y'],
    ['y', 'H', None, None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ],
    
    #Level 29 - Ring (not 100% because theres 2 blue pieces)
    6: [
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ['y', 'O', None, None, 'O', 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', 'O', None, None, 'O', 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ]
}
    
