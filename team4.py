import random

team_name = 'Team 10' # Only 10 chars displayed.
strategy_name = 'Winning'
strategy_description = 'By not being stupid'
    
def move(my_history, their_history, my_score, their_score):
    dude = random.randint(1, 4)
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if 'b' in their_history[0]:
        return 'b'
    else:
        if 'b' in their_history[-1]:
            return 'b'
        else:
            if 'c' in their_history[-1] and dude == 3:
                return 'b'
            else:
                if 'c' in their_history[-2] and 'c' in their_history[-1] and dude == 1 or dude == 2:
                    return 'b'
                else:
                    return 'c'
                
                
            
            
            
            
            
            
            
            
            
            
            
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    