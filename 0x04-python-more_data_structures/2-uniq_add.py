def uniq_add(my_list=[]):
    unique_sum = 0  # Initialize a variable to store the sum of unique integers
    seen = set()   # Create a set to keep track of seen integers
    
    for num in my_list:
        if num not in seen:
            unique_sum += num   # Add the unique integer to the sum
            seen.add(num)       # Add the integer to the set to mark it as seen
    
    return unique_sum
