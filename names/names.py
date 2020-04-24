import time
from binary_search_tree import BinarySearchTree

start_time = time.time()
def BTS_sol():
    f = open('names_1.txt', 'r')
    names_1 = f.read().split("\n")  # List containing 10000 names
    f.close()

    f = open('names_2.txt', 'r')
    names_2 = f.read().split("\n")  # List containing 10000 names
    f.close()

    duplicates = []  # Return the list of duplicates in this data structure

    # Replace the nested for loops below with your improvements runtime is O(n^2) or O(n)
    # for name_1 in names_1:
    #     for name_2 in names_2:
    #         if name_1 == name_2:
    #             duplicates.append(name_1)
    # create root for the BST
    binary = BinarySearchTree(names_1[0]) 
    # create a variable that incrememnts every time something gets added to the tree
    i = 1
    # create a loop that will insert each name into the tree and increment by one
    while i < len(names_1[1:]):
        binary.insert(names_1[i])
        i += 1
    # once the list has been exhausted loop through the second list of names, comparing it to the tree
    # list comprehesion that takes in the second list, and compares it to the binary tree pass in each name to the contains method
    duplicates = [dup for dup in names_2 if binary.contains(dup)]
    # return the dupes
    return duplicates

duplicates = BTS_sol() # run time is O(n log n) still linear but splitting in half 

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
