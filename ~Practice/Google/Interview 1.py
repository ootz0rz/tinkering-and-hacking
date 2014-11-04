'''
Part 1:

    Make every permutation of the following (or similarly formatted) list:

listOfLists = [ [ “the”, “a”, “one”], [“quick”, “slow”], [“cow”, “dog”, “fish”] ] 

    Ex:
        the quick cow
        the quick dog
        the quick fish
        the slow cow
        the slow dog
        the slow fish
        a quick cow
        ...
        one slow fish

    More Examples:
        [[ ‘a’ ]] => a
        [[ ‘a’, ‘b’ ]] => a, b
        [[ ‘a’ ], [‘b’, ‘c’]] => a b, a c
        [[ ‘a’, ‘b’ ], [‘c’, ‘d’]] => a c, a d, b c, b d
'''

def combination(list_of_lists):
    print '\n'.join(_combination(list_of_lists))

def _combination(list_of_lists):
    if len(list_of_lists) == 0:
        return ['']
    
    out = []
    for word in list_of_lists[0]:
        for word2 in _combination(list_of_lists[1:]):
            out.append(word + ' ' + word2)

    return out

'''
Part 2:

    Memory complexity of original solution was NxM (N = length of list, M = 
    number of elements per sub-list.)

    How can you make this more space-efficient?

    Idea: Solution above takes a bottom-up approach. We'll take a top-down
    approach instead. Build the solution at the current level, and then
    pass the current solution down to the next level. Finally print out every-
    thing at the bottom and end.
'''

def combination(list_of_lists):
    _combination(list_of_lists[1:], list_of_lists[0])

def _combination(list_of_lists, results_thus_far):
    if len(list_of_lists) == 0:
        print '\n'.join(results_thus_far)
        return
    
    out = []
    for idx, word2 in enumerate(results_thus_far):
        for word in list_of_lists[0]:
            out.append(word2 + ' ' + word)

    return combination(list_of_lists[1:], out)
    
