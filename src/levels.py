#Blue is the piece that moves 
#Red the other symbols
#yellow is the wall
#The first 2 levels aHe easy, the next 2 medium and the others hand 

levels = {
    #Level 1 - Cell
    1: {"board" : [
    ['y', 'y', 'y', 'y', 'y', 'y'],
    ['y', 'H', None, None, 'O', 'y'],
    ['y', None, None, None, None, 'y'],
    ['y', None, 'H', 'y', 'y', 'y'],
    ['y', 'y', 'y', 'y', None, None]],
    "player_pos" : (1,1),
    "cut_pieces" : []
    },

    #Level 2 - Loop
    2: {"board" : [
    ['y', 'y', 'y', 'y', 'y', 'y', 'y'],
    ['y', None, None, 'O', None, None, 'y'],
    ['y', None, None, 'y', None, None, 'y'],
    ['y', None, 'H', 'y', 'H', None, 'y'],
    ['y', None, None, 'y', None, None, 'y'],
    ['y', None, None, 'O', None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y']],
    "player_pos" : (3,2),
    "cut_pieces" : []
    },

    #Level 3 - RoadRunner
    3: {"board" : [
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
    ['y', None, None, None, None, None, None, None, 'y'],
    ['y', None, None, 'H', None, 'H', None, None, 'y'],
    ['y', None, 'O', None, None, None, 'C', None, 'y'],
    ['y', None, None, 'H', None, 'H', None, None, 'y'],
    ['y', None, None, None, None, None, None, None, 'y'],
    ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']],
    "player_pos" : (3,2),
    "cut_pieces" : []
    },
    
    #Level 4 - Split
    4: {"board" : [
        [None,None,'y','y','y','y','y','y',None,None],
        [None,None,'y',None,None,None,None,'y',None,None],
        [None,None,'y',None,None,None,None,'y',None,None],
        ['y','y','y',None,None,None,None,'y','y','y'],
        ['y','H','H',None,None,None,None,None,'O','y'],
        ['y','y','y','y','y','y','y','y','y','y']],
        "player_pos" : (4,1),
        "cut_pieces" : [(3,5)]
    }
        
}
    
