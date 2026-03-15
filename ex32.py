# Exercise 32: Zip and Enumerate Mapping
# Practice Problem: You have two separate lists: one of student names and one of their exam scores. Use zip() to combine them into a dictionary, 
# then use enumerate() to print a ranked list (1st, 2nd, 3rd…).

# Given Input:

# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
# Expected Output:

# Rank 1: Bob scored 92
# Rank 2: Alice scored 85
# Rank 3: Charlie scored 78

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

score_map= dict(zip(names, scores) )

sorted_map = sorted(score_map.items(), key = lambda x : x[1], reverse = True)

print(sorted_map)

for i, (name, score) in enumerate(sorted_map, start=1) :
    print(f"Rank {i}: {name} scored {score}")
