#Eigth exercise: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums): #We opened new function. Name of the function is - spy_game
    sequence = [0, 0, 7] #List
    seq_index = 0 #Index
    for num in nums: #This loop is for checking elements in the nums. 
        if num = sequence[seq_index]: #If elements that we checking equal to the elements of the list "sequence".
            seq_index += 1 #We increment the index
            if seq_index == len(sequence): 
                return True
    return False #If we didn't find 007 sequence in the list, then we return False.

print(spy_game([1, 2, 4, 0, 0, 7, 5]))   
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#Why we used this operation "if seq_index == len(sequence):"?

# 1) When the loop finds 0, it will be seq_index = 1.
# 2) When the second 0 is found, seq_index = 2.
# 3) When 7 is found at the end, seq_index = 3. (Returns True because 3 == 3.)