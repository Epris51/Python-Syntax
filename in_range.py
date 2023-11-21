def in_range(nums, lowest, highest):
    """Print numbers inside range."""
    for num in nums:
        if lowest <= num <= highest:
            print(f"{num} fits")

# Testing the function
in_range([10, 20, 30, 40, 50], 15, 30)
       
