#Blue is the piece that moves 
#Red the other symbols
#yellow is the wall
#The first 2 levels aHe easy, the next 2 medium and the others hand 

levels = {
    #Level 2 - Cell
    1: {"board" : [
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ['y', 'H', None, None, 'O', 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', None, 'H', 'y', 'y', 'y'],
    ['y', 'y', 'y', 'y', None, None]],
    "player_pos" : (1,1)
    },

    #Level 4 - Loop
    2: {"board" : [
    ['y', 'y', 'y', 'y', 'y', 'y', 'y'],
    ['y', None, None, 'O', None, None, 'y'],
    ['y', None, None, 'y', None, None, 'y'],
    ['y', None, 'H', 'y', 'H', None, 'y'],
    ['y', None, None, 'y', None, None, 'y'],
    ['y', None, None, 'O', None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y']],
    "player_pos" : (3,2)
    },

    #Level 13 - Scoop
    3: {"board" : [
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
    ['y', None, None, 'H', None, 'O', None, None, 'y'],
    ['y', None, None, None, None, None, None, None, 'y'],
    ['y', None, 'H', None, 'H', None, 'H', None, 'y'],
    ['y', None, None, None, None, None, None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']],
    "player_pos" : (3,3)
    },

    #Level 21 - Split (don't know how to implement the +)
    4: {"board" : [
    [None, None, 'y', 'y', 'y', 'y', 'y', 'y', None, None],
    [None, None, 'y', None, None, None, None, 'y', None, None],
    [None, None, 'y', None, None, None, None, 'y', None, None],
    ['y', 'y', 'y', None, None, None, None, 'y', 'y', 'y'],
    ['y', 'H', 'H', None, None, None, None, None, 'O', 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']],
    "player_pos" : (4,1)
    },

    #Level 23 - Lock
    5: {"board" : [
    ['y', 'y', 'y', 'y', 'y', None],
    ['y', None, None, None, 'y', None],
    ['y', 'H', None, None, 'y', None],
    ['y', 'y', 'y', None, 'y', 'y'],
    ['y', 'O', None, None, None, 'y'],
    ['y', 'H', None, None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y']],
    "player_pos" : (4,1)
    },
    
    #Level 29 - Ring (not 100% because theres 2 blue pieces)
    6: {"board" : [
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ['y', 'O', None, None, 'O', 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', 'O', None, None, 'O', 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y']],
    "player_pos" : (2,2)
    },
}
    
