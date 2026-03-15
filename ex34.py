# Exercise 34: Set Operations for Data Analysis
# Exercise Purpose: Sets are not just for removing duplicates; 
# they are powerful mathematical tools for comparing collections. 
# Using set logic is much faster and more readable than writing multiple for loops with if conditions.

# Given Input:

# trial = [1, 2, 3, 4, 5]
# paid = [4, 5, 6, 7, 8]
# Expected Output:

# Upgraded (Both): {4, 5}
# Leads (Trial only): {1, 2, 3}
# Unique Status (Not both): {1, 2, 3, 6, 7, 8}

trial = set([1, 2, 3, 4, 5])
paid = set([4, 5, 6, 7, 8])

print( trial.intersection(paid) )
print( trial.difference(paid) )
print( trial.symmetric_difference(paid) )
