# Step 1: Create an empty list
my_list = []

# Step 2: Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend my_list with another list
my_list.extend([50, 60, 70])

# Step 5: Remove the last element from my_list
my_list.pop()  # This removes the last element (70)

# Step 6: Sort my_list in ascending order
my_list.sort()

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)

# Optional: Print the final state of my_list
print("Final list:", my_list)
