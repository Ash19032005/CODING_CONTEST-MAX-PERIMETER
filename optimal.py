def read_input_from_file(filename):
    with open(filename, 'r') as file:
        # Read the total number of elements from the first line
        n= int(file.readline().strip())
        # Initialize an empty list to store elements
        elements = []
        # Read the elements in chunks
        chunk_size = 10000  # Adjust the chunk size as needed
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file
            elements.extend(map(int, chunk.split()))
    return n,elements
n,nums = read_input_from_file("testcase12.txt")
nums.sort()
total=0
res=-1
for i in range(len(nums)):
    if total>nums[i]:
        res=total+nums[i]
    total+=nums[i]
print(res)