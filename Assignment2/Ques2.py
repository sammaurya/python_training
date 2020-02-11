
# Ques2:
# Given an array of names of candidates in an election. 
# A candidate name in array represents a vote casted to the candidate. 
# Print the name of candidates received Max vote. 
# If there is a tie, print lexicographically smaller name.

# Examples:

# Input :  votes[] = {"john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"};
# Output : John

# We have four Candidates with name as 'John', 
# 'Johnny', 'jamie', 'jackie'. The candidates
# John and Johnny get maximum votes. Since John
# is alphabetically smaller, we print it.


vote_cast = ["john", "johnny", "jackie", "johnny",
         "john", "jackie", "jamie", "jamie", 
         "john",  "johnny", "jamie", "johnny", "john"]

votes_count = {}

for v in vote_cast:
    candidates = votes_count.keys()
    if v in candidates:
        votes_count[v] += 1
    else:
        votes_count[v] = 1

winner = ""
max = 0

for candidate, votes in votes_count.items():
    
    if max == 0:
        winner = candidate
        max = votes

    elif votes > max:
        winner = candidate
        max = votes

    elif votes == max:
        if winner > candidate:
            winner = candidate
    
    
print(winner)
     
