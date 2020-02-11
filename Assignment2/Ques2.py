
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


voteCast = ["john", "johnny", "jackie", "johnny",
         "john", "jackie", "jamie", "jamie", 
         "john",  "johnny", "jamie", "johnny", "john"]

votesCount = {}

for v in voteCast:
    candidates = votesCount.keys()
    if v in candidates:
        votesCount[v] = votesCount[v] + 1
    else:
        votesCount[v] = 1
    
# print(votesCount)

winner = ""
max = 0

for candidate, votes in votesCount.items():

    print(candidate, votes, max, winner)
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
     
