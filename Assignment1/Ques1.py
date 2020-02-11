

# Ques1: 
# In Scrabble1 each player has a set of tiles with letters on them. 
# The object of the game is to use those letters to spell words. 
# The scoring system is complex, but longer words are usually worth
#  more than shorter words.
# Imagine you are given your set of tiles as a string, like "quijibo", 
# and you are given another string to test, like "jib".
# Write a logic that takes two strings and checks whether the set of 
# tiles can spell the word. You might have more than one tile with the
#  same letter, but you can only use each tile once.

s1 = input("Enter string : ")
s2 = input("Enter substring : ")
        

def canSpell(s1, s2):
    listS1 = [0] * len(s1)

    for x in s2:
        found = False
        for y in range(0,len(s1)):
            if x == s1[y] and listS1[y] == 0:
                listS1[y] = 1
                found = True
                break
        
        if(found):
            continue
        else:
            return False
    
    return True

print(canSpell(s1, s2))