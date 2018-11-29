import random

team_name = 'Team 10' # Only 10 chars displayed.
strategy_name = 'Winning'
strategy_description = 'By not being stupid'   

def move(my_history, their_history, my_score, their_score):
    if len(their_history) == 99 or len(their_history) == 149 or len(their_history) == 69:
        return 'b'
    else:
        if len(their_history) >= 2:
            if 'b' in their_history[0]:
                return 'b'
            else:
                if 'b' in their_history[-2]:
                    return 'b'
                else:
                    dude = random.randint(1, 4)
                    if 'c' in their_history[-1] and 'c' in their_history[-2] and dude == 1 or dude == 2:
                        return 'b'
                    else:
                        guy = random.randint(1, 3)
                        return 'c'
                        if 'c' in their_history[-1] and guy == 2:
                            return 'b'
                        else:
                            prob = random.randint(0,5)
                            if prob == 2:
                                return 'b'
                            else:
                                return 'c'
        else:
            if len(their_history) >= 1:
                if 'b' in their_history[0]:
                    return 'b'
                else:
                    if 'b' in their_history[-1]:
                        return 'b'
                    else:
                        if 'c' in their_history[-1] and dude == 3:
                            return 'b'
                        else:
                            return 'c'
            else:
                return 'c'
           
'''      
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'. 
'''
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='c')             