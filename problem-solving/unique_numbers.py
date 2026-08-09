# # Unique Numbers

# Given the following list of integers:

# ```python
# numbers = [12, 7, 19, 4, 12, 8, 19, 3, 7, 15, 4]
# ```

# Write a Python program using a `for` loop to print each number only once, while preserving the original order of the elements.

# ### Requirements

# * Use a `for` loop.
# * Do not use `set()`.
# * Do not use `count()`.
# * Do not import any external libraries.
# * The original order of the numbers must be preserved.

# ### Expected Output

# ```text
# 12
# 7
# 19
# 4
# 8
# 3
# 15
# ```

# ### Bonus Challenge

# Modify your program so that it also displays how many times each unique number appears in the list.

# Example:

# ```text
# 12 -> 2
# 7 -> 2
# 19 -> 2
# 4 -> 2
# 8 -> 1
# 3 -> 1
# 15 -> 1
# ```

numbers = [12, 7, 19, 4, 12, 8, 19, 3, 7, 15, 4]

unique = []
unique.append(numbers[0])

count_numbers = []

for a in numbers :
    for b in unique :
        if a == b:
            break
    else :
        unique.append(a)


for c in unique : 
        i = 0
        for d in numbers :
            if c == d :
                i+=1
        count_numbers.append(i)

for num in unique : 
    print(num)

for e,f in zip(unique,count_numbers) : 
    print(f"{e} -> {f}")
