

# Quemy_tiles: 
# In Scrabble1 each player has a set of tiles with letters on them. 
# The object of the game is to use those letters to spell words. 
# The scoring system is complex, but longer words are usually worth
#  more than shorter words.
# Imagine you are given your set of tiles as a string, like "quijibo", 
# and you are given another string to test, like "jib".
# Write a logic that takes two strings and checks whether the set of 
# tiles can spell the word. You might have more than one tile with the
#  same letter, but you can only use each tile once.

my_tiles = input("Enter string : ")
enemy_tiles = input("Enter substring : ")
        

def can_spell(my_tiles, enemy_tiles):
    
    tiles_used = [0] * len(my_tiles)

    for x in enemy_tiles:
        found = False
        for y in range(len(my_tiles)):
            if x == my_tiles[y] and tiles_used[y] == 0:
                tiles_used[y] = 1
                found = True
                break
        
        if(found):
            continue
        else:
            return False
    
    return True

print(can_spell(my_tiles, enemy_tiles))